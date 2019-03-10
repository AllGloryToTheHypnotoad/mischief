##############################################
# The MIT License (MIT)
# Copyright (c) 2019 Kevin Walchko
# see LICENSE for full details
##############################################

from __future__ import print_function
from setuptools import setup

from build_utils import BuildCommand
from build_utils import PublishCommand
from build_utils import BinaryDistribution
from build_utils import SetGitTag
from build_utils import get_pkg_version

VERSION = get_pkg_version('mischief/__init__.py')
PACKAGE_NAME = 'mischief'
BuildCommand.pkg = PACKAGE_NAME
BuildCommand.py2 = False
BuildCommand.test = False
PublishCommand.pkg = PACKAGE_NAME
PublishCommand.version = VERSION
SetGitTag.version = VERSION


setup(
    author='Kevin Walchko',
    author_email='walchko@users.noreply.github.com',
    name=PACKAGE_NAME,
    version=VERSION,
    description='Another interface to haveibeenpawned.com',
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/AllGloryToTheHypnotoad/{}'.format(PACKAGE_NAME),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ],
    license='MIT',
    keywords=['hibp', 'pwn', 'pwned', 'haveibeenpwned'],
    packages=[PACKAGE_NAME],
    install_requires=[
        'build_utils',
        'requests',
        'colorama'
    ],
    cmdclass={
        'publish': PublishCommand,
        'make': BuildCommand,
        'git': SetGitTag
    },
    scripts=[
        'bin/pymischief.py',
    ]
)
