# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""

{%- if cookiecutter.github_username == cookiecutter.github_orgname %}
__author__ = '{{ cookiecutter.full_name.replace("\'", "\\\'") }}'
__email__ = '{{ cookiecutter.email }}'
{%- else %}
__author__ = 'MIT Data To AI Lab'
__email__ = 'dailabmit@gmail.com'
{%- endif %}
__version__ = '{{ cookiecutter.version }}'
