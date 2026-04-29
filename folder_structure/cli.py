from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional, Sequence

from .folder_structure_generator import DEFAULT_IGNORED_FOLDERS, FolderStructureGenerator


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="folder-structure",
        description="Generate a Markdown-friendly tree for a project directory.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Directory to scan. Defaults to the current directory.",
    )
    parser.add_argument(
        "-i",
        "--ignore",
        action="append",
        default=[],
        metavar="NAME",
        help="Folder name or relative path to ignore. Can be used multiple times.",
    )
    parser.add_argument(
        "--no-default-ignore",
        action="store_true",
        help="Do not apply the built-in ignore list.",
    )
    parser.add_argument(
        "--directories-only",
        action="store_true",
        help="Show directories only.",
    )
    parser.add_argument(
        "--exclude-hidden",
        action="store_true",
        help="Hide dotfiles and hidden directories.",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        metavar="N",
        help="Maximum folder depth to render below the root.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Write the generated tree to a file instead of stdout.",
    )
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    ignored_folders = [] if args.no_default_ignore else list(DEFAULT_IGNORED_FOLDERS)
    ignored_folders.extend(args.ignore)

    generator = FolderStructureGenerator(
        ignored_folders=ignored_folders,
        include_files=not args.directories_only,
        include_hidden=not args.exclude_hidden,
        max_depth=args.max_depth,
    )
    tree = generator.generate(args.path)

    if args.output:
        args.output.write_text(tree, encoding="utf-8")
    else:
        print(tree, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
