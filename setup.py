from setuptools import setup, find_packages
from typing import List

#HYPEN_E_DOT='-e .' #this is compulsory for -e . means HYPEN_E_DOT

def get_requirements(file_path:str) -> List[str]:
    #this will return a list of requirements
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '')for req in requirements]

        #if HYPEN_E_DOT in requirements:
            #requirements.remove(HYPEN_E_DOT)

    return requirements    

setup(
name = 'mlproject',
version = '1.0.1',
author = 'navanish',
author_email= 'navanish06@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)