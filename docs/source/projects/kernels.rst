.. _kernels-langs:

===============================
Kernels (Programming Languages)
===============================

The Jupyter team maintains the `IPython <https://github.com/ipython/ipython>`_
project which is shipped as a default kernel (as :term:`ipykernel`) in a number of Jupyter clients.
Many other languages, in addition to Python, may be used in the notebook.

The community maintains many other language kernels, and new kernels become
available often. Please see the `list of available kernels`_ for additional
languages and `kernel installation instructions`_ to begin using these
language kernels.

Kernels
-------

Kernels are `programming language specific` processes that run independently
and interact with the Jupyter Applications and their user interfaces.
`ipykernel <https://github.com/ipython/ipykernel>`__ is the reference Jupyter kernel
is the reference Jupyter kernel built on top of `IPython <https://ipython.org>`__,
providing a powerful environment for interactive computing in Python.

`jupyter-client <https://jupyter-client.readthedocs.io/en/stable/>`__ contains
the authoritative description of the Jupyter messaging protocol which is used
by clients to communicate with the kernels.

`Xeus <https://ipyparallel.readthedocs.io/en/latest/>`__ subproject facilitates
implementation of kernels for Jupyter and provides a number of kernels such as
`xeus-cling <https://github.com/jupyter-xeus/xeus-cling>`__ (C++),
`xeus-sql <https://github.com/jupyter-xeus/xeus-sql>`__ (SQL) and many more.

.. glossary::

    `IPython <https://ipython.org>`__
        interactive computing in Python - 
        `Documentation <https://ipython.readthedocs.io/en/stable/>`__ |
        `Repo <https://github.com/ipython/ipykernel>`__

    `ipykernel <ipykernel>`__
        the wrapper around IPython which enables using IPython as a kernel
        `Repo <https://github.com/ipython/ipython>`__

    `Xeus <https://ipyparallel.readthedocs.io/en/latest/>`__
        library facilitating the implementation of kernels for Jupyter
        It implements the Jupyter Kernel protocol so developers
        can focus on implementing the interpreter part of the kernel.
        `Documentation <https://xeus.readthedocs.io/en/latest/>`__ |
        `Repo <https://github.com/jupyter-xeus/xeus>`__

    `ipywidgets <https://ipywidgets.readthedocs.io/en/latest/>`__
        interactive widgets for Python in the Jupyter Notebook.
        `Documentation <https://ipywidgets.readthedocs.io/en/latest/>`__ |
        `Repo <https://github.com/ipython/ipywidgets>`__

    `ipyparallel <https://ipyparallel.readthedocs.io/en/latest/>`__
        lightweight parallel computing in Python offering seamless notebook integration.
        `Documentation <https://ipyparallel.readthedocs.io/en/latest/>`__ |
        `Repo <https://github.com/ipython/ipyparallel>`__

.. seealso::

      `Jupyter kernels <list of available kernels_>`_

      A full list of kernels available for other languages. Many of
      these kernels are developed by third parties and may or may not be stable.

.. _list of available kernels: https://github.com/jupyter/jupyter/wiki/Jupyter-kernels

.. _kernel installation instructions: https://ipython.readthedocs.io/en/latest/install/kernel_install.html
