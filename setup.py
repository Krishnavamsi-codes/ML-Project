from setuptools import find_packages,setup
from typing import List
hyphen_e_dot='-e.'
## file_path is a string a list needs to be returned so write like that
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()## also reads the \n character so remove it and also the -e .
        requirements=[req.replace("\n","")for req in requirements ]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements

setup(name='ML_Project',
version='0.0.1',
author='Krishnavamsi',
author_email='vamsi9398672280@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'))

