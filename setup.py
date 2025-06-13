
'''
The  setup.py file is an essential part of packaging
 and distributing python projects. it is used 
 by setuptools(or distutils in older python 
 versions) to define the configuration of your 
 project, such as its metadata,depndencies, and entry points
 '''

from setuptools import find_packages, setup
from typing import list 

def get_requirements(file_path:str)->list[str]:
    