from setuptools import find_packages,setup
from typing import List

Hypen_E_DOT='-e .'
def get_requirments(file_path:str)->List[str]:

    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        [req.replace("\n","") for req in requirments]
    
        if Hypen_E_DOT in requirments:
            requirments.remove(Hypen_E_DOT)
    return requirments
setup(
name='mlproject',
version='0.0.1',
author='krish',
author_mail='rohananvekar30@gmail.com',
packages=find_packages(),
install_requires=get_requirments('requirements.txt')

)