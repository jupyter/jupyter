.. _install:

============
Installation
============

This section explains how to install the Jupyter Notebook and the IPython
kernel.

While Jupyter runs code in many different programming languages, Python is a
prerequisite for installing Jupyter notebook. Select one of the following
scenarios to install Jupyter:

- **Recommended:** :ref:`Installing Jupyter and Python <new-to-python-and-jupyter>`
- :ref:`Installing Jupyter (experienced Python developers) <existing-python-new-jupyter>`
- :ref:`Upgrading a Jupyter installation <upgrading>`

.. _new-to-python-and-jupyter:

Installing Jupyter and Python
-----------------------------

**For new users, we highly recommend** `installing Anaconda
<https://www.continuum.io/downloads>`_. Anaconda conveniently
installs:

- Python, 
- the Jupyter Notebook, and 
- other commonly used packages for scientific computing and data science. 

Follow Anaconda's instructions for downloading and installing the Python 3.5
version.

See :ref:`next steps <next-steps>` for running the Jupyter Notebook.

.. _existing-python-new-jupyter:

Installing Jupyter (experienced Python developers)
--------------------------------------------------

.. important::

    Prerequisite: Jupyter installation requires Python 3.3 or greater, or
    Python 2.7. Older releases of IPython are available
    `here <http://archive.ipython.org/release/>`__.

As an existing Python user, you may have installed Python from the Python
website, a system package manager, or using Anaconda. The command for
installing Jupyter Notebook is slightly different depending on how you
installed Python. Depending on whether you prefer Anaconda or pip, select the
relevant instructions below to install Jupyter on your system. We recommend
installation of Anaconda. 

.. _existing-anaconda-new-jupyter:

Using Anaconda and conda (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once `Anaconda <https://www.continuum.io/downloads>`_ is installed, run the
following command in the Terminal (Mac and Linux) or CommandPrompt (Windows)
to install Jupyter:

.. code-block:: bash

    conda install jupyter

See :ref:`next steps <next-steps>` for running the Jupyter Notebook.

.. _python-using-pip:

Using pip
~~~~~~~~~

If you already have Python installed and are **not** using conda or Anaconda,
you may install the Jupyter Notebook using Python's package manager,
:file:`pip`:

.. code-block:: bash

    pip3 install jupyter

(Use :command:`pip` for legacy Python 2 instead of :command:`pip3`.)

.. note::

    Some of Jupyter's dependencies may require compilation,
    in which case you would need the ability to compile Python C-extensions.
    This means a C compiler and the Python headers.
    On Debian-based systems (e.g. Ubuntu), you can get this with:
    
    .. code-block:: bash

        apt-get install build-essential python3-dev

    And on Fedora-based systems (e.g. Red Hat, CentOS):
    
    .. code-block:: bash

        yum groupinstall 'Development Tools'
        yum install python3-devel

    (Use ``python`` instead of ``python3`` for legacy Python 2.)

See :ref:`next steps <next-steps>` for running the Jupyter Notebook.

.. _upgrading:

Upgrading a Jupyter installation
--------------------------------

The Jupyter Notebook used to be called the IPython Notebook. If you are 
running an older version of the IPython Notebook (version 3 or earlier) you
can use the following to upgrade to the latest version of the Jupyter
Notebook.

If using :command:`pip`: 

.. code-block:: bash

    pip install -U jupyter

*or*

If using **Anaconda**:

.. code-block:: bash

    conda update jupyter

See :ref:`next steps <next-steps>` for running the Jupyter Notebook.

.. seealso::
    
    The :doc:`migrating` document has additional
    information about migrating from IPython 3 to Jupyter.

.. _next-steps:

Next steps
----------

Congratulations. You have installed Jupyter Notebook and are ready to
:ref:`run the notebook <running>`.

.. _installing-kernels:

Installing kernels (optional)
-----------------------------

Installing the Jupyter Notebook as described above will also install the `IPython
kernel <https://ipython.readthedocs.org/en/latest/>`_ which allows working on
notebooks using the Python programming language.

To run notebooks in languages other than Python, you will need to install
additional kernels. For more information, see the full `list of available kernels
<https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages>`_.

To install extra Python kernels—to make both Python 2 and 3 available in
Jupyter, or to set up kernels in environments—see `the IPython docs on
installing kernels <https://ipython.readthedocs.org/en/latest/install/kernel_install.html>`__.

.. seealso::

    For detailed installation instructions for individual Jupyter or IPython
    subprojects, see the :ref:`Jupyter Subprojects <subprojects>`
    document.