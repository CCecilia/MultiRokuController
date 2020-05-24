# type: ignore
import pathlib

from setuptools import setup

# The directory containing this file
CWD = pathlib.Path(__file__).parent

# The text of the README file
README = (CWD / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="multi-roku-controller",
    version="1.0.0",
    description="Controller for multiple Rokus",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/CCecilia/MultiRokuController",
    author="Christian Cecilia",
    author_email="christian.cecilia1@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["multi-roku"],
    include_package_data=True,
    install_requires=[
        "roku-scanner"
    ],
    entry_points={
        "console_scripts": [
            "multi_roku=multi_roku.__main__:main",
        ]
    },
)