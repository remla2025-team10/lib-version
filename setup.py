from setuptools import setup, find_packages
import os
import re   

# Read instead of import to avoid racing conditions
def read_version():
    with open(os.path.join("lib-version", "VERSION"), "r") as file:
        return file.read().strip()