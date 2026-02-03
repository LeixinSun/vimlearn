"""User management for VimLearn."""

import json
from datetime import datetime
from pathlib import Path
from typing import Optional


def get_user_dir() -> Path:
    """Get the user data directory."""
    user_dir = Path.home() / ".vimlearn" / "users"
    user_dir.mkdir(parents=True, exist_ok=True)
    return user_dir


def get_user_file(username: str) -> Path:
    """Get the path to a user's data file."""
    return get_user_dir() / f"{username}.json"


class User:
    """Represents a VimLearn user with their progress."""

    def __init__(
        self,
        username: str,
        created_at: Optional[str] = None,
        last_active: Optional[str] = None,
        current_lesson: str = "1.1",
        completed_lessons: Optional[list[str]] = None,
        stats: Optional[dict] = None,
    ):
        self.username = username
        self.created_at = created_at or datetime.now().isoformat()
        self.last_active = last_active or datetime.now().isoformat()
        self.current_lesson = current_lesson
        self.completed_lessons = completed_lessons or []
        self.stats = stats or {
            "total_exercises": 0,
            "successful_first_try": 0,
            "total_attempts": 0,
        }

    def to_dict(self) -> dict:
        """Convert user to dictionary for JSON serialization."""
        return {
            "username": self.username,
            "created_at": self.created_at,
            "last_active": self.last_active,
            "current_lesson": self.current_lesson,
            "completed_lessons": self.completed_lessons,
            "stats": self.stats,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """Create a User from a dictionary."""
        return cls(
            username=data["username"],
            created_at=data.get("created_at"),
            last_active=data.get("last_active"),
            current_lesson=data.get("current_lesson", "1.1"),
            completed_lessons=data.get("completed_lessons", []),
            stats=data.get("stats"),
        )

    def save(self) -> None:
        """Save user data to file."""
        self.last_active = datetime.now().isoformat()
        user_file = get_user_file(self.username)
        with open(user_file, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2, ensure_ascii=False)

    @classmethod
    def load(cls, username: str) -> Optional["User"]:
        """Load a user from file."""
        user_file = get_user_file(username)
        if not user_file.exists():
            return None
        with open(user_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls.from_dict(data)

    @classmethod
    def create(cls, username: str) -> "User":
        """Create a new user."""
        user = cls(username=username)
        user.save()
        return user

    @classmethod
    def load_or_create(cls, username: str) -> "User":
        """Load an existing user or create a new one."""
        user = cls.load(username)
        if user is None:
            user = cls.create(username)
        return user

    def complete_lesson(self, lesson_id: str) -> None:
        """Mark a lesson as completed."""
        if lesson_id not in self.completed_lessons:
            self.completed_lessons.append(lesson_id)
        self.save()

    def record_exercise(self, success: bool, first_try: bool) -> None:
        """Record an exercise attempt."""
        self.stats["total_exercises"] += 1
        self.stats["total_attempts"] += 1
        if success and first_try:
            self.stats["successful_first_try"] += 1
        self.save()

    def record_attempt(self) -> None:
        """Record an additional attempt (retry)."""
        self.stats["total_attempts"] += 1
        self.save()

    def set_current_lesson(self, lesson_id: str) -> None:
        """Set the current lesson."""
        self.current_lesson = lesson_id
        self.save()

    def get_progress_percentage(self, total_lessons: int) -> float:
        """Calculate progress percentage."""
        if total_lessons == 0:
            return 0.0
        return (len(self.completed_lessons) / total_lessons) * 100

    def reset_progress(self) -> None:
        """Reset all progress."""
        self.current_lesson = "1.1"
        self.completed_lessons = []
        self.stats = {
            "total_exercises": 0,
            "successful_first_try": 0,
            "total_attempts": 0,
        }
        self.save()


def list_users() -> list[str]:
    """List all existing users."""
    user_dir = get_user_dir()
    return [f.stem for f in user_dir.glob("*.json")]
