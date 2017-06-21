#!/usr/bin/env python3

from setuptools import setup, find_packages
from pathlib import Path
try:
    from sphinx.setup_command import BuildDoc
except ImportError:
    BuildDoc = None

name = "pandas_diff"
version = "0.1"
release = "0.1.0"
here = Path(__file__).parent.resolve()

setup(
    name=name,
    version=version,
    packages=find_packages(),
    test_suite="test",
    entry_points={
        'console_scripts': [
            'pdiff = pandas_diff.scripts:main',
        ],
    },

    install_requires=[
        'pandas',
        'oset'
    ],
    dependency_links=['http://github.com/TMiguelT/sphinxcontrib-restbuilder/tarball/master#egg=sphinxcontrib-restbuilder'],
    license="GPL",
    cmdclass={
        'build_readme': BuildDoc,
        'build_html': BuildDoc
    },
    command_options={
        'build_readme': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'source_dir': ('setup.py', 'docs/source'),
            'build_dir': ('setup.py', str(here)),
            'builder': ('setup.py', 'rst')
        },
        'build_html': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'source_dir': ('setup.py', 'docs/source'),
            'build_dir': ('setup.py', '.'),
            'builder': ('setup.py', 'html')
        }
    },
)
