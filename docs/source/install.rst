.. _install:

=========================================
Installing and Upgrading Jupyter Notebook
=========================================

This section explains how to install the Jupyter Notebook and the IPython
kernel.

While Jupyter runs code in many different programming languages, Python is a
prerequisite for installing Jupyter notebook. We recommend using Anaconda
when installing Jupyter since Anaconda supports all major operating systems
and is user friendly.

.. _new-to-python-and-jupyter:

Installing Jupyter and Python using Anaconda (Recommended)
----------------------------------------------------------

**For new users, we highly recommend** `installing Anaconda
<https://www.continuum.io/downloads>`_. Anaconda conveniently
installs:

- Python,
- the Jupyter Notebook, and
- other commonly used packages for scientific computing and data science.

Installation steps
~~~~~~~~~~~~~~~~~~

1. Download `Anaconda <https://www.continuum.io/downloads>`_. We recommend
downloading Anaconda's latest Python 3 version (currently Python 3.5).

2. Install the version of Anaconda which you downloaded.

3. Install Jupyter using `conda` from the Terminal (Mac and Linux) or
CommandPrompt (Windows) to install Jupyter::

.. code-block:: bash

    conda install jupyter

See :ref:`Next Steps <next-steps>` for running the Jupyter Notebook.

.. _existing-anaconda-new-jupyter:

Installing Jupyter if I already have Anaconda Installed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you already have Anaconda installed, install Jupyter using `conda` from
the Terminal (Mac and Linux) or CommandPrompt (Windows) to install Jupyter::

.. code-block:: bash

    conda install jupyter

See :ref:`Next Steps <next-steps>` for running the Jupyter Notebook.

Upgrading Jupyter using Anaconda
--------------------------------
If using **Anaconda**, update Jupyter using `conda`::

.. code-block:: bash

    conda update jupyter

See :ref:`next steps <next-steps>` for running the Jupyter Notebook.


.. _existing-python-new-jupyter:

(Experienced Python Developers) Installing Jupyter with pip
-----------------------------------------------------------

.. important::

    Prerequisite: Jupyter installation requires Python 3.3 or greater, or
    Python 2.7. Older releases of IPython are available
    `here <http://archive.ipython.org/release/>`__.

We recommend Anaconda for installing Jupyter. As an existing Python
user, you may wish to use Python's package manager, :file:`pip`, as an
alternative.

.. _python-using-pip:

Install the Jupyter Notebook using::

.. code-block:: bash

    pip3 install jupyter

(Use :command:`pip` if using legacy Python 2.)

.. note::

    Some of Jupyter's dependencies may require compilation,
    in which case you would need the ability to compile Python C-extensions.
    This means having a C compiler and the Python headers.
    On Debian-based systems (e.g. Ubuntu), you can get this with::

    .. code-block:: bash

        apt-get install build-essential python3-dev

    And on Fedora-based systems (e.g. Red Hat, CentOS)::

    .. code-block:: bash

        yum groupinstall 'Development Tools'
        yum install python3-devel

    (Use ``python`` instead of ``python3`` for legacy Python 2.)

See :ref:`next steps <next-steps>` for running the Jupyter Notebook.

.. _upgrading:

Upgrading IPython Notebook to Jupyter Notebook
----------------------------------------------

The Jupyter Notebook used to be called the IPython Notebook. If you are
running an older version of the IPython Notebook (version 3 or earlier) you
can use the following to upgrade to the latest version of the Jupyter
Notebook.

If using **Anaconda**::

.. code-block:: bash

    conda update jupyter

*or*

If using :command:`pip`::

.. code-block:: bash

    pip install -U jupyter

See :ref:`next steps <next-steps>` for running the Jupyter Notebook.

.. seealso::

    The :doc:`migrating` document has additional
    information about migrating from IPython 3 to Jupyter.

.. _next-steps:

Next steps
----------

Congratulations. You have installed Jupyter Notebook and are ready to
:ref:`Run the Notebook <running>`.

.. _installing-kernels:

(Optional) Installing Kernels
-----------------------------

Installing the Jupyter Notebook as described above will also install the
`IPython <https://ipython.readthedocs.io/en/latest/>`_ :term:`kernel` which
allows working on notebooks using the Python programming language.

To run notebooks in languages other than Python, you will need to install
additional kernels. For more information, see the full `list of available kernels
<https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages>`_.

To install extra Python kernels, to make both Python 2 and 3 available in
Jupyter, or to set up kernels in environments, see `the IPython docs on
installing kernels <https://ipython.readthedocs.io/en/latest/install/kernel_install.html>`__.

.. seealso::

    For detailed installation instructions for individual Jupyter or IPython
    subprojects, see the :ref:`Jupyter Subprojects <subprojects>`
    document.