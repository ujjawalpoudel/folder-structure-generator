import tempfile
import unittest
from pathlib import Path

from folder_structure import FolderStructureGenerator


class FolderStructureGeneratorTest(unittest.TestCase):
    def test_generates_sorted_markdown_tree(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "src").mkdir()
            (root / "src" / "app.py").write_text("print('hello')\n", encoding="utf-8")
            (root / "README.md").write_text("# Demo\n", encoding="utf-8")
            (root / "dist").mkdir()
            (root / "dist" / "package.whl").write_text("", encoding="utf-8")

            generator = FolderStructureGenerator()

            self.assertEqual(
                generator.generate(root),
                f"{root.name}/\n"
                "|-- src/\n"
                "|   `-- app.py\n"
                "`-- README.md\n",
            )

    def test_can_render_directories_only(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs" / "index.md").write_text("# Docs\n", encoding="utf-8")
            (root / "README.md").write_text("# Demo\n", encoding="utf-8")

            generator = FolderStructureGenerator(include_files=False)

            self.assertEqual(generator.generate(root), f"{root.name}/\n`-- docs/\n")

    def test_can_limit_depth(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "src").mkdir()
            (root / "src" / "package").mkdir()
            (root / "src" / "package" / "module.py").write_text("", encoding="utf-8")

            generator = FolderStructureGenerator(max_depth=1)

            self.assertEqual(generator.generate(root), f"{root.name}/\n`-- src/\n")

    def test_can_ignore_relative_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "src").mkdir()
            (root / "src" / "generated").mkdir()
            (root / "src" / "generated" / "api.py").write_text("", encoding="utf-8")
            (root / "src" / "main.py").write_text("", encoding="utf-8")

            generator = FolderStructureGenerator(ignored_folders=["src/generated"])

            self.assertEqual(
                generator.generate(root),
                f"{root.name}/\n"
                "`-- src/\n"
                "    `-- main.py\n",
            )


if __name__ == "__main__":
    unittest.main()
