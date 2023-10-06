
from setuptools import find_packages, setup

setup(
    name="cilia_tracker",
    version="0.1.0",
    install_requires=[],
    packages=find_packages(exclude="notebooks"),
    extras_require={
        "all": ["matplotlib", "opencv-python"],
        "dev": ["flake8", "black"],
    },
)
