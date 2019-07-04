#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import setuptools

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ['Click>=6.0', "rpy2"]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest']

setuptools.setup(
    author="Martin Skarzynski",
    author_email='marskar@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Construct, deconstruct, and convert R markdown files.",
    entry_points={
        'console_scripts': [
            'rmdusk=cli.rmdusk_cli:rmdusk_cli',
            'rmdawn=cli.rmdawn_cli:rmdawn_cli',
            'rmdtor=cli.rmdtor_cli:rmdtor_cli',
            'rtormd=cli.rtormd_cli:rtormd_cli',
            'render=cli.render_cli:render_cli',
            'catren=cli.catren_cli:catren_cli',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='rmdawn',
    name='rmdawn',
    package_dir={"": "src"},
    packages=setuptools.find_packages('src'),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/marskar/rmdawn',
    version='0.1.2',
    zip_safe=False,
)
