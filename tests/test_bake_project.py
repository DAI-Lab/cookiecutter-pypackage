from contextlib import contextmanager
import shlex
import os
import sys
import subprocess
import yaml
import datetime
import tempfile
import shutil
from cookiecutter.main import cookiecutter
import importlib.util
import importlib
from click.testing import CliRunner

@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)

@contextmanager
def bake_in_temp_dir(template_path, extra_context=None, keep_temp_dir=False):
    """
    Bake a cookiecutter template in a temporary directory.
    :param template_path: Path to the cookiecutter template.
    :param extra_context: Additional context for cookiecutter.
    :param keep_temp_dir: Boolean, if True, the temporary directory will not be removed.
    """
    temp_dir = tempfile.mkdtemp()
    try:
        cookiecutter(template_path, no_input=True, extra_context=extra_context, output_dir=temp_dir)
        yield temp_dir
    finally:
        if not keep_temp_dir:
            shutil.rmtree(temp_dir)

def test_bake_with_defaults():
    template_path = os.path.abspath("../cookiecutter-pypackage")
    with bake_in_temp_dir(template_path) as temp_dir:
        project_dir = os.path.join(temp_dir, 'python-boilerplate')
        project_files = os.listdir(project_dir)
        assert 'pyproject.toml' in project_files
        assert 'README.md' in project_files
        assert 'tests' in project_files

def test_bake_and_run_tests():
    template_path = os.path.abspath("../cookiecutter-pypackage")
    with bake_in_temp_dir(template_path) as temp_dir:
        assert os.path.isdir(temp_dir)

        # Check that pytest is used by default
        test_file_path = os.path.join(temp_dir, 'python-boilerplate', 'tests', 'test_python_boilerplate.py')
        with open(test_file_path, 'r') as test_file:
            assert "import pytest" in test_file.read()

        # Run pytest directly to validate the baked project
        result = subprocess.run(['pytest', '--maxfail=1', '--disable-warnings'], cwd=temp_dir, capture_output=True)
        print(result.stdout.decode())
        print(result.stderr.decode())
        assert result.returncode == 0

def test_bake_with_custom_context():
    template_path = os.path.abspath("../cookiecutter-pypackage")
    extra_context = {
        "project_name": "Custom Project",
        "full_name": "Test Author",
        "package_name": "custom-project",
        "project_slug": "custom_project",
        "repository_name": "custom-project"
    }
    with bake_in_temp_dir(template_path, extra_context=extra_context) as temp_dir:
        project_dir = os.path.join(temp_dir, 'custom-project')
        with open(os.path.join(project_dir, 'pyproject.toml')) as f:
            content = f.read()
            assert "Custom Project" in content
            assert "Test Author" in content

def test_year_in_license_file():
    """Ensure the current year is included in the LICENSE file."""
    template_path = os.path.abspath("../cookiecutter-pypackage")
    with bake_in_temp_dir(template_path) as temp_dir:
        license_file_path = os.path.join(temp_dir, 'python-boilerplate', 'LICENSE')
        now = datetime.datetime.now()
        with open(license_file_path, 'r') as license_file:
            assert str(now.year) in license_file.read()

def test_bake_with_special_characters():
    """Ensure special characters in `full_name` do not break the template."""
    template_path = os.path.abspath("../cookiecutter-pypackage")
    extra_context = {"full_name": "O'Connor"}
    with bake_in_temp_dir(template_path, extra_context=extra_context) as temp_dir:
        project_dir = os.path.join(temp_dir, 'python-boilerplate')
        assert os.path.isdir(project_dir)

def test_make_help():
    template_path = os.path.abspath("../cookiecutter-pypackage")
    with bake_in_temp_dir(template_path) as temp_dir:
        project_dir = os.path.join(temp_dir, 'python-boilerplate')
        makefile_path = os.path.join(project_dir, 'Makefile')

        # Debugging: Print the contents of the baked project directory
        print("Contents of the baked project directory:")
        print(os.listdir(project_dir))

        # Check if Makefile exists
        assert os.path.exists(makefile_path), "Makefile is missing in the baked project."

        # Run make help
        result = subprocess.run(['make', 'help'], cwd=project_dir, capture_output=True, text=True)
        output = result.stdout
        error_output = result.stderr

        # Debugging information
        print("STDOUT:")
        print(output)
        print("STDERR:")
        print(error_output)

        # Assertions
        assert "install the package to the active Python's site-packages" in output
        assert "check code coverage quickly with the default Python" in output
        assert "generate Sphinx HTML documentation, including API docs" in output

def test_bake_not_open_source():
    template_path = os.path.abspath("../cookiecutter-pypackage")
    with bake_in_temp_dir(template_path, extra_context={'open_source_license': 'Not open source'}) as temp_dir:
        project_dir = os.path.join(temp_dir, 'python-boilerplate')
        project_files = os.listdir(project_dir)
        assert 'pyproject.toml' in project_files
        assert 'LICENSE' not in project_files
        with open(os.path.join(project_dir, 'README.md')) as readme:
            assert 'License' not in readme.read()

def test_bake_selecting_license():
    template_path = os.path.abspath("../cookiecutter-pypackage")
    license_strings = {
        'MIT license': 'MIT ',
        'BSD license': 'Redistributions of source code must retain the above copyright notice, this',
        'ISC license': 'ISC License',
        'Apache Software License 2.0': 'Licensed under the Apache License, Version 2.0',
        'GNU General Public License v3': 'GNU GENERAL PUBLIC LICENSE',
    }
    for license, target_string in license_strings.items():
        with bake_in_temp_dir(template_path, extra_context={'open_source_license': license}) as temp_dir:
            license_file_path = os.path.join(temp_dir, 'python-boilerplate', 'LICENSE')
            with open(license_file_path) as license_file:
                assert target_string in license_file.read()

def test_bake_with_no_console_script():
    template_path = os.path.abspath("../cookiecutter-pypackage")
    with bake_in_temp_dir(template_path, extra_context={'command_line_interface': "No command-line interface"}) as temp_dir:
        project_dir = os.path.join(temp_dir, 'python-boilerplate')
        project_files = os.listdir(project_dir)
        assert "cli.py" not in project_files

def test_bake_with_console_script_files():
    template_path = os.path.abspath("../cookiecutter-pypackage")
    with bake_in_temp_dir(template_path, extra_context={'command_line_interface': 'Click'}) as temp_dir:  # Updated to match valid choices
        project_dir = os.path.join(temp_dir, 'python-boilerplate')
        package_dir = os.path.join(project_dir, 'python_boilerplate')
        project_files = os.listdir(package_dir)
        assert "cli.py" in project_files

def test_bake_with_console_script_cli():
    template_path = os.path.abspath("../cookiecutter-pypackage")
    with bake_in_temp_dir(template_path, extra_context={'command_line_interface': 'Click'}) as temp_dir:  # Updated to match valid choices
        project_dir = os.path.join(temp_dir, 'python-boilerplate')
        cli_path = os.path.join(project_dir, 'python_boilerplate', 'cli.py')
        module_name = 'python_boilerplate.cli'
        spec = importlib.util.spec_from_file_location(module_name, cli_path)
        cli = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cli)
        runner = CliRunner()
        noarg_result = runner.invoke(cli.main)
        assert noarg_result.exit_code == 0
        assert 'Replace this message by putting your code into' in noarg_result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert 'Show this message' in help_result.output
