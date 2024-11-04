import os


class FolderStructureGenerator:
    """Generates the markdown representation of the current folder structure."""

    def __init__(self, ignored_folders=None):
        """
        Initializes the FolderStructureGenerator.

        :param ignored_folders: List of folders (with relative paths) to ignore during folder structure generation.
        """
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
        self.ignored_folders = [
            os.path.join(os.getcwd(), folder) for folder in ignored_folders
        ]

    def generate_folder_structure_md(
        self, current_directory=os.getcwd(), indentation=""
    ):
        """
        Generates the markdown representation of the current folder structure.

        :param current_directory: Current directory to generate the folder structure from.
        :param indentation: Indentation string for representing folder hierarchy.
        :return: Markdown string representing the folder structure.
        """

        markdown = indentation + os.path.basename(current_directory) + "/\n"
        entries = os.scandir(current_directory)

        for entry in entries:
            entry_path = entry.path  # Get the full path of the entry

            if entry.is_dir():
                # Skip the folder's contents if its path is in ignored_folders
                if entry_path in self.ignored_folders:
                    markdown += indentation + "├── " + entry.name + "\n"
                else:
                    markdown += self.generate_folder_structure_md(
                        entry_path, indentation + "├── "
                    )
            elif entry.is_file():
                markdown += indentation + "├── " + entry.name + "\n"

        return markdown
