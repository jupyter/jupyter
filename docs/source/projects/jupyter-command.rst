.. _jupyter_command:

The ``jupyter`` Command
=======================

.. program:: jupyter

Jupyter applications are started with commands like ``jupyter notebook``.
The ``jupyter`` command is primarily a namespace for subcommands:
a command like ``jupyter-foo`` found on your :envvar:`PATH` will be
available as a subcommand ``jupyter foo``.

The jupyter command can also do a few basic things itself:

.. option:: --help , -h

   Show help information, including available subcommands.

.. option:: --config-dir

   Show the location of the config directory.

.. option:: --data-dir

   Show the location of the data directory.

.. option:: --runtime-dir

   Show the location of the data directory.

.. option:: --paths

   Show all Jupyter directories and search paths.

.. option:: --json

   Print directories and search paths in machine-readable JSON format.