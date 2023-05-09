from setuptools import find_packages, setup
from typing import List

HYPEN_DOT_E= "-e ."
# -e . acts as a link between setup file and requirements.txt 
# read the requirements file after opening it 
def get_requirements(file_path:str)->List[str]:
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #as every line with have \n embedded, we replace it
        requirements=[req.replace("\n","")   for req in requirements]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)

    return requirements

setup( 
    name = "houseprice_project",
    version= "0.0.1",
    author ="anisha-dsgit",
    author_email="anisha1207@gmail.com", 
    install_requires=get_requirements("requirements.txt"),
    packages= find_packages()
    )

