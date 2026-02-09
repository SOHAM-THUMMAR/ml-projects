from setuptools import find_packages,setup
from typing import List


hyphen_e_dot = "-e ."

def getRequires(filePath)-> List[str]:
  '''
  this function will return the list of requirements
  '''
  requirements = []

  with open(filePath) as file_obj:
    requirements = file_obj.readlines()
    requirements = [req.replace("\n","") for req in requirements]

    if hyphen_e_dot in requirements:
      requirements.remove(hyphen_e_dot)

  return requirements


setup(
  name='mlproject',
  version='0.0.1',
  author="SOHAM-THUMMAR",
  author_email="sohamthummar04@gmail.com",
  packages=find_packages(),
  install_requires=getRequires('requirements.txt')
)