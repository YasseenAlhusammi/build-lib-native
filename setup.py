from setuptools import setup, find_packages

setup(
    name='my_firebase_admin',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'firebase-admin',
        'zbar',
    ],
    python_requires='>=3.6',
)
