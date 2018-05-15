"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='contrary',
    version='0.1',
    description='Ordered data structures from multiple YAML sources',
    long_description=long_description,
    long_description_content_type='text/markdown',
    # Main URL
    url='https://github.com/rbricheno/contrary',
    author='Robert Bricheno',

    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='yaml ordered OrderedDict merge',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # List additional URLs
    project_urls={
        'Bug Reports': 'https://github.com/rbricheno/contrary/issues',
        'Source': 'https://github.com/rbricheno/contrary',
    },
)
