.. _jupyter_directories:

Common Directories and File Locations
=====================================

.. contents:: Contents
   :local:

Jupyter stores different files (i.e. configuration, data, runtime) in a
number of different locations. Environment variables may be set to
customize for the location of each file type.

Jupyter separates **data files** (nbextensions, kernelspecs)
from **runtime files** (logs, pid files, connection files)
from **configuration** (config files, custom.js).

.. _config_dir:

Configuration files
-------------------

Config files are stored by default in the :file:`~/.jupyter` directory.

.. envvar:: JUPYTER_CONFIG_DIR

   Set this environment variable to use a particular directory, other than the
   default, for Jupyter config files.

Besides the :envvar:`JUPYTER_CONFIG_DIR`, additional directories to search can be 
specified through :envvar:`JUPYTER_CONFIG_PATH`.

.. envvar:: JUPYTER_CONFIG_PATH

   Set this environment variable to provide extra directories for the config search path.
   :envvar:`JUPYTER_CONFIG_PATH` should contain a series of directories, seperated by
   `` os.pathsep`` (``;`` on Windows, ``:`` on Unix).

An example of where the :envvar:`JUPYTER_CONFIG_PATH` can be set is if notebook or server extensions are 
installed in a custom prefix. Since notebook and server extensions are automatically enabled through configuration files, 
automatic enabling will only work if the custom prefix's ``etc/jupyter`` directory is added to the Jupyter config search path.

Besides the user config directory mentioned above, Jupyter has a search
path of additional locations from which a config file will be loaded. Here's a
table of the locations to be searched, in order of preference:

+------------------------------+----------------------------+
| Unix                         | Windows                    |
+==============================+============================+
|                 :envvar:`JUPYTER_CONFIG_DIR`              |
+------------------------------+----------------------------+
|                 :envvar:`JUPYTER_CONFIG_PATH`             |
+-----------------------------------------------------------+
|                ``{sys.prefix}/etc/jupyter/``              |
+------------------------------+----------------------------+
| ``/usr/local/etc/jupyter/``  | ``%PROGRAMDATA%\jupyter\`` |
| ``/etc/jupyter/``            |                            |
+------------------------------+----------------------------+

To list the config directories currrently being used you can run the below command from the :term:`command line`::

    jupyter --paths

The following command shows the config directory specifically::

    jupyter --config-dir

Data files
----------

.. _jupyter_path:


Jupyter uses a search path to find installable data files, such as
:ref:`kernelspecs <kernelspecs>` and notebook extensions. When searching for
a resource, the code will search the search path starting at the first
directory until it finds where the resource is contained.

Each category of file is in a subdirectory of each directory of the
search path. For example, kernel specs are in ``kernels`` subdirectories.

.. envvar:: JUPYTER_PATH

   Set this environment variable to provide extra directories for the data
   search path. :envvar:`JUPYTER_PATH` should contain a series of directories,
   separated by ``os.pathsep`` (``;`` on Windows, ``:`` on Unix).
   Directories given in :envvar:`JUPYTER_PATH` are searched before other
   locations. This is used in addition to other entries, rather than replacing any.

+-------------------------------+----------------------------+----------------------------+
| Linux (& other free desktops) | Mac                        | Windows                    |
+===============================+============================+============================+
| :envvar:`JUPYTER_PATH`                                                                  |
+-------------------------------+----------------------------+----------------------------+
| :envvar:`JUPYTER_DATA_DIR`    | :envvar:`JUPYTER_DATA_DIR` | :envvar:`JUPYTER_DATA_DIR` |
| or (if not set)               | or (if not set)            | or (if not set)            |
| ``~/.local/share/jupyter/``   | ``~/Library/Jupyter``      | ``%APPDATA%\jupyter``      |
| (respects ``$XDG_DATA_HOME``) |                            |                            |
+-------------------------------+----------------------------+----------------------------+
| ``{sys.prefix}/share/jupyter/``                                                         |
+-------------------------------+----------------------------+----------------------------+
| ``/usr/local/share/jupyter``                               | ``%PROGRAMDATA\jupyter``   |
| ``/usr/share/jupyter``                                     |                            |
+-------------------------------+----------------------------+----------------------------+

.. _jupyter_data_dir:

The config directory for Jupyter data files, which contain non-transient, non-configuration files.
Examples include kernelspecs, nbextensions, or voila templates.

.. envvar:: JUPYTER_DATA_DIR

   Set this environment variable to use a particular directory, other than the default, as the user data directory. 

As mentioned above, to list the config directories currently being used you can run the below command from the :term:`command line`::

   jupyter --paths

The following command shows the data directory specifically::

   jupyter --data-dir

.. _jupyter_runtime_dir:

Runtime files
-------------

Things like connection files, which are only useful for the lifetime of a
particular process, have a runtime directory.

On Linux and other free desktop platforms, these runtime files are stored in
``$XDG_RUNTIME_DIR/jupyter`` by default. On other platforms, it's a
``runtime/`` subdirectory of the user's data directory (second row of the
table above).

An environment variable may also be used to set the runtime directory.

.. envvar:: JUPYTER_RUNTIME_DIR

   Set this to override where Jupyter stores runtime files.

As mentioned above, to list the config directories currently being used you can run the below command from the :term:`command line`::

   jupyter --paths

The following command shows the runtime directory specifically::

   jupyter --runtime-dir

Summary
-------

:envvar:`JUPYTER_CONFIG_DIR` for config file location

:envvar:`JUPYTER_CONFIG_PATH` for config file locations

:envvar:`JUPYTER_PATH` for datafile directory locations

:envvar:`JUPYTER_DATA_DIR` for data file location

:envvar:`JUPYTER_RUNTIME_DIR` for runtime file location


.. seealso::

   :mod:`jupyter_core.paths`
       The Python API to locate these directories.

   :ref:`jupyter_command`
       Locate these directories from the command line.
