"""Exercise verification for VimLearn."""

import os
import subprocess
import tempfile
import uuid
from pathlib import Path
from typing import Optional

from .lesson import Exercise


class ExerciseRunner:
    """Handles exercise file creation, vim execution, and verification."""

    def __init__(self):
        self.temp_dir = Path(tempfile.gettempdir())
        self.current_file: Optional[Path] = None

    def create_exercise_file(self, exercise: Exercise) -> Path:
        """Create a temporary file with the exercise's initial content."""
        filename = f"vimlearn_exercise_{uuid.uuid4().hex[:8]}.txt"
        self.current_file = self.temp_dir / filename
        with open(self.current_file, "w", encoding="utf-8") as f:
            f.write(exercise.initial)
        return self.current_file

    def run_vim(self, filepath: Path, cursor_position: Optional[int] = None) -> bool:
        """Open vim with the exercise file. Returns True if vim exited normally."""
        vim_cmd = ["vim"]

        if cursor_position is not None:
            # Position cursor at specific column on first line
            vim_cmd.extend(["-c", f"call cursor(1, {cursor_position + 1})"])

        vim_cmd.append(str(filepath))

        try:
            result = subprocess.run(vim_cmd)
            return result.returncode == 0
        except FileNotFoundError:
            return False

    def verify_result(self, exercise: Exercise) -> tuple[bool, str, str]:
        """
        Verify the exercise result.

        Returns:
            tuple: (success, actual_content, expected_content)
        """
        if self.current_file is None or not self.current_file.exists():
            return False, "", exercise.expected

        with open(self.current_file, "r", encoding="utf-8") as f:
            actual = f.read()

        # Normalize: strip trailing whitespace from each line and trailing newlines
        actual_normalized = "\n".join(line.rstrip() for line in actual.rstrip("\n").split("\n"))
        expected_normalized = "\n".join(line.rstrip() for line in exercise.expected.rstrip("\n").split("\n"))

        success = actual_normalized == expected_normalized
        return success, actual, exercise.expected

    def cleanup(self) -> None:
        """Remove the temporary exercise file."""
        if self.current_file and self.current_file.exists():
            try:
                os.remove(self.current_file)
            except OSError:
                pass
            self.current_file = None

    def run_exercise(self, exercise: Exercise) -> tuple[bool, str, str]:
        """
        Run a complete exercise cycle.

        Returns:
            tuple: (success, actual_content, expected_content)
        """
        filepath = self.create_exercise_file(exercise)
        vim_success = self.run_vim(filepath, exercise.cursor_position)

        if not vim_success:
            return False, "", exercise.expected

        return self.verify_result(exercise)
