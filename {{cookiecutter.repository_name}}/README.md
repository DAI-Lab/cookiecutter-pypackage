<p align="left">
<img width=15% src="https://dai.lids.mit.edu/wp-content/uploads/2018/06/Logo_DAI_highres.png" alt=“DAI-Lab” />
<i>An open source project from Data to AI Lab at MIT.</i>
</p>

[![PyPI Shield](https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.package_name }})
[![Travis CI Shield](https://travis-ci.org/{{ cookiecutter.github_owner }}/{{ cookiecutter.repository_name }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.github_owner }}/{{ cookiecutter.repository_name }})
{%- if cookiecutter.use_codecov == 'y' %}
[![Coverage Status](https://codecov.io/gh/{{ cookiecutter.github_owner }}/{{ cookiecutter.repository_name }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_owner }}/{{ cookiecutter.repository_name }})
{%- endif %}
[![Downloads](https://pepy.tech/badge/{{ cookiecutter.package_name }})](https://pepy.tech/project/{{ cookiecutter.package_name }})

# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if cookiecutter.open_source_license == 'Not open source' -%}
- Free software: {{ cookiecutter.open_source_license }}
{% endif -%}
- Documentation: https://{{ cookiecutter.github_owner }}.github.io/{{ cookiecutter.repository_name }}
- Homepage: https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.repository_name }}

# Overview

TODO: Provide a short overview of the project here.

# Install

## Requirements

**{{ cookiecutter.project_name }}** has been developed and tested on [Python {%- if cookiecutter.support_py2 == 'y' %}2.7, {%- endif %}3.4, 3.5, 3.6 and 3.7](https://www.python.org/downloads/)

Also, although it is not strictly required, the usage of a [virtualenv](https://virtualenv.pypa.io/en/latest/)
is highly recommended in order to avoid interfering with other software installed in the system
where **{{ cookiecutter.project_name }}** is run.

These are the minimum commands needed to create a virtualenv using python3.6 for **{{ cookiecutter.project_name }}**:

```bash
pip install virtualenv
virtualenv -p $(which python3.6) {{ cookiecutter.repository_name }}-venv
```

Afterwards, you have to execute this command to have the virtualenv activated:

```bash
source {{ cookiecutter.repository_name }}-venv/bin/activate
```

Remember about executing it every time you start a new console to work on **{{ cookiecutter.project_name }}**!

## Install with pip

After creating the virtualenv and activating it, we recommend using
[pip](https://pip.pypa.io/en/stable/) in order to install **{{ cookiecutter.project_name }}**:

```bash
pip install {{ cookiecutter.package_name }}
```

This will pull and install the latest stable release from [PyPi](https://pypi.org/).

## Install from source

Alternatively, with your virtualenv activated, you can clone the repository and install it from
source by running `make install` on the `stable` branch:

```bash
git clone git@github.com:{{ cookiecutter.github_owner }}/{{ cookiecutter.repository_name }}.git
cd {{ cookiecutter.repository_name }}
git checkout stable
make install
```

## Install for Development

If you want to contribute to the project, a few more steps are required to make the project ready
for development.

First, please head to [the GitHub page of the project](https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.repository_name }})
and make a fork of the project under you own username by clicking on the **fork** button on the
upper right corner of the page.

Afterwards, clone your fork and create a branch from master with a descriptive name that includes
the number of the issue that you are going to work on:

```bash
git clone git@github.com:{your username}/{{ cookiecutter.repository_name }}.git
cd {{ cookiecutter.repository_name }}
git branch issue-xx-cool-new-feature master
git checkout issue-xx-cool-new-feature
```

Finally, install the project with the following command, which will install some additional
dependencies for code linting and testing.

```bash
make install-develop
```

Make sure to use them regularly while developing by running the commands `make lint` and
`make test`.

# Quickstart

In this short tutorial we will guide you through a series of steps that will help you
getting started with **{{ cookiecutter.project_name }}**.

## 1. TODO: Put a title here

TODO: Provide a step by step guide here.

# What's next?

For more details about **{{ cookiecutter.project_name }}** and all its possibilities and features, please check the
[documentation site](https://{{ cookiecutter.github_owner }}.github.io/{{ cookiecutter.repository_name }}/).
