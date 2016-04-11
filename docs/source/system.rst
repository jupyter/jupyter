Jupyter on your system
======================

.. _jupyter_command:

The jupyter command
-------------------

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


.. _jupyter_directories:

Jupyter directories
-------------------

Jupyter stores different files (i.e. configuration, data, runtime) in a
number of different locations. Environment variables may be set for each
location.

.. _config_dir:

Configuration
~~~~~~~~~~~~~

Config files are stored by default in the :file:`~/.jupyter` directory.

.. envvar:: JUPYTER_CONFIG_DIR
   
   Set this environment variable to use a directory, other than the above
   default, for Jupyter config files.

Besides the main user config directory mentioned above, Jupyter has a search
path of additional locations from which config will be loaded. Here's a table
of the locations:

+------------------------------+----------------------------+
| Unix                         | Windows                    |
+==============================+============================+
|                      Config directory                     |
+------------------------------+----------------------------+
|                ``{sys.prefix}/etc/jupyter/``              |
+------------------------------+----------------------------+
|| ``/usr/local/etc/jupyter/`` | ``%PROGRAMDATA%\jupyter\`` |
|| ``/etc/jupyter/``           |                            |
+------------------------------+----------------------------+

.. _jupyter_path:

Data files
~~~~~~~~~~

Jupyter uses a search path to find installable data files, such as 
:ref:`kernelspecs <kernelspecs>` and notebook extensions. When searching for
a resource, code will stop searching the search path at the first directory 
where the resource is contained.

Each category of file in here is in a subdirectory of each directory of the
search path. E.g. kernel specs are in ``kernels`` subdirectories.

.. envvar:: JUPYTER_PATH

   Set this environment variable to provide extra directories for the data
   search path. It should be a series of directory paths, separated by
   ``os.pathsep`` (i.e. ``;`` on Windows, ``:`` on Unix).
   Directories given in :envvar:`JUPTYER_PATH` are searched first.

+-------------------------------+----------------------------+----------------------------+
| Linux (& other free desktops) | Mac                        | Windows                    |
+===============================+============================+============================+
| :envvar:`JUPYTER_PATH`                                                                  |
+-------------------------------+----------------------------+----------------------------+
|| ``~/.local/share/jupyter/``  | ``~/Library/Jupyter``      | ``%APPDATA%\jupyter``      |
|| (respects ``$XDG_DATA_HOME``)|                            |                            |
+-------------------------------+----------------------------+----------------------------+
| ``{sys.prefix}/share/jupyter/``                                                         |
+-------------------------------+----------------------------+----------------------------+
|| ``/usr/local/share/jupyter``                              | ``%PROGRAMDATA\jupyter``   |
|| ``/usr/share/jupyter``                                    |                            |
+-------------------------------+----------------------------+----------------------------+

.. _jupyter_runtime_dir:

Runtime files
~~~~~~~~~~~~~

Things like connection files, which are only useful for the lifetime of a
specific process, have their own directory.

On Linux and other free desktop platforms, these runtime files are stored in
``$XDG_RUNTIME_DIR/jupyter`` by default. On other platforms, it's a
``runtime/`` subdirectory of the user's data directory (second row of the
table above).

An environment variable may also be set:

.. envvar:: JUPYTER_RUNTIME_DIR

   Set this to override where Jupyter stores runtime files.

.. seealso::

   :mod:`jupyter_core.paths`
       The Python API to locate these directories.
   :ref:`jupyter_command`
       Locate these directories from the command line.
