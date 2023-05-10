from setuptools import find_packages,setup
from typing import List


HYPHE_E_DOT= "-e ."

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPHE_E_DOT in requirements:
            requirements.remove(HYPHE_E_DOT)
      
    return requirements

get_requirements("D:\\Gemstone_project\\requirements.txt")    

setup( name= "gemstone_project",
      version="0.0.1",
      author="anisha",
      author_email="anisha1207@gmail.com",
      install_requires= get_requirements('requirements.txt'),
      packages=find_packages()
     )  

      
      
      