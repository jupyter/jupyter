.. _jupyter_command:

The :command:`jupyter` Command
==============================

.. program:: jupyter

Synopsis
--------

::

    jupyter <subcommand> [options]

Description
-----------

Commands like ``jupyter notebook`` start Jupyter applications.
The ``jupyter`` command is primarily a namespace for subcommands.
A command like ``jupyter-foo`` found on your :envvar:`PATH` will be
available as a subcommand ``jupyter foo``.

The :command:`jupyter` command can also be used to do actions other than
starting a Jupyter application.

Command options
----------------

.. option:: -h, --help

   Show help information, including available subcommands.

.. option:: --config-dir

   Show the location of the config directory.

.. option:: --data-dir

   Show the location of the data directory.

.. option:: --runtime-dir

   Show the location of the runtime directory.

.. option:: --paths

   Show all Jupyter directories and search paths.

.. option:: --json

   Print directories and search paths in machine-readable JSON format.
