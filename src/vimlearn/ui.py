"""Terminal UI components for VimLearn using rich."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box

from .lesson import Lesson, Exercise, Module
from .user import User


console = Console()

# 统一的分隔线
SEPARATOR = "─" * 60


def clear_screen() -> None:
    """Clear the terminal screen."""
    console.clear()


def print_header(user: User, total_lessons: int, current_module: int, total_modules: int, current_lesson_in_module: int, total_lessons_in_module: int) -> None:
    """Print the application header with user info and progress."""
    progress_pct = user.get_progress_percentage(total_lessons)
    progress_bar = create_progress_bar(progress_pct)

    header_text = Text()
    header_text.append("VimLearn - 交互式 Vim 学习\n", style="bold cyan")
    header_text.append(SEPARATOR + "\n", style="dim")
    header_text.append("用户: ", style="dim")
    header_text.append(f"{user.username}    ", style="bold yellow")
    header_text.append(f"进度: {progress_bar} {progress_pct:.0f}%\n", style="dim")
    header_text.append(f"当前: 模块 {current_module}/{total_modules}  |  课程 {current_lesson_in_module}/{total_lessons_in_module}", style="dim")

    console.print(Panel(header_text, box=box.ROUNDED, border_style="blue"))


def create_progress_bar(percentage: float, width: int = 20) -> str:
    """Create a text-based progress bar."""
    filled = int(width * percentage / 100)
    empty = width - filled
    return "█" * filled + "░" * empty


def print_lesson_header(lesson: Lesson) -> None:
    """Print the lesson header."""
    console.print()
    console.print(f"[模块 {lesson.module_num}] {lesson.module}", style="bold magenta")
    console.print(f"[课程 {lesson.id}] {lesson.title}", style="bold green")
    console.print()


def print_explanation(explanation: str) -> None:
    """Print the lesson explanation in a panel."""
    console.print(Panel(
        explanation.strip(),
        title="讲解",
        title_align="left",
        border_style="cyan",
        box=box.ROUNDED,
    ))


def print_why(why: str) -> None:
    """Print the design philosophy explanation."""
    console.print()
    console.print(Panel(
        why.strip(),
        title="为什么这样设计？",
        title_align="left",
        border_style="yellow",
        box=box.ROUNDED,
    ))


def print_exercise(exercise: Exercise, exercise_num: int, total_exercises: int) -> None:
    """Print an exercise."""
    console.print()
    console.print(SEPARATOR, style="dim")
    console.print()
    console.print(f"练习 {exercise_num}/{total_exercises}: {exercise.instruction}", style="bold white")
    console.print()

    # Initial content
    console.print("[dim]初始内容:[/dim]")
    console.print(Panel(
        exercise.initial or "(空文件)",
        border_style="white",
        box=box.ROUNDED,
    ))

    # Expected content
    console.print("[dim]目标内容:[/dim]")
    console.print(Panel(
        exercise.expected or "(空文件)",
        border_style="green",
        box=box.ROUNDED,
    ))

    # Commands to learn
    if exercise.commands_to_learn:
        commands = "  ".join([f"[bold cyan]{cmd}[/bold cyan]" for cmd in exercise.commands_to_learn])
        console.print(f"本练习命令: {commands}")


def print_hint(hint: str) -> None:
    """Print a hint."""
    console.print()
    console.print(Panel(
        hint,
        title="提示",
        title_align="left",
        border_style="yellow",
        box=box.ROUNDED,
    ))


def print_menu(options: list[tuple[str, str]]) -> None:
    """Print a menu with options. Each option is (key, label)."""
    menu_items = "  ".join([f"[bold cyan]{key}[/bold cyan] {label}" for key, label in options])
    console.print()
    console.print(SEPARATOR)
    console.print(menu_items)


def print_exercise_menu() -> None:
    """Print the exercise action menu."""
    print_menu([
        ("1", "开始练习"),
        ("2", "显示提示"),
        ("3", "设计原因"),
        ("4", "跳过"),
        ("0", "退出"),
    ])


def print_success() -> None:
    """Print success message."""
    console.print()
    console.print(Panel(
        "练习完成！",
        border_style="green",
        box=box.ROUNDED,
    ))


def print_success_menu() -> None:
    """Print menu after successful exercise."""
    print_menu([
        ("1", "下一个"),
        ("2", "显示提示"),
        ("3", "设计原因"),
        ("0", "退出"),
    ])


def print_failure(actual: str, expected: str) -> None:
    """Print failure message with diff."""
    console.print()
    console.print(Panel(
        "结果不匹配，请再试一次",
        border_style="red",
        box=box.ROUNDED,
    ))
    console.print()

    # 使用表格并排显示对比
    table = Table(show_header=True, box=box.ROUNDED, border_style="dim")
    table.add_column("你的结果", style="red", width=30)
    table.add_column("期望结果", style="green", width=30)
    table.add_row(actual or "(空)", expected or "(空)")
    console.print(table)


def print_retry_menu() -> None:
    """Print retry menu after failure."""
    print_menu([
        ("1", "重试"),
        ("2", "显示提示"),
        ("4", "跳过"),
        ("5", "强制通过"),
        ("0", "退出"),
    ])


def print_lesson_complete(lesson: Lesson) -> None:
    """Print lesson completion message."""
    console.print()
    console.print(Panel(
        f"课程 {lesson.id}: {lesson.title} 完成！",
        border_style="green",
        box=box.DOUBLE,
    ))


def print_module_complete(module_num: int, module_title: str) -> None:
    """Print module completion message."""
    console.print()
    console.print(Panel(
        f"模块 {module_num}: {module_title} 全部完成！",
        border_style="yellow",
        box=box.DOUBLE,
    ))


def print_all_complete() -> None:
    """Print all lessons complete message."""
    console.print()
    console.print(Panel(
        "恭喜你完成了所有课程！",
        border_style="magenta",
        box=box.DOUBLE,
    ))


def print_modules_list(modules: list[Module], completed_lessons: list[str]) -> None:
    """Print a list of all modules and their lessons."""
    for module in modules:
        console.print()
        console.print(f"[模块 {module.num}] {module.title}", style="bold magenta")
        console.print(f"  {module.description}", style="dim")

        for lesson in module.lessons:
            if lesson.id in completed_lessons:
                console.print(f"  [green]✓[/green] {lesson.id}: {lesson.title}", style="green")
            else:
                console.print(f"    {lesson.id}: {lesson.title}", style="white")


def print_progress_stats(user: User, total_lessons: int) -> None:
    """Print detailed progress statistics."""
    console.print()
    console.print(Panel(
        f"学习统计 - {user.username}",
        border_style="cyan",
        box=box.DOUBLE,
    ))

    table = Table(show_header=False, box=box.SIMPLE)
    table.add_column("项目", style="dim", width=15)
    table.add_column("数值", style="bold")

    completed = len(user.completed_lessons)
    progress_pct = user.get_progress_percentage(total_lessons)

    table.add_row("已完成课程", f"{completed} / {total_lessons}")
    table.add_row("完成进度", f"{progress_pct:.1f}%")
    table.add_row("当前课程", user.current_lesson)
    table.add_row("练习总数", str(user.stats["total_exercises"]))
    table.add_row("一次通过", str(user.stats["successful_first_try"]))
    table.add_row("总尝试次数", str(user.stats["total_attempts"]))

    if user.stats["total_exercises"] > 0:
        first_try_rate = (user.stats["successful_first_try"] / user.stats["total_exercises"]) * 100
        table.add_row("一次通过率", f"{first_try_rate:.1f}%")

    console.print(table)


def print_welcome() -> None:
    """Print welcome message."""
    welcome_text = """
