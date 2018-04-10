======================
Cookiecutter PyPackage
======================

Cookiecutter_ template for a Python package, customized for DAI-Lab.

This is a slight fork of https://github.com/audreyr/cookiecutter-pypackage.

Why do this stuff? See `Why???`_.

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

   * Deactivate any virtual environments. (This may or may not be necessary for you, tox definitely doesn't work inside conda.)
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
       * `Sign up for a Test PyPI account`_ (this is different from normal PyPI but looks exactly the same)
       * Ensure that ``make test-release`` works
       * View your test release at https://test.pypi.org/project/PROJECT_NAME (or similar)

   * Release your package by pushing a new tag to master (``git tag -a v0.1.0 -m "Tag version 0.1.0"``), and Travis will automatically deploy your release

6. Configure Travis to automatically deploy documentation to GitHub pages

   * Configure a GitHub deployment token and add it to Travis. See the ``.travis.yml`` file of your project for details.
   * Push a commit and watch your documentation being built.
   * View the documentation at https://hdi-project.github.io/PROJECT_NAME

7. Start developing!

   * Add a `requirements.txt` file that specifies the packages you will need for your project and their versions. For more info see the `pip docs for requirements files`_.

For more details, see the `cookiecutter-pypackage tutorial`_.

Why???
------

Why should you use this? Why do you want these features? Here are some quick and
dirty answers, that will hopefully get expanded and referenced with appropriate
links.

You're probably doing some of these things already, like structuring your python
package in a standard manner, writing README, setup.py, and requirements.txt
files, and writing tests. This is not enough to (a) distribute your code (b) get
people to trust your code (c) get people to download your code (d) get people to
use your code.

Let this template handle the little things. You will avoid the following:

* committing ``.pyc`` files or other binary files because you never thought to add
  a ``.gitignore``
* omitting a ``LICENSE`` which means that other people cannot legally reuse your
  software
* having your tests pass locally but finding that a stranger on the internet
  can't install your code because they use Python 3.5 and you use Python 3.6
* having a sequence of 8 commits (``add Travis``, ``see if this fix makes Travis
  work now``, ``Travis still doesn't work``, etc.) because you are rolling your own
  configuration for different services one project at a time
* spending time and effort figuring out how to release your project on PyPI
* releasing your project on PyPI and finding that people can't install it
  successfully because you misconfigured one release
* etc.

Distribution
~~~~~~~~~~~~

Do you want people to use your software? If so

* you need to make it available on PyPI
* you need to make it trustworthy with up-to-date testing and documentation that
  can be verified and referenced
* you need to signal that it is high-quality by following best practices

It is imperative that ``pip install your_package`` works out of the box for as
many people as possible, and that they can quickly assess whether your software
is high-quality and deserves a chance to be used.

Testing
~~~~~~~

If you're reading this, you should be testing your code. With unittests and
integration tests if applicable. Full stop.

There are several unit testing frameworks in Python. You can use whatever one
you want. Unittest in Python 3 is part of the standard library and is pretty
solid. You can use pytest as a test runner. It's easiest if we are consistent
across the lab.

But writing and running your tests is just one part of the picture. ``tox`` makes
sure that your code works/your tests pass on every version of Python you claim
to support and all other dependencies your require. What is the probability that
the person who wants to pip install your package is using the same version of
Python as you are? This is standard in python projects.

Finally, you should run your tests automatically everytime you update your
software using continuous integration.

Docs
~~~~

You should document your code.

It is not enough to document your code in docstrings. Users across the world
should be able to quickly view your documentation on the web.

It is not enough to have your documentation on the web. Built documentation
should be standardized across the lab with a consistent theme/style to look
polished.

It is not enough to have a standardized look and feel. Built documentation
should be automatically updated to reflect the current state of your repository.

Finally, it is not enough to just write docstrings etc. You should also write
expository documentation: introduction, installation, quick start/basic usage,
tutorial/advanced usage, examples, faq, how to contribute, API reference.

Dev tools
~~~~~~~~

Use dev tools to make your life easier.

Want to release a new version of your software?

1. Update your HISTORY file
2. Use ``bumpversion`` to tag a new version following semantic versioning.
3. Push your commit and tags to GitHub, and have your CI service automatically
   deploy a new release to PyPI.

Want to automatically build and deploy your documentation?

1. Literally, do nothing different. If you configure your CI provider
   correctly, your documentation can be rebuild and redeployed on every commit.

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
