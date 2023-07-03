from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'The "Project Tree" is designed to simplify generating project directory structures. '
LONG_DESCRIPTION = '"Project Tree" simplifies the generation of project directory structures. Easily create a predefined directory tree, copy it to project documentation or README files, and save time when setting up new projects. Eliminate manual directory creation, ensure consistency across projects, and enhance project organization..'

# Setting up
setup(
    name="project-tree",
    version=VERSION,
    author="Ujjawal Poudel",
    author_email="ujjawalpoudel@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=["python",'documentation', "structure"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)