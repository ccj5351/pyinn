#!/usr/bin/env python
import os
import shutil
import sys
from setuptools import setup, find_packages

VERSION = '0.0.1'

long_description = "Manually fused PyTorch NN ops"

setup_info = dict(
    # Metadata
    name='pyinn',
    version=VERSION,
    author='Sergey Zagoruyko',
    author_email='sergey.zagoruyko@enpc.fr',
    url='https://github.com/szagoruyko/pyinn',
    description='Manually fused PyTorch NN ops',
    long_description=long_description,
    license='BSD',

    # Package info
    packages=find_packages(exclude=('test',)),

    zip_safe=True,

    install_requires=[
        'torch',
        'cupy',
        # 'scikit-cuda',
    ]
)

#added by CCJ:
""" 
> see: http://cerfacs.fr/coop/python3_doc/pip_install/
1) We can see that sampleproject and peppercorn have been installed. The line 
Running setup.py install for sampleproject ... done 
tells us more about the installation mechanism used here: the `pip install` command 
actually run a `python setup.py install` command.

2) We can install the sampleproject library and its dependencies (namely peppercorn) using 
either the python setup.py install or the python setup.py develop:
 - a) The `python setup.py install` command will copy the compiled files in your python virtual environnement folder. 
   This is equivalent to using `pip install .` (as `pip install .` actually runs the `python setup.py install` command!).
 - b) The `python setup.py develop` command will create a symbolic link from the library to your python virtual 
   environnement folder. This allows you to code your library while using it from anywhere on your system.
"""

"""
# >see instruction at : https://github.com/pypa/sampleproject
# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.
"""
setup_info_local = dict(
    # Metadata
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install sampleproject
    #
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    name='pyinn',  # Required
    
    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.1',  # Required

    author="Forked from Sergey Zagoruyko, updated by Changjiang Cai for his own research project", # Optional
    author_email='caicj5351@gmail.com', # Optional 
    
    # This should be a valid link to your project's main homepage.
    url='https://github.com/ccj5351/pyinn', # Optional
    description='Manually fused PyTorch NN ops', # Optional
    long_description= "Manually fused PyTorch NN ops", # # Optional
    license='BSD',

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    # e.g.,:
    # package_dir={'': 'src'},  # Optional
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(where='src', exclude=('test',)),  # Required
    
    # Package info
    #packages=find_packages(exclude=('test',)),

    zip_safe=True,

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'torch',
        'cupy',
        # 'scikit-cuda',
    ]
)

setup(**setup_info_local)
