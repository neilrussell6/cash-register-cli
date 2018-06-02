from setuptools import setup

setup(
    name='cash-register',
    version='0.1',
    py_modules=['src'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        cash-register=src.cli:cli
    ''',
)
