import os


class FolderStructureGenerator:
    """This class generates the markdown representation of the current folder structure."""

    def __init__(self, ignored_folders=None):
        """Initializes the FolderStructureGenerator class.
        :param ignored_folders: List of folders to ignore during folder structure generation."""

        if ignored_folders is None:
            ignored_folders = [
                "__pycache__",
                ".git",
                ".idea",
                "venv",
                "node_modules",
                "build",
                "dist",
                "env",
            ]
        self.ignored_folders = ignored_folders

    def generate_folder_structure_md(self, indentation=""):
        """
        Generates the markdown representation of the current folder structure.

        :param indentation: Indentation string for representing folder hierarchy.
        :return: Markdown string representing the folder structure.
        """
        current_directory = os.getcwd()
        markdown = indentation + os.path.basename(current_directory) + "/\n"
        entries = os.scandir(current_directory)

        for entry in entries:
            if entry.name not in self.ignored_folders:
                if entry.is_dir():
                    markdown += self.generate_folder_structure_md(
                        entry.path, indentation + "├── "
                    )
                else:
                    markdown += indentation + "├── " + entry.name + "\n"

        return markdown
