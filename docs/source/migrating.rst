Migrating from IPython
======================

`The Big Split <https://blog.jupyter.org/2015/04/15/the-big-split/>`__
has changed a few things, moving the various language-agnostict
components of IPython under the Jupyter umbrella. This doc should help
you find what's changed, and how to keep doing what you've been doing.

Where have all my files gone?
-----------------------------

AKA Why isn't my configuration having any effect anymore?

Jupyter splitting out from IPython means that the locations of some
files have moved, and Jupyter projects have not inherited everything
from how IPython did it.

The ``jupyter migrate`` command copies several of these files to their
new homes.

Quick reference
~~~~~~~~~~~~~~~

A quick reference for common locations of relocated files.

Configuration files
^^^^^^^^^^^^^^^^^^^

-  ``~/.ipython/profile_default/static/custom`` → ``~/.jupyter/custom``
-  ``~/.ipython/profile_default/ipython_notebook_config.py`` →
   ``~/.jupyter/jupyter_notebook_config.py``
-  ``~/.ipython/profile_default/ipython_nbconvert_config.py`` →
   ``~/.jupyter/jupyter_nbconvert_config.py``
-  ``~/.ipython/profile_default/ipython_qtconsole_config.py`` →
   ``~/.jupyter/jupyter_qtconsole_config.py``
-  ``~/.ipython/profile_default/ipython_console_config.py`` →
   ``~/.jupyter/jupyter_console_config.py``

``JUPYTER_CONFIG_DIR`` env can be used if ``~/.jupyter`` is not desired.

Data files
^^^^^^^^^^

Data files are things that are installed, but not configuration. This
includes kernelspecs and notebook extensions. Data files use
platform-appropriate locations:

-  OS X: ``~/Library/Jupyter``
-  Windows: the ``%APPDATA%`` environment variable is used
-  Elsewhere, ``$XDG_DATA_HOME`` is respected, with the default of
   ``~/.local/share/jupyter``

In all cases, ``JUPYTER_DATA_DIR`` can be used to specify this location
explicitly. Data files installed system-wide (e.g. in
``/usr/local/share/jupyter``) have not changed. Per-user installation of
these has changed from going in .ipython to the above locations:

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

People could use commands like ``ipython notebook --profile demo`` to
set the profile for *both* the notebook server and the IPython kernel.
This is no longer possible in one go with Jupyter, just like it wasn't
possible in IPython 3 for any other kernels. If you wanted to change the
notebook configuration, you can set the ``JUPYTER_CONFIG_DIR``:

::

    JUPYTER_CONFIG_DIR=./jupyter_config jupyter notebook

If you just want to change the config file, you can do:

::

    jupyter notebook --config=/path/to/myconfig.py

If, instead, you do want to change the IPython kernel's profile, you
can't do this at the server command-line anymore. Kernel arguments must
be done by modifying the kernelspec. The good thing about this is that
you can do it without relaunching the server. Kernelspec changes take
effect every time you start a new kernel. The less good thing is that
there isn't a great way to modify the kernelspecs. You can see where the
file is with ``jupyter kernelspec list``, and then modify
``kernels/python3/kernel.json`` by hand.

Installation
------------

I want everything
~~~~~~~~~~~~~~~~~

In IPython 3, to get everything you would type:

::

    pip install "ipython[all]"

In Jupyter, there is a metapackage that means the same thing:

::

    pip install jupyter

Just the notebook, please
~~~~~~~~~~~~~~~~~~~~~~~~~

If you wanted a subset of the functionality, say

::

    pip install "ipython[notebook]"

you would now install the ``notebook`` package:

::

    pip install notebook

Notebook extensions
~~~~~~~~~~~~~~~~~~~

Notebook extensions used to be installed with

::

    ipython install-nbextension [--user] EXTENSION

They are now installed with

::

    jupyter nbextension install [--user] EXTENSION

They will go in the ``JUPYTER_DATA_DIR`` above if a ``--user`` install
is specified, otherwise they will go in a system-wide location (e.g.
``/usr/local/share/jupyter/nbextensions``). Installation **SHOULD NOT**
be done by manually guessing where the files should go.

Kernels
~~~~~~~

Kernels are installed in much the same way as notebook extensions,
above:

Notebook extensions used to be installed with

::

    ipython kernelspec install [--user] KERNEL

They are now installed with

::

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
-  ``IPython.kernel`` → ``jupyter_client``, ``ipykernel`` (this became
   two packages - one for the client-side APIs, one for the IPython
   kernel for Jupyter)
-  ``IPython.parallel`` → ``ipyparallel``
-  ``IPython.qt.console`` → ``qtconsole``
-  ``IPython.utils.traitlets`` → ``traitlets``
-  ``IPython.config`` → ``traitlets.config``
