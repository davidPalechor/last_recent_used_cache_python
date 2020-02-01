
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='greater_version_validation',
    version='0.1.0',
    description='Returns the latest version between two entries',
    long_description=readme,
    author='Sergio Palechor',
    author_email='sergiopalechor@hotmail.com',
    url='https://github.com/davidPalechor/sergio_palechor_test/tree/master/greater_version_validation',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)