"""Main entry point for VimLearn CLI."""

import shutil
import typer
from typing import Optional

from .user import User, list_users
from .lesson import get_next_lesson_id, parse_lesson_id
from .lessons import MODULES, get_lesson, get_all_lessons
from .exercise import ExerciseRunner
from . import ui

app = typer.Typer(
    name="vimlearn",
    help="交互式 Vim 学习工具",
    add_completion=False,
)


def check_vim_installed() -> bool:
    """Check if vim is installed."""
    return shutil.which("vim") is not None


@app.command()
def start(
    username: Optional[str] = typer.Option(None, "--user", "-u", help="用户名"),
    lesson: Optional[str] = typer.Option(None, "--lesson", "-l", help="指定课程 ID (如 1.1)"),
):
    """开始学习 Vim。"""
    if not check_vim_installed():
        ui.print_vim_not_found()
        raise typer.Exit(1)

    ui.clear_screen()
    ui.print_welcome()

    # Get or create user
    if username is None:
        username = ui.prompt_username()
        if not username:
            ui.print_error("用户名不能为空")
            raise typer.Exit(1)

    user = User.load_or_create(username)

    # Determine starting lesson
    if lesson:
        if get_lesson(lesson) is None:
            ui.print_error(f"课程 {lesson} 不存在")
            raise typer.Exit(1)
        user.set_current_lesson(lesson)

    run_learning_session(user)


def run_learning_session(user: User) -> None:
    """Run the main learning session loop."""
    all_lessons = get_all_lessons()
    runner = ExerciseRunner()

    while True:
        current_lesson = get_lesson(user.current_lesson)
        if current_lesson is None:
            ui.print_all_complete()
            break

        # Calculate progress info
        module_num, lesson_num = parse_lesson_id(current_lesson.id)
        module_lessons = [l for l in all_lessons if l.module_num == module_num]
        total_lessons_in_module = len(module_lessons)

        ui.clear_screen()
        ui.print_header(
            user=user,
            total_lessons=len(all_lessons),
            current_module=module_num,
            total_modules=len(MODULES),
            current_lesson_in_module=lesson_num,
            total_lessons_in_module=total_lessons_in_module,
        )

        ui.print_lesson_header(current_lesson)
        ui.print_explanation(current_lesson.explanation)

        # Run exercises
        lesson_completed = run_lesson_exercises(user, current_lesson, runner)

        if not lesson_completed:
            # User quit
            break

        # Mark lesson complete and move to next
        user.complete_lesson(current_lesson.id)
        ui.print_lesson_complete(current_lesson)

        # Check if module is complete
        module_lesson_ids = [l.id for l in module_lessons]
        if all(lid in user.completed_lessons for lid in module_lesson_ids):
            ui.print_module_complete(module_num, current_lesson.module)

        # Move to next lesson
        next_lesson_id = get_next_lesson_id(current_lesson.id, all_lessons)
        if next_lesson_id:
            user.set_current_lesson(next_lesson_id)
            ui.wait_for_key()
        else:
            ui.print_all_complete()
            break

    runner.cleanup()


def run_lesson_exercises(user: User, lesson, runner: ExerciseRunner) -> bool:
    """
    Run all exercises in a lesson.
    Returns True if all exercises completed, False if user quit.
    """
    exercises = lesson.exercises
    total_exercises = len(exercises)

    for i, exercise in enumerate(exercises, 1):
        ui.print_exercise(exercise, i, total_exercises)
        ui.print_exercise_menu()

        first_try = True
        while True:
            action = ui.prompt_action()

            if action == "0":
                return False
            elif action == "4":
                # Skip exercise
                break
            elif action == "2":
                ui.print_hint(exercise.hint)
            elif action == "3":
                if lesson.why:
                    ui.print_why(lesson.why)
                else:
                    ui.print_info("本课程没有设计原因说明")
            elif action == "1":
                # Run the exercise
                success, actual, expected = runner.run_exercise(exercise)

                if success:
                    ui.print_success()
                    user.record_exercise(success=True, first_try=first_try)
                    # Show success menu and let user choose
                    while True:
                        ui.print_success_menu()
                        post_action = ui.prompt_action()
                        if post_action == "1":
                            # Next exercise
                            break
                        elif post_action == "2":
                            ui.print_hint(exercise.hint)
                        elif post_action == "3":
                            if lesson.why:
                                ui.print_why(lesson.why)
                            else:
                                ui.print_info("本课程没有设计原因说明")
                        elif post_action == "0":
                            return False
                    break
                else:
                    ui.print_failure(actual, expected)
                    user.record_exercise(success=False, first_try=first_try)
                    first_try = False
                    # Show retry menu and handle actions
                    while True:
                        ui.print_retry_menu()
                        retry_action = ui.prompt_action()
                        if retry_action == "0":
                            return False
                        elif retry_action == "4":
                            # Skip
                            break
                        elif retry_action == "5":
                            # Pass anyway
                            ui.print_info("已强制通过此练习")
                            break
                        elif retry_action == "2":
                            ui.print_hint(exercise.hint)
                        elif retry_action == "1":
                            # Retry - break inner loop to retry exercise
                            success, actual, expected = runner.run_exercise(exercise)
                            if success:
                                ui.print_success()
                                user.record_exercise(success=True, first_try=False)
                                while True:
                                    ui.print_success_menu()
                                    post_action = ui.prompt_action()
                                    if post_action == "1":
                                        break
                                    elif post_action == "2":
                                        ui.print_hint(exercise.hint)
                                    elif post_action == "3":
                                        if lesson.why:
                                            ui.print_why(lesson.why)
                                        else:
                                            ui.print_info("本课程没有设计原因说明")
                                    elif post_action == "0":
                                        return False
                                break
                            else:
                                ui.print_failure(actual, expected)
                    break

    return True


@app.command()
def lessons():
    """显示所有课程列表。"""
    ui.clear_screen()
    ui.print_modules_list(MODULES, [])
    ui.console.print()


@app.command()
def progress(
    username: str = typer.Argument(..., help="用户名"),
):
    """查看学习进度。"""
    user = User.load(username)
    if user is None:
        ui.print_error(f"用户 {username} 不存在")
        raise typer.Exit(1)

    all_lessons = get_all_lessons()
    ui.clear_screen()
    ui.print_progress_stats(user, len(all_lessons))
    ui.print_modules_list(MODULES, user.completed_lessons)


@app.command()
def reset(
    username: str = typer.Argument(..., help="用户名"),
):
    """重置用户进度。"""
    user = User.load(username)
    if user is None:
        ui.print_error(f"用户 {username} 不存在")
        raise typer.Exit(1)

    if ui.confirm(f"确定要重置用户 {username} 的所有进度吗？"):
        user.reset_progress()
        ui.print_info("进度已重置")
    else:
        ui.print_info("已取消")


if __name__ == "__main__":
    app()
