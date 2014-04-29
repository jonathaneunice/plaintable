from setuptools import setup
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))

# Read the version number from a source file.
# Why read it, and not import?
# see https://groups.google.com/d/topic/pypa-dev/0PkjVpcxTzQ/discussion
def find_version(*file_paths):
    with open(os.path.join(here, *file_paths), 'r') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


# Get the long description from the relevant file
with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='plaintable',
    version=find_version('plaintable.py'),
    description='a simple library to build plain text tables',
    long_description=long_description,
    url='https://github.com/rumpelsepp/plaintable',
    author='Stefan Tatschner',
    author_email='stefan@sevenbyte.org',
    license='MIT',
    py_modules = ['plaintable'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='table development')

