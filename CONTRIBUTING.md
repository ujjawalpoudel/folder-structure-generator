# Contributing

Thanks for helping improve Folder Structure Generator.

## Local Setup

```bash
git clone https://github.com/ujjawalpoudel/folder-structure-generator.git
cd folder-structure-generator
python3 -m pip install -e .
```

## Before Opening a Pull Request

Run the tests:

```bash
python3 -m unittest discover -s tests
```

Check the command-line interface:

```bash
python3 -m folder_structure.cli --help
```

## Good First Contributions

- Add more output styles, such as Unicode tree characters or JSON.
- Add richer ignore matching, such as glob patterns.
- Improve examples for common Python, Node.js, and documentation projects.
- Add tests for edge cases on Windows, macOS, and Linux paths.

## Release Checklist

1. Update the version in `pyproject.toml` and `folder_structure/__init__.py`.
2. Update `CHANGELOG.md`.
3. Run `python3 -m unittest discover -s tests`.
4. Build with `python3 -m build`.
5. Publish with `python3 -m twine upload dist/*`.