欢迎使用 VimLearn！

这是一个交互式 Vim 学习工具。你将在这里学习 Vim 的各种命令和技巧，
然后在真实的 Vim 编辑器中完成练习。

学习流程：
  1. 阅读课程讲解，理解命令的用法
  2. 查看练习要求和目标
  3. 按 1 启动 Vim 进行练习
  4. 在 Vim 中完成编辑后保存退出 (:wq)
  5. 工具会自动验证你的结果

准备好了吗？让我们开始吧！
"""
    console.print(Panel(
        welcome_text.strip(),
        title="VimLearn",
        title_align="left",
        border_style="cyan",
        box=box.DOUBLE,
    ))


def prompt_username() -> str:
    """Prompt for username."""
    console.print()
    return console.input("[bold cyan]请输入用户名: [/bold cyan]").strip()


def prompt_action(prompt: str = "") -> str:
    """Prompt for a single character action."""
    if prompt:
        console.print(prompt, style="dim")
    return console.input("[bold cyan]请选择 > [/bold cyan]").strip().lower()


def confirm(message: str) -> bool:
    """Ask for confirmation."""
    response = console.input(f"[bold yellow]{message} (y/n): [/bold yellow]").strip().lower()
    return response in ("y", "yes", "是")


def print_error(message: str) -> None:
    """Print an error message."""
    console.print(f"[bold red]错误: {message}[/bold red]")


def print_info(message: str) -> None:
    """Print an info message."""
    console.print(f"[cyan]{message}[/cyan]")


def print_vim_not_found() -> None:
    """Print vim not found error."""
    console.print(Panel(
        "未找到 Vim！请确保 Vim 已安装并在 PATH 中。\n\n"
        "安装方法:\n"
        "  macOS:   brew install vim\n"
        "  Ubuntu:  sudo apt install vim\n"
        "  Windows: 下载 gvim 或使用 WSL",
        border_style="red",
        box=box.ROUNDED,
    ))


def wait_for_key() -> None:
    """Wait for user to press Enter."""
    console.input("\n[dim]按 Enter 继续...[/dim]")
