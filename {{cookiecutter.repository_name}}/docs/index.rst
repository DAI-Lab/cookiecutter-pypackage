.. mdinclude:: readme.rst

.. toctree::
   :hidden:
   :maxdepth: 2

   Overview <readme>
   installation
   usage

.. toctree::
   :caption: Advanced Usage
   :hidden:

   API Reference <api/{{ cookiecutter.project_slug }}>

.. toctree::
   :caption: Development Notes
   :hidden:

   contributing
   {% if cookiecutter.create_author_file == 'y' -%}authors
   {% endif -%}history

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
