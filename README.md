# Package Creator and Preparer

This repo contains a script that automates the process of creating and preparing a Python package for distribution.

## Usage

The script contains two classes: `PackageCreator` and `PackagePreparer`. 

### PackageCreator

The `PackageCreator` class can be used to create the basic structure of a Python package. It creates the package directory, the `src` directory, the `__init__.py` file, the `setup.py` file, the `README.md` file, the `LICENSE` file, and the `.gitignore` file.

You can use the class by creating an instance of it and calling the `create` method.

```python
from package_creator import PackageCreator

creator = PackageCreator('mypackage')
creator.create()
