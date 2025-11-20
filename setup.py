'''
setup.py is an essential part of packaging and distributing python projects .
its is used by setuptools to define configurations like meta data , dependencies
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    this func will return list for requiremnets
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt' , 'r') as file:
            # Read lines from the file
            lines = file.readlines()

            # process each line
            for line in lines:
                requirement = line.strip()

                ## ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt not found")

    return requirement_lst


setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Shubham kumar",
    author_email="kr95.shubham447@gmail.com",
    packages= find_packages(),
    install_requires=get_requirements()

)


