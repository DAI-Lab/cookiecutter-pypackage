======================
Cookiecutter PyPackage
======================

Cookiecutter_ template for a Python package, customized for DAI-Lab.

This is a slight fork of https://github.com/audreyr/cookiecutter-pypackage.

* GitHub repo: https://github.com/DAI-Lab/cookiecutter-pypackage/
* Documentation: https://cookiecutter-pypackage.readthedocs.io/
* Free software: BSD license

Features
--------

* Testing setup with ``unittest`` and ``pytest``
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 2.7, 3.4, 3.5, 3.6
* Sphinx_ docs: Documentation ready for generation, automatic building and deploying to gh-pages (last part optional).
* Bumpversion_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click (optional)

.. _Cookiecutter: https://github.com/DAI-Lab/cookiecutter

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter gh:DAI-Lab/cookiecutter-pypackage

Then:

* Create a repo and put it there.
* Add the repo to your Travis-CI_ account.
* Create a virtual environment of your choice ( e.g. ``conda create -n project_name_env python=3.6``).
* Install the dev environment (``python setup.py develop``).
* Register_ your project with PyPI.
* Run the Travis CLI command `travis encrypt MY_PYPI_PASSWORD` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Test your release
  * Ensure you can create the dist using ``make dist``
  * `Sign up for a Test PyPI account`_ (this is different from normal PyPI but
    looks exactly the same)
  * Ensure that ``make test-release`` works
  * View your test release at https://test.pypi.org/project/project_name (or
    similar)
* Release your package by pushing a new tag to master (``git tag -a v0.1.0 -m "Tag version 0.1.0"``), and Travis will automatically deploy your release
* Add a `requirements.txt` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.
* View your built documentation on the web

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _`Sign up for a Test PyPI account`: https://test.pypi.org/account/register/
.. _Register: https://packaging.python.org/distributing/#register-your-project

For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html
