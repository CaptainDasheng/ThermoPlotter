#!/usr/bin/env python3

__name__ =       'ThermoPlotter'
__author__ =     'Kieran B. Spooner'
__copyright__ =  'Copyright Kieran B. Spooner (2020)'
__version__ =    '0.3.0'
__maintainer__ = 'Kieran B. Spooner'
__email__ =      'kieran.spooner.14@ucl.ac.uk'
__date__ =       'Dec 4 2020'

import glob
import matplotlib as mpl
import os
import setuptools
from setuptools.command.install import install
from sphinx.setup_command import BuildDoc
import shutil

with open('README.rst', 'r') as f:
    long_description=f.read()

def load_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test*.py')
    return test_suite

def install_style():
    style = 'tp.mplstyle'

    styledir = os.path.join(mpl.get_configdir(), 'stylelib')
    if not os.path.exists(styledir):
        os.makedirs(styledir)

    shutil.copy(os.path.join(os.path.dirname(__file__), style),
                os.path.join(styledir, style))

class PostInstallMoveFile(install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        install_style()

scripts = glob.glob("scripts/tp-*")

setuptools.setup(
    name='ThermoPlotter',
    version='0.3.0',
    author='Kieran B. Spooner',
    description='A simple thermoelectrics plotting tool',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/kbspooner/ThermoPlotter',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Visualization'],
    keywords='chemistry materials thermoelectric dft phonopy phono3py '
             'amset tp matplotlib',
    test_suite='setup.load_test_suite',
    install_requires=['h5py', 'matplotlib', 'numpy', 'pymatgen',
                      'pyyaml', 'scipy', 'sphinx']
    python_requires='>=3',
    cmdclass={'build_sphinx': BuildDoc,
              'install':      PostInstallMoveFile},
    command_options={'build_sphinx':
                        {'project':    ('setup.py', __name__),
                         'version':    ('setup.py', __version__),
                         'source_dir': ('setup.py', 'docs')}},
    scripts=scripts)
