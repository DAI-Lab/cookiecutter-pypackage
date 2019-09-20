#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [
    {%- if cookiecutter.command_line_interface|lower == 'click' %}'Click>=6.0',{%- endif %}
    {%- if cookiecutter.support_py2 == 'y' %}'six',{%- endif %}
]

setup_requirements = [
    'pytest-runner>=2.11.1',
]

test_requirements = [
    'coverage>=4.5.1',
    'pytest>=3.4.2',
    'tox>=2.9.1',
]

development_requirements = [
    # general
    'bumpversion>=0.5.3',
    'pip>=9.0.1',
    'watchdog>=0.8.3',

    # docs
    'm2r>=0.2.0',
    'Sphinx>=1.7.1',
    'sphinx_rtd_theme>=0.2.4',

    # style check
    'flake8>=3.5.0',
    'isort>=4.3.4',

    # fix style issues
    'autoflake>=1.1',
    'autopep8>=1.3.5',

    # distribute on PyPI
    'twine>=1.10.0',
    'wheel>=0.30.0',
]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    author='{{ cookiecutter.license_owner }}',
    author_email='{{ cookiecutter.license_owner_email }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
{%- if cookiecutter.support_py2 == 'y' %}
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
{%- endif %}
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description='{{ cookiecutter.project_short_description.replace("\'", "\\\'") }}',
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.package_name }}={{ cookiecutter.project_slug }}.cli:main',
        ],
    },
    {%- endif %}
    extras_require={
        'test': test_requirements,
        'dev': development_requirements + test_requirements,
    },
    install_package_data=True,
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license='{{ cookiecutter.open_source_license }}',
{%- endif %}
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }} {{ cookiecutter.package_name }} {{ cookiecutter.project_name }}',
    name='{{ cookiecutter.package_name }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}.*']),
{%- if cookiecutter.support_py2 == 'y' %}
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
{%- else %}
    python_requires='>=3.4',
{%- endif %}
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.repository_name }}',
    version='{{ cookiecutter.version }}',
    zip_safe=False,
)
