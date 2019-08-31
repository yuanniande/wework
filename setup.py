import os
from setuptools import setup, find_packages


def read(*rnames):
    file_path = os.path.join(os.path.dirname(__file__), *rnames)
    return open(file_path).read()


setup(
    name="wework",
    version="0.1.3",
    packages=find_packages(),
    install_requires=[
        'requests>=2.12.4',
        'pycrypto>=2.6'
    ],
    description="Official lib of wework.",
    long_description=read('README.md'),
    url='https://github.com/iamsk/wework'
)
