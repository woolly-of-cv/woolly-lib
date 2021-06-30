from setuptools import setup, find_packages
import os

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="woolly-lib",
    version="0.0.1",
    description="This Library for pytorch based utilities which will be used for training and visualizing cv models",
    long_description=open("README.txt").read() + "\n\n" + open("CHANGELOG.txt").read(),
    url="",
    author="Team_woolly",
    author_email="srikanthakandarp23@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords="ML",
    packages=find_packages(),
    install_requires=required,
)