import setuptools


with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()


__version__='0.0.0'
    
REPO_NAME = "Kidney"

AUTHOR_USER_NAME="mlraviteja"

SRC_REPO = "cnnclassifier"

AUTHOR_EMAIL="lakshmi.ravi3003@gmail.com"


setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL ,
    description= "A small python package for cnn app",
    Long_description = long_description,
    Long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls ={"Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    Package_dir = {"":"src"},
    package=setuptools.find_packages(where='src')
    
)