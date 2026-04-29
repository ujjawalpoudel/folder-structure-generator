# Folder Structure Generator

Generate clean Markdown folder trees for project documentation, README files, onboarding notes, and issue reports.

```text
my-project/
|-- docs/
|   `-- index.md
|-- src/
|   `-- app.py
`-- README.md
```

## Why use it?

- Simple Python API for generating project trees.
- Command-line interface for quick copy-and-paste output.
- Deterministic, sorted output for cleaner documentation diffs.
- Built-in ignores for common noise like `.git`, `__pycache__`, `venv`, `dist`, and `node_modules`.
- No runtime dependencies.

## Installation

```bash
pip install folder-structure-generator
```

For local development:

```bash
git clone https://github.com/ujjawalpoudel/folder-structure-generator.git
cd folder-structure-generator
python3 -m pip install -e .
```

## Command-Line Usage

Generate a tree for the current directory:

```bash
folder-structure
```

Generate a tree for a specific project:

```bash
folder-structure path/to/project
```

Write the output to a file:

```bash
folder-structure path/to/project --output STRUCTURE.md
```

Useful options:

```bash
folder-structure --directories-only
folder-structure --exclude-hidden
folder-structure --max-depth 2
folder-structure --ignore migrations --ignore generated
folder-structure --no-default-ignore
```

The package also exposes `folder-structure-generator` as an alias command.

## Python Usage

```python
from folder_structure import FolderStructureGenerator

generator = FolderStructureGenerator(
    ignored_folders=[".git", "__pycache__", "node_modules"],
    max_depth=3,
)

tree = generator.generate("path/to/project")
print(tree)
```

You can also keep using the original method name:

```python
tree = generator.generate_folder_structure_md("path/to/project")
```

## API

### `FolderStructureGenerator(...)`

Options:

- `ignored_folders`: folder names or relative paths to exclude.
- `include_files`: include files in the generated tree. Defaults to `True`.
- `include_hidden`: include dotfiles and hidden directories. Defaults to `True`.
- `max_depth`: maximum folder depth below the root. Defaults to no limit.

### `generate(path=None)`

Returns a Markdown-friendly tree for `path`. If `path` is not provided, it scans the current working directory.

## Development

Run the test suite:

```bash
python3 -m unittest discover -s tests
```

Build the package:

```bash
python3 -m pip install build
python3 -m build
```

## Contributing

Ideas, issues, and pull requests are welcome. Good first improvements include output format options, richer ignore patterns, and documentation examples for common project types.

See [CONTRIBUTING.md](CONTRIBUTING.md) for local setup, test commands, and release notes.

Repository: https://github.com/ujjawalpoudel/folder-structure-generator

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for release history.

## License

Licensed under the Apache License 2.0. See [LICENSE](LICENSE).
