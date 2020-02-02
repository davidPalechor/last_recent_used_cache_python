
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='lru_cache',
    version='0.1.0',
    description='Distributed LRU Cache',
    long_description=readme,
    author='Sergio Palechor',
    author_email='sergiopalechor@hotmail.com',
    install_requires=['kafka-python==1.4.7'],
    python_requires='>=3.7.0',
    url='https://github.com/davidPalechor/sergio_palechor_test/tree/master/lru_cache',
    license=license,
    packages=find_packages(exclude=('tests',))
)
