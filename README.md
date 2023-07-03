# Folder Structure Generator
Folder Structure Generator is a Python package that simplifies the generation of project directory structures. It provides an easy way to create a predefined directory tree that can be copied and pasted into project documentation or README files.

# Installation
You can install Folder Structure Generator using pip:
```
pip install folder-structure-generator
```

# Usage
To generate a project directory structure, simply run the following command:
```
from folder_structure import FolderStructureGenerator

# List of folders to be ignored in the folder structure generation
folders_to_ignore = [
    "__pycache__",
    ".git",
    ".idea",
    "venv",
]

# Generate the markdown representation of the folder structure
folder_structure_generator = FolderStructureGenerator(ignored_folders=folders_to_ignore)
folder_structure_md = folder_structure_generator.generate_folder_structure_md()

# Print the markdown representation of the folder structure
print(folder_structure_md)
```
This will generate a predefined directory tree in the current working directory. You can then copy and paste the generated structure into your project documentation or README file.

## Expected Output
```
folder-structure-generator/
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.py
├── .gitignore
├── folder_structure/
├── ├── __init__.py
├── ├── folder_structure_generator.py
```

# Features
- Automated generation of project directory structures
- Saves time and effort when setting up new projects
- Ensures consistency across projects
- User-friendly interface for easy usage
- Enhances project organization and collaboration

# Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue on the [GitHub repository](https://github.com/ujjawalpoudel/project-tree). We appreciate your feedback.
