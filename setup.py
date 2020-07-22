#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0',
                'beautifulsoup4>=4.9.1',
                'requests>=2.24.0',
                'termcolor>=1.1.0']

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Allen Shaw",
    author_email='lonsty@sina.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="ZCool picture crawler. Download ZCool (https://www.zcool.com.cn/) "
                "Designer's or User's pictures, photos and illustrations.",
    entry_points={
        'console_scripts': [
            'zcooldl=zcooldl.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords=['zcooldl', 'zcool', 'picture', 'download', 'downloader'],
    name='zcooldl',
    packages=find_packages(include=['zcooldl', 'zcooldl.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/lonsty/zcooldl',
    version='0.1.3',
    zip_safe=False,
)
