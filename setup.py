#!/usr/bin/env python

from setuptools import setup
import cinergia
package_classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering',
    ]
setup(
    name='cinergia',
    version=cinergia.__version__,
    description='Library for communication with cinergia electronic loads',
    author=cinergia.__author__,
    author_email='boudinpg@gmail.com',
    url='http://github.com/cedricboudinet/python-cinergia',
    packages=['cinergia'],
    license="LGPL-3.0",
    test_suite='tests',
    classifiers=package_classifiers,
    install_requires=['pymodbus'],
    )
