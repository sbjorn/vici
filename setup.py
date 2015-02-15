import codecs

from setuptools import setup

import vici


with codecs.open("README.rst", "r", "UTF-8") as readme:
    long_description = readme.read()

setup(
    name="vici",
    version=vici.__version__,
    description="Library talking vici to strongSwan",
    author="Bjorn Schuberg",
    url="https://github.com/sbjorn/vici",
    license="MIT",
    long_description=long_description,
    packages=["vici"],
    include_package_data=True,
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries",
    )
)
