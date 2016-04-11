.. _migrating:

===============================
Migrating from IPython Notebook
===============================

`The Big Split <https://blog.jupyter.org/2015/04/15/the-big-split/>`__
has changed a few things, moving the various language-agnostic
components of IPython under the Jupyter umbrella. This document
describes what has changed, and how you may need to modify your code or
configuration.

The first time you run any jupyter command, it will perform an automatic
migration of files. This **copies** (not moves, so IPython 3 will be
unaffected) files to their new homes, You can re-run the migration by
calling :command:`jupyter migrate`. This means that you shouldn't need to do
anything to keep using your custom configuration with Jupyter. What it
does mean, though, is that when you go to update or modify your
configuration, the relevant locations may have changed.

Where have all my files gone?
-----------------------------

AKA Why isn't my configuration having any effect anymore?

Jupyter splitting out from IPython means that the locations of some
files have moved, and Jupyter projects have not inherited everything
from how IPython did it. When you start your first jupyter application,
the relevant configuration files are automatically copied to their new
Jupyter locations. The configuration files in their IPython locations no
longer affect Jupyter, so if you edit your existing config file and it
is not having the desired effect, this is the likely cause—you are
editing the old location of a file, rather than the file that is
actually loaded.

Quick reference
~~~~~~~~~~~~~~~

A quick reference for common locations of relocated files. **These
should all be automatically copied to their new locations.**

Configuration files
^^^^^^^^^^^^^^^^^^^

-  :file:`~/.ipython/profile_default/static/custom` → :file:`~/.jupyter/custom`
-  ``~/.ipython/profile_default/ipython_notebook_config.py`` →
   ``~/.jupyter/jupyter_notebook_config.py``
-  ``~/.ipython/profile_default/ipython_nbconvert_config.py`` →
   ``~/.jupyter/jupyter_nbconvert_config.py``
-  ``~/.ipython/profile_default/ipython_qtconsole_config.py`` →
   ``~/.jupyter/jupyter_qtconsole_config.py``
-  ``~/.ipython/profile_default/ipython_console_config.py`` →
   ``~/.jupyter/jupyter_console_config.py``

``JUPYTER_CONFIG_DIR`` environment variable can be used if :file:`~/.jupyter`
is not desired.

Data files
^^^^^^^^^^

Data files are things that are installed, but not configuration. This
includes kernelspecs and notebook extensions. Like config files above,
**data files are automatically migrated to their new locations**.

In IPython 3, these data files lived in ``~/.ipython``. In Jupyter, data
files use platform-appropriate locations:

-  OS X: ``~/Library/Jupyter``
-  Windows: the ``%APPDATA%`` environment variable is used
-  Elsewhere, ``$XDG_DATA_HOME`` is respected, with the default of
   ``~/.local/share/jupyter``

In all cases, ``JUPYTER_DATA_DIR`` can be used to specify this location
explicitly. Data files installed system-wide (e.g. in
``/usr/local/share/jupyter``) have not changed. Per-user installation of
these has changed from going in ``.ipython`` to the above locations.

Profiles
~~~~~~~~

IPython has the concept of **profiles**, which are collections of
configuration and runtime files. Inside the IPython directory
(``~/.ipython``), there are directories with names like
``profile_default`` or ``profile_demo``. In each of these are
configuration files (``ipython_config.py``,
``ipython_notebook_config.py``) and runtime files (``history.sqlite``,
``security/kernel-*.json``). Profiles could be used to switch between
configurations of IPython. **Jupyter does not have profiles**.

People could use commands like :command:`ipython notebook --profile demo` to
set the profile for *both* the notebook server and the IPython kernel.
This is no longer possible in one go with Jupyter, just like it wasn't
possible in IPython 3 for any other kernels. If you wanted to change the
notebook configuration, you can set the ``JUPYTER_CONFIG_DIR``::

    JUPYTER_CONFIG_DIR=./jupyter_config jupyter notebook

If you just want to change the config file, you can do::

    jupyter notebook --config=/path/to/myconfig.py

If, instead, you do want to change the IPython kernel's profile, you
can't do this at the server command-line anymore. Kernel arguments must
be done by modifying the kernelspec. The good thing about this is that
you can do it without relaunching the server. Kernelspec changes take
effect every time you start a new kernel. The less good thing is that
there isn't a great way to modify the kernelspecs. You can see where the
file is with ``jupyter kernelspec list``, and then modify
``kernels/python3/kernel.json`` by hand.
`a2km <https://github.com/minrk/a2km>`__ is an experimental project that
tries to make these things easier.

Installation
------------

See the :ref:`install` page for more information about
installing Jupyter itself. There are some things that you install *with
Jupyter*, which are a kind of data files, described above. Jupyter
automatically migrates these

Notebook extensions
~~~~~~~~~~~~~~~~~~~

Any IPython notebook extensions should be automatically migrated as part
of the data-files migration above.

Notebook extensions used to be installed with::

    ipython install-nbextension [--user] EXTENSION

They are now installed with::

    jupyter nbextension install [--user] EXTENSION

They will go in the ``JUPYTER_DATA_DIR`` above if a ``--user`` install
is specified, otherwise they will go in a system-wide location (e.g.
``/usr/local/share/jupyter/nbextensions``). Installation **SHOULD NOT**
be done by manually guessing where the files should go.

Kernels
~~~~~~~

Kernels are installed in much the same way as notebook extensions above,
and also like notebook extensions, they will be automatically migrated.

Kernel specs used to be installed with::

    ipython kernelspec install [--user] KERNEL

They are now installed with::

    jupyter kernelspec install [--user] KERNEL

They will go in the ``JUPYTER_DATA_DIR`` above if a ``--user`` install
is specified, otherwise they will go in a system-wide location (e.g.
``/usr/local/share/jupyter/kernels``). Installation **SHOULD NOT** be
done by manually guessing where the files should go.

Imports
-------

The split has created many new packages. IPython 4.0 includes shims so
if you have the dependencies all imports that work on IPython 3 should
continue to work on IPython 4. If this is not the case, `let us
know <https://github.com/ipython/ipython/issues>`__.

Some changed imports:

-  ``IPython.html`` → ``notebook``
-  ``IPython.html.widgets`` → ``ipywidgets``
-  ``IPython.kernel`` → ``jupyter_client``, ``ipykernel``
   (``IPython.kernel`` became two packages - one for the client-side
   APIs, one for the IPython kernel for Jupyter)
-  ``IPython.parallel`` → ``ipyparallel``
-  ``IPython.qt.console`` → ``qtconsole``
-  ``IPython.utils.traitlets`` → ``traitlets``
-  ``IPython.config`` → ``traitlets.config``
