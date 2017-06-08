from setuptools import setup, find_packages

setup(
    name="pandas_diff",
    version="0.0.1",
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
    license="GPL"
)
