======================
Cookiecutter PyPackage
======================

Cookiecutter_ template for a Python package, customized for DAI-Lab.

This is a slight fork of https://github.com/audreyr/cookiecutter-pypackage.

FOR ANY BUGS OR QUESTIONS, CONTACT MICAH SMITH (@micahjsmith).

* GitHub repo: https://github.com/DAI-Lab/cookiecutter-pypackage/
* Free software: BSD license

Features
--------

* Testing setup with ``unittest`` and ``pytest``
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 2.7, 3.4, 3.5, 3.6
* Sphinx_ docs: Documentation ready for generation, automatic building and deploying to gh-pages (last part optional)
* Bumpversion_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click (optional)

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project (this will create a new subdirectory of your
current working directory)::

    cookiecutter gh:DAI-Lab/cookiecutter-pypackage

Then:

1. Initialize a git repo in your new project

  * Commit the new project (``git add .`` and ``git commit -m "Initial commit"``)

2. Create and test your development environment

  * Create a virtual environment of your choice ( e.g. ``conda create -n project_name_env python=3.6``, ``virtualenv``, ``pyenv``, etc.).
  * Install the dev environment (``python setup.py develop``).
  * Check that the tests work (``make test``)
  * Check that the linter works (``make lint``)

3. Make sure that you can test your project using tox

  * Deactivate any virtual environments. (This may or may not be necessary for you, tox
    definitely doesn't work inside conda.)
  * Install tox (``pip install tox``)
  * Run tox (``tox``)

4. Configure Travis to run tests and build documentation

  * Create the repo on GitHub if it is not already there
  * Add the repo to your Travis-CI_ account (https://travis-ci.org/ORG_NAME/PROJECT_NAME)
  * Push a commit and monitor the build

5. Configure Travis to automatically deploy to PyPI on new tags

  * Register_ your project with PyPI.
  * Use Travis to encrypt your PyPI password in Travis config and activate automated deployment on PyPI when you push a new tag to master branch. See the ``.travis.yml`` file of your project for details.
  * Test the release process

      * Ensure you can create the dist using ``make dist``
      * `Sign up for a Test PyPI account`_ (this is different from normal PyPI but
        looks exactly the same)
      * Ensure that ``make test-release`` works
      * View your test release at https://test.pypi.org/project/PROJECT_NAME (or
        similar)

  * Release your package by pushing a new tag to master (``git tag -a v0.1.0 -m "Tag version 0.1.0"``), and Travis will automatically deploy your release

6. Configure Travis to automatically deploy documentation to GitHub pages

  * Configure a GitHub deployment token and add it to Travis. See the ``.travis.yml`` file of your
    project for details.
  * Push a commit and watch your documentation being built.
  * View the documentation at https://hdi-project.github.io/PROJECT_NAME

7. Start developing!

  * Add a `requirements.txt` file that specifies the packages you will need for
    your project and their versions. For more info see the `pip docs for requirements files`_.

For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _`Sign up for a Test PyPI account`: https://test.pypi.org/account/register/
.. _Register: https://packaging.python.org/distributing/#register-your-project
.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html
.. _Cookiecutter: https://github.com/DAI-Lab/cookiecutter
.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _Bumpversion: https://github.com/peritus/bumpversion
.. _PyPi: https://pypi.python.org/pypi
