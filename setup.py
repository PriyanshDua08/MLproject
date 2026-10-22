from setuptools import find_packages, setup

E_DOT = '-e .'
def get_requirements(file_path):
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if E_DOT in requirements:
                requirements.remove(E_DOT) 
    return requirements

    

setup(
    name="mlproject",
    version="0.0.1",
    author="Priyansh"
    , author_email="priyanshdua08@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)