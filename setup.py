from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyemvue',
    version='0.7.2',
    packages=find_packages(exclude=['tools*', 'simulator*']),
    license='MIT',
    description='EmporiaEnergy vue API Wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['requests', 'typing_extensions', 'setuptools'],
    url='https://github.com/magico13/PyEmVue',
    author='Mike Marvin',
    author_email='magico1313@gmail.com'
)
