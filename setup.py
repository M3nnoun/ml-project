## will be responsable to create my ML project as a package
from setuptools import setup, find_packages

def get_requirements(file_path):
    """
    This function will return a list of requirements from the given file path.
    """
    with open(file_path, 'r') as file:
        requirements= file.readlines()[:-1]
        requirements =[req.strip() for req in requirements if req.strip() and not req.startswith('#')]
    return requirements

setup(
    name='ml_project',
    version='0.1',
    author='M3nnoun',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)

