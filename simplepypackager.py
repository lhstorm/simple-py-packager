import os
import shutil

class PackagePreparer:
    def __init__(self, package_name):
        self.package_name = package_name

    def prepare(self):
        # Create the source and wheel distributions
        os.system(f'python {self.package_name}/setup.py sdist bdist_wheel')

        # Create a README.md file if it doesn't exist
        if not os.path.exists(f'{self.package_name}/README.md'):
            open(f'{self.package_name}/README.md', 'w').close()

        # Create a LICENSE file if it doesn't exist
        if not os.path.exists(f'{self.package_name}/LICENSE'):
            open(f'{self.package_name}/LICENSE', 'w').close()

        # Create a CHANGELOG.md file if it doesn't exist
        if not os.path.exists(f'{self.package_name}/CHANGELOG.md'):
            open(f'{self.package_name}/CHANGELOG.md', 'w').close()

        # Create a .gitignore file if it doesn't exist
        if not os.path.exists(f'{self.package_name}/.gitignore'):
            with open(f'{self.package_name}/.gitignore', 'w') as f:
                f.write('__pycache__\n')
                f.write('dist\n')
                f.write('build\n')
                f.write('*.egg-info\n')

        # Create a requirements.txt file if it doesn't exist
        if not os.path.exists(f'{self.package_name}/requirements.txt'):
            open(f'{self.package_name}/requirements.txt', 'w').close()

        # Move the distributions to the package root
        if not os.path.exists(f'{self.package_name}/dist'):
            os.mkdir(f'{self.package_name}/dist')
        for file in os.listdir(f'{self.package_name}/dist'):
            shutil.move(f'{self.package_name}/dist/{file}', f'{self.package_name}/{file}')

        print(f'Successfully prepared {self.package_name} for distribution')
        
class PackageCreator:
    def __init__(self, package_name):
        self.package_name = package_name

    def create(self):
        # Create package directory
        os.mkdir(self.package_name)

        # Create src directory
        os.mkdir(f'{self.package_name}/src')

        # Create __init__.py file
        open(f'{self.package_name}/__init__.py', 'w').close()

        # Create setup.py file
        with open(f'{self.package_name}/setup.py', 'w') as f:
            f.write(f'''from setuptools import setup, find_packages

setup(
    name="{self.package_name}",
    version="0.1",
    packages=find_packages(),
)''')

        # Create README.md file
        with open(f'{self.package_name}/README.md', 'w') as f:
            f.write(f'# {self.package_name}\n')

        # Create LICENSE file
        with open(f'{self.package_name}/LICENSE', 'w') as f:
            f.write('MIT License')

        # Create .gitignore file
        with open(f'{self.package_name}/.gitignore', 'w') as f:
            f.write('__pycache__\n')
            f.write('dist\n')
            f.write('build\n')
            f.write('*.egg-info\n')

        print(f'Successfully created {self.package_name} package')

