from distutils.core import setup

from setuptools import find_packages

VERSION = '0.1.2'

setup(
    name='spock',
    description='A pure python framework that implements the 1.8 Minecraft '
                'protocol for building Minecraft clients',
    license='MIT',
    long_description=open('README.rst').read(),
    version=VERSION,
    url='https://github.com/SpockBotMC/SpockBot',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
        'cryptography >= 0.9',
        'minecraft_data == 0.3.0',
        'six',
    ],
    keywords=['minecraft'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ]
)
