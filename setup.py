from setuptools import find_packages, setup
from typing import List


def get_requirements() ->List[str]:
    '''
    This function will return the list of requirements
    '''

    requirement_list:List[str] = []

    try:
        with open('requirements.txt','r') as file:
            #Read the lines from the file
            lines = file.readlines()

            #We will process each line
            for line in lines:
                requirement = line.strip()
                #ignore the empty line and -e .

                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file is not found')
    
    return requirement_list

setup(
    name="Network Security",
    version="0.0.1",
    author="Shubham Gangwar",
    author_email="gangwarshubham490@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()    
)

