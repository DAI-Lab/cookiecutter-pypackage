#!/usr/bin/env python

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def copy_context():
    src = os.path.join(os.path.expanduser('~'),
                       '.cookiecutter_replay',
                       'cookiecutter-pypackage.json')
    dst = os.path.join(PROJECT_DIRECTORY, '.cookiecutter_replay.json')
    shutil.copyfile(src, dst)


def main():

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    copy_context()


if __name__ == '__main__':
    main()
