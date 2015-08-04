Configuring Jupyter applications
================================

The Jupyter applications have a common config system, and a common
:ref:`config directory <config_dir>`. By default, this is ``~/.jupyter``.

If kernels use config files, these will normally be organised separately.
For instance, the IPython kernel looks for files in the :ref:`IPython directory
<ipythondir>`.

Python config files
-------------------

To create the blank config files, run::

    jupyter {application} --generate-config

The file will be named :file:`jupyter_{application}_config.py`

Inside the file, you can configure class attributes like this::

    c.NotebookApp.port = 8754

Be careful with spelling--incorrect names will simply be ignored, with
no error.

To add to a collection which may have already been defined elsewhere,
you can use methods like those found on lists, dicts and sets: append,
extend, :meth:`~traitlets.config.LazyConfigValue.prepend` (like
extend, but at the front), add and update (which works both for dicts
and sets)::

    c.TemplateExporter.template_path.append('./templates')


Command line arguments
----------------------

Every configurable value can be set from the command line, using this
syntax::

    jupyter notebook --NotebookApp.port=8754

Many frequently used options have short aliases and flags, such as
``--port 8754`` or ``--no-browser``.

To see these abbreviated options, run::

    jupyter {application} --help       # Just the short options
    jupyter {application} --help-all   # Includes options without short names

Options specified at the command line, in either format, override
options set in a configuration file.

.. seealso::

   :mod:`traitlets:traitlets.config`
     The low-level architecture of this config system.
