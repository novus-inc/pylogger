from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()

# See pyproject.toml for checking dependencies
setup(
    name="pylogger",
    version="0.0.1",
    description="A logger for Python projects.",
    long_description=readme,
    url="https://github.com/novus-inc/pylogger",
    packages=find_packages(exclude=("tests", "docs")),
)
