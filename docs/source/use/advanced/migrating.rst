===============================
Migrating from IPython Notebook
===============================

.. contents:: Contents
   :local:

Abstract
--------

`The Big Split <https://blog.jupyter.org/the-big-split-9d7b88a031a7>`__
moved IPython's various language-agnostic components under the Jupyter
umbrella. Going forward, Jupyter will contain the language-agnostic
projects that serve many languages. IPython will continue to focus
on Python and its use with Jupyter.

This document describes what has changed, and how you may need to
modify your code or configuration when migrating from IPython version 3 to
Jupyter.

Understanding the Migration Process
-----------------------------------

Automatic migration of files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first time you run any ``jupyter`` command, it will perform an automatic
migration of files. The automatic migration process **copies** files,
instead of moving files, leaving the originals in place and the copies in the
Jupyter file locations. You can re-run the migration, if needed, by calling
``jupyter migrate``. Your custom configuration will be migrated automatically
and should work with Jupyter without further editing. When you update or
modify your configuration in the future, please keep in mind that the file
locations may have changed.

Where have my configuration files gone?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Also known as: "Why isn't my configuration having any effect anymore?"

Jupyter splitting out from IPython means that the locations of some
files have moved, and Jupyter projects have not inherited everything
from how IPython did it.

When you start your first Jupyter application, the relevant configuration
files are automatically copied to their new Jupyter locations. The original
configuration files in the IPython locations have no effect on Jupyter's
execution. If you accidentally edit your original IPython config file, you may
not see the desired effect with Jupyter now. You should check that you are
editing Jupyter's configuration file, and you should see the expected effect
after restarting the Jupyter server.

Finding the Location of Important Files
---------------------------------------

This section provides quick reference for common locations of IPython 3 files
and the migrated Jupyter files.

Configuration files
~~~~~~~~~~~~~~~~~~~

Configuration files customize Jupyter to the user's preferences.
The migrated files should all be **automatically copied** to their new Jupyter
locations. Here are the location changes:

==============================================================  =====    ==============================================
IPython location                                                          Jupyter location
==============================================================  =====    ==============================================
:file:`~/.ipython/profile_default/static/custom`                  →      :file:`~/.jupyter/custom`
:file:`~/.ipython/profile_default/ipython_notebook_config.py`     →      :file:`~/.jupyter/jupyter_notebook_config.py`
:file:`~/.ipython/profile_default/ipython_nbconvert_config.py`    →      :file:`~/.jupyter/jupyter_nbconvert_config.py`
:file:`~/.ipython/profile_default/ipython_qtconsole_config.py`    →      :file:`~/.jupyter/jupyter_qtconsole_config.py`
:file:`~/.ipython/profile_default/ipython_console_config.py`      →      :file:`~/.jupyter/jupyter_console_config.py`
==============================================================  =====    ==============================================

To choose a directory location other than the default :file:`~/.jupyter`, set
the ``JUPYTER_CONFIG_DIR`` environment variable. You may need to run
``jupyter migrate`` after setting the environment variable for files to be
copied to the desired directory.

Data files: kernelspecs and notebook extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data files include files, other than configuration files, which are
user installed. Examples include kernelspecs and notebook extensions. Like
the configuration files, data files are also **automatically migrated** to
their new Jupyter locations.

In **IPython 3**, data files lived in ``~/.ipython``.

In **Jupyter**, data files use platform-appropriate locations:

-  OS X: ``~/Library/Jupyter``
-  Windows: the location specified in ``%APPDATA%`` environment variable
-  Elsewhere, ``$XDG_DATA_HOME`` is respected, with the default of
   ``~/.local/share/jupyter``

In all cases, the ``JUPYTER_DATA_DIR`` environment variable can be used to set
a location explicitly.

Data files installed system-wide (e.g. in ``/usr/local/share/jupyter``) have
not changed. Per-user installation of data files has changed location from
``.ipython`` to the platform-appropriate Jupyter location.

Since Jupyter does not have profiles, how do I customize it?
------------------------------------------------------------

While IPython has the concept of :term:`profiles`, **Jupyter does not have
profiles**.

In IPython, profiles are collections of configuration and runtime files.
Inside the IPython directory (``~/.ipython``), there are directories with
names like ``profile_default`` or ``profile_demo``. In each of these are
configuration files (``ipython_config.py``, ``ipython_notebook_config.py``)
and runtime files (``history.sqlite``, ``security/kernel-*.json``). Profiles
could be used to switch between configurations of IPython.

