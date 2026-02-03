"""Lesson data structures for VimLearn."""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Exercise:
    """Represents a single exercise within a lesson."""

    instruction: str
    initial: str
    expected: str
    hint: str
    commands_to_learn: list[str] = field(default_factory=list)
    cursor_position: Optional[int] = None


@dataclass
class Lesson:
    """Represents a single lesson."""

    id: str
    title: str
    module: str
    module_num: int
    description: str
    explanation: str
    exercises: list[Exercise]
    why: Optional[str] = None

    @property
    def lesson_num(self) -> int:
        """Get the lesson number within the module."""
        return int(self.id.split(".")[1])


@dataclass
class Module:
    """Represents a module containing multiple lessons."""

    num: int
    title: str
    description: str
    lessons: list[Lesson] = field(default_factory=list)


def parse_lesson_id(lesson_id: str) -> tuple[int, int]:
    """Parse a lesson ID into module and lesson numbers."""
    parts = lesson_id.split(".")
    return int(parts[0]), int(parts[1])


def get_next_lesson_id(current_id: str, all_lessons: list[Lesson]) -> Optional[str]:
    """Get the next lesson ID after the current one."""
    lesson_ids = [lesson.id for lesson in all_lessons]
    try:
        current_index = lesson_ids.index(current_id)
        if current_index + 1 < len(lesson_ids):
            return lesson_ids[current_index + 1]
    except ValueError:
        pass
    return None


def get_previous_lesson_id(current_id: str, all_lessons: list[Lesson]) -> Optional[str]:
    """Get the previous lesson ID before the current one."""
    lesson_ids = [lesson.id for lesson in all_lessons]
    try:
        current_index = lesson_ids.index(current_id)
        if current_index > 0:
            return lesson_ids[current_index - 1]
    except ValueError:
        pass
    return None
