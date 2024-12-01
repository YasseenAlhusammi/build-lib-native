from setuptools import setup, find_packages

setup(
    name='pyzbar',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'firebase-admin',
        'pyzbar',
    ],
    python_requires='>=3.6',
)
