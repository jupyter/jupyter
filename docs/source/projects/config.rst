.. _jupyter_config:

Jupyter's Common Configuration Approach
=======================================

**Common Jupyter configuration system**
The Jupyter applications have a common config system, and a common
:ref:`config directory <config_dir>`. By default, this directory is
:file:`~/.jupyter`.

**Kernel configuration directories**
If kernels use config files, these will normally be organised in separate
directories for each kernel. For instance, the IPython kernel looks for files
in the :ref:`IPython directory <ipythondir>` instead of the default Jupyter
directory :file:`~/.jupyter`.

The Python config file
----------------------

To create a default config file, run:

.. code-block:: bash

    jupyter {application} --generate-config

The generated file will be named :file:`jupyter_{application}_config.py`.

By editing the :file:`jupyter_{application}_config.py` file, you can configure
class attributes like this::

    c.NotebookApp.port = 8754

Be careful with spelling. Incorrect names will simply be ignored, with
no error message.

To add to a collection which may have already been defined elsewhere,
you can use methods like those found on lists, dicts and sets: ``append``,
``extend``, :meth:`~traitlets.config.LazyConfigValue.prepend` (like
extend, but at the front), ``add``, and ``update`` (which works both for dicts
and sets)::

    c.TemplateExporter.template_path.append('./templates')


Command line options for configuration
--------------------------------------
Every configurable value can also be set from the command line and passed as
an argument, using this syntax:

.. code-block:: bash

    jupyter notebook --NotebookApp.port=8754

Frequently used options will also have short aliases and flags, such as
``--port 8754`` or ``--no-browser``.

To see the abbreviated options, pass :option:`--help` or :option:`--help-all`
as follows:

.. code-block:: bash

    jupyter {application} --help       # Just the short options
    jupyter {application} --help-all   # Includes options without short names

Command line options **will override** options set within a
configuration file.

.. seealso::

   :mod:`traitlets:traitlets.config`
       The low-level architecture of this config system.
