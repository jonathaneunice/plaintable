import plaintable
from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='plaintable',
    version=plaintable.__version__,
    description='A simple library to build plain text tables',
    long_description=long_description,
    url='https://github.com/rumpelsepp/plaintable',
    author='Stefan Tatschner',
    author_email='stefan@sevenbyte.org',
    license=plaintable.__license__,
    py_modules=['plaintable'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='table development')
