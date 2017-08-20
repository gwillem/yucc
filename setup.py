from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from yucc import __version__

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name = 'yucc',
    version = __version__,
    description = 'CLI for UpCloud public cloud service',
    long_description = long_description,
    url = 'TODO',
    author = 'Erik Sørensen',
    author_email = 'erik@enssoftware.no',
    license = 'MIT',
    classifiers = [
    ],
    keywords = 'cli upcloud',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['upcloud-api', 'colorama'],
    extras_require = {},
    entry_points = {
        'console_scripts': [
            'yucc-cli=yucc.cli:main',
        ],
    }
)
