''' It is used to define the configuration of your project ,
 such as its dependencies, metadata, and other settings.'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    ''' This function will return the list of requirements '''
    requirement_lst: List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines= file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("The requirements.txt file is not found.")
    
    return requirement_lst

# print(get_requirements()) 
setup(
    name='network_security_project',
    version='0.0.1',
    author='Starkk',
    packages=find_packages(),
    install_requires=get_requirements(),
)