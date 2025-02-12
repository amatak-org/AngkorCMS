# setup.py
from setuptools import setup, find_packages

setup(
    name='angkor',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'angkor = cli:main',
        ],
    },
    install_requires=[
        'Flask==2.3.2',
    ],
)