Previously, people could use commands like ``ipython notebook --profile demo``
to set the profile for *both* the notebook server and the IPython kernel.
This is no longer possible in one go with Jupyter, just like it wasn't
possible in IPython 3 for any other kernels.

Changing the Jupyter notebook configuration directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to change the notebook configuration, you can set the
``JUPYTER_CONFIG_DIR``:

.. code-block:: bash

    JUPYTER_CONFIG_DIR=./jupyter_config
    jupyter notebook

Changing the Jupyter notebook configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you just want to change the config file, you can do:

.. code-block:: bash

    jupyter notebook --config=/path/to/myconfig.py

Changing IPython's profile using custom kernelspecs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you do want to change the IPython kernel's profile, you
can't do this at the server command-line anymore. Kernel arguments must
be changed by modifying the kernelspec. You can do this without relaunching
the server. Kernelspec changes take effect every time you start a new kernel.
However, there isn't a great way to modify the kernelspecs.
One approach uses ``jupyter kernelspec list`` to find the
``kernel.json`` file and then modifies it, e.g. ``kernels/python3/kernel.json``,
by hand. Alternatively, `a2km <https://github.com/minrk/a2km>`__ is an
experimental project that tries to make these things easier.

For example, add the ``--profile`` option to a custom kernelspec under ``kernels/mycustom/kernel.json``
(see the Jupyter kernelspec directions
`here <https://jupyter-client.readthedocs.io/en/latest/kernels.html#kernel-specs>`__):

.. code-block:: json

    {
     "argv": ["python", "-m", "ipykernel",
              "--profile=my-ipython-profile",
              "-f", "{connection_file}"],
     "display_name": "Custom Profile Python",
     "language": "python"
    }

You can then run Jupyter with the ``--kernel=mycustom`` command-line option and IPython
will find the appropriate profile.

Understanding Installation Changes
----------------------------------

See the :ref:`install` page for more information about
installing Jupyter. Jupyter automatically migrates some things,
like Notebook extensions and kernels.

Notebook extensions
~~~~~~~~~~~~~~~~~~~

Any IPython notebook extensions should be **automatically migrated** as part
of the data files migration.

Notebook extensions were installed with:

.. code-block:: bash

    ipython install-nbextension [--user] EXTENSION

Now, extensions are installed with:

.. code-block:: bash

    jupyter nbextension install [--user] EXTENSION

The notebook extensions will be installed in a system-wide location (e.g.
``/usr/local/share/jupyter/nbextensions``). If doing a ``--user``
install, the notebook extensions will go in the ``JUPYTER_DATA_DIR`` location.
Installation **SHOULD NOT** be done manually by guessing where the files
should go.

Kernels
~~~~~~~

Kernels are installed in much the same way as notebook extensions. They will
also be **automatically migrated**.

Kernel specs used to be installed with:

.. code-block:: bash

    ipython kernelspec install [--user] KERNEL

They are now installed with:

.. code-block:: bash

    jupyter kernelspec install [--user] KERNEL

By default, kernel specs will go in a system-wide location
(e.g. ``/usr/local/share/jupyter/kernels``). If doing a ``--user`` install,
the kernel specs will go in the ``JUPYTER_DATA_DIR`` location. Installation
**SHOULD NOT** be done manually by guessing where the files should go.

Understanding Changes in imports
--------------------------------

IPython 4.0 includes shims to manage dependencies; so, all imports that work
on IPython 3 should continue to work on IPython 4. If you find any
differences, please `let us know <https://github.com/ipython/ipython/issues>`__.

Some changes include:

==================================  =====  ==================================
IPython 3                                   Jupyter and IPython 4.0
==================================  =====  ==================================
``IPython.html``                     →      ``notebook``
``IPython.html.widgets``             →      ``ipywidgets``
``IPython.kernel``                   →      ``jupyter_client``, ``ipykernel``
``IPython.parallel``                 →      ``ipyparallel``
``IPython.qt.console``               →      ``qtconsole``
``IPython.utils.traitlets``          →      ``traitlets``
``IPython.config``                   →      ``traitlets.config``
==================================  =====  ==================================

.. important::

    The ``IPython.kernel`` Split

    ``IPython.kernel`` became two packages:

    * ``jupyter_client`` for the Jupyter client-side APIs.
    * ``ipykernel`` for Jupyter's IPython kernel
