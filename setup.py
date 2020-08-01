# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='dice',
    version='0.1.0',
    description='App to roll dice.',
    long_description=readme,
    author='Ian Hayfield',
    author_email='irhayf@gmail.com',
    url='https://github.com/IRHayfield/dice.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)