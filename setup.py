from setuptools import find_packages
from typing import List
from setuptools import setup

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="Fault detection",
    version="0.0.1",
    author="Adarsh Kumar Bhardwaj",
    author_email="adarsh20221217@gmail.com",
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt')
)