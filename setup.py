from io import open

from setuptools import find_packages, setup

REQUIRES = []

setup(
    name='package_demo',
    version='0.0.1',
    description='',
    author='Lee Sutton',
    author_email='leesutton1@gmail.com',
    maintainer='Lee Sutton',
    maintainer_email='leesutton1@gmail.com',
    url='https://github.com/lee-sutton/package_demo',
    license='MIT/Apache-2.0',
    entry_points={'console_scripts': ['command = package_demo.cli:main']},
    keywords=[
        '',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    install_requires=REQUIRES,
    tests_require=['coverage', 'pytest'],

    packages=find_packages(),
)
