from setuptools import setup
import os

# Read instead of import to avoid racing conditions
def read_version():
    with open(os.path.join("src", "lib_version", "VERSION"), "r") as file:
        return file.read().strip()

setup(
    version=read_version()
)