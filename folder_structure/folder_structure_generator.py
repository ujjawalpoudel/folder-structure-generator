from __future__ import annotations

from pathlib import Path
from typing import Iterable, List, Optional, Union


DEFAULT_IGNORED_FOLDERS = (
    "__pycache__",
    ".git",
    ".idea",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".tox",
    ".venv",
    "build",
    "dist",
    "env",
    "node_modules",
    "venv",
)


class FolderStructureGenerator:
    """Generate a Markdown-friendly tree for a project directory."""

    def __init__(
        self,
        ignored_folders: Optional[Iterable[str]] = None,
        *,
        include_files: bool = True,
        include_hidden: bool = True,
        max_depth: Optional[int] = None,
    ) -> None:
        """
        Create a folder structure generator.

        Args:
            ignored_folders: Folder names or relative paths to exclude.
            include_files: Include files as well as folders in the output.
            include_hidden: Include hidden files and folders, except ignored folders.
            max_depth: Maximum folder depth to render below the root. ``None``
                renders the full tree.
        """
        self.ignored_folders = set(ignored_folders or DEFAULT_IGNORED_FOLDERS)
        self.include_files = include_files
        self.include_hidden = include_hidden
        self.max_depth = max_depth

    def generate_folder_structure_md(
        self,
        current_directory: Optional[Union[str, Path]] = None,
        indentation: str = "",
    ) -> str:
        """
        Generate a Markdown tree for a directory.

        ``indentation`` is kept for compatibility with earlier releases. New
        code should leave it unset.
        """
        root = Path(current_directory or Path.cwd()).expanduser().resolve()
        lines = [f"{indentation}{root.name}/"]
        lines.extend(self._render_children(root, root, indentation, depth=0))
        return "\n".join(lines) + "\n"

    def generate(self, path: Optional[Union[str, Path]] = None) -> str:
        """Generate a Markdown tree for ``path`` or the current directory."""
        return self.generate_folder_structure_md(path)

    def _render_children(
        self,
        root: Path,
        directory: Path,
        prefix: str,
        *,
        depth: int,
    ) -> List[str]:
        if self.max_depth is not None and depth >= self.max_depth:
            return []

        entries = [
            entry for entry in directory.iterdir() if self._should_include(root, entry)
        ]
        entries.sort(key=lambda entry: (entry.is_file(), entry.name.lower()))

        lines = []
        for index, entry in enumerate(entries):
            is_last = index == len(entries) - 1
            connector = "`-- " if is_last else "|-- "
            display_name = f"{entry.name}/" if entry.is_dir() else entry.name
            lines.append(f"{prefix}{connector}{display_name}")

            if entry.is_dir():
                child_prefix = f"{prefix}{'    ' if is_last else '|   '}"
                lines.extend(
                    self._render_children(root, entry, child_prefix, depth=depth + 1)
                )

        return lines

    def _should_include(self, root: Path, entry: Path) -> bool:
        if entry.is_file() and not self.include_files:
            return False

        if not self.include_hidden and entry.name.startswith("."):
            return False

        if entry.is_dir() and self._is_ignored(root, entry):
            return False

        return True

    def _is_ignored(self, root: Path, path: Path) -> bool:
        try:
            relative_path = path.relative_to(root).as_posix()
        except ValueError:
            relative_path = path.as_posix()

        return path.name in self.ignored_folders or relative_path in self.ignored_folders
