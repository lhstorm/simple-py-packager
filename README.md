# Package Creator and Preparer

This repo contains a script that automates the process of creating and preparing a Python package for distribution. This script was created in 3 minutes with the help of ChatGPT.

## Usage

The script contains two classes: `PackageCreator` and `PackagePreparer`. 

### PackageCreator

The `PackageCreator` class can be used to create the basic structure of a Python package. It creates the package directory, the `src` directory, the `__init__.py` file, the `setup.py` file, the `README.md` file, the `LICENSE` file, and the `.gitignore` file.

You can use the class by creating an instance of it and calling the `create` method.

```python
from package_creator import PackageCreator

creator = PackageCreator('mypackage')
creator.create()
```

### PackagePreparer
The PackagePreparer class can be used to prepare a Python package for distribution. It creates source and wheel distributions, creates the necessary files (README.md, LICENSE, CHANGELOG.md, .gitignore, requirements.txt) if they don't exist, and moves the distributions to the package root.

You can use the class by creating an instance of it and calling the prepare method, passing in the package name as an argument.

```python
from package_preparer import PackagePreparer

preparer = PackagePreparer()
preparer.prepare('mypackage')
```

##Dependencies

The script requires the setuptools library to be installed.

##Note

Make sure that the package name passed to the class is a valid package name, and that you have the setup.py file in the package root directory.
The PackagePreparer class also assumes that you have the required dependencies installed, such as twine to upload the package to PyPI.
Contributions

Feel free to contribute to this project by submitting pull requests or reporting issues.
Please make sure that you have created an account on PyPI, and also that your package name is unique, and it's not already taken by someone else.

## Release Notes: 

202301 - First Release 
