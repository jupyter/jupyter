.. _install:


============
Installation
============

These installation instructions explain how to install the Jupyter Notebook and
the IPython kernel.

While Jupyter allows users to run code in many different
programming languages, the Jupyter Notebook itself is implemented in Python.
To install Jupyter Notebook, you will also need Python installed on your system.

**Installation Scenarios**

* :ref:`New user: New to Python and Jupyter <new-to-python-and-jupyter>`
* :ref:`Experienced Python user: New to Jupyter <existing-python-new-jupyter>`
* :ref:`Upgrading Jupyter <upgrading>`

.. note::

     All commands shown below must be run in the Terminal (Mac/Linux) or Command
     Prompt (Windows)

.. _new-to-python-and-jupyter:

New Users: New to Python and Jupyter
------------------------------------

If you're new to Python, we highly recommend `installing Anaconda
<https://www.continuum.io/downloads>`_. Anaconda includes and conveniently
installs Python, the Jupyter Notebook, and other commonly used packages for
scientific computing and data science. Follow Anaconda's instructions for
downloading the Python 3.5 version.

After you have Anaconda installed, you should make sure that Jupyter is up to
date. Run the following command in the Terminal (Mac/Linux) or Command
Prompt (Windows)::

    conda install jupyter

Alternatively, you may also use the Anaconda Launcher application to update to
the latest version.

Now, you may consider :ref:`installing additional kernels <installing-kernels>`
and :ref:`next steps <next-steps>` such as running the Jupyter Notebook.


.. _existing-python-new-jupyter:

Experienced Python user: New to Jupyter
---------------------------------------

.. important::

    **Jupyter installation requires Python 3.3 or greater, or Python 2.7.**

    If you need to use Python 2.6 or 3.2, you may install
    `IPython 1.2 <http://archive.ipython.org/release/1.2.0/>`_.
    Older releases of IPython are available `here <http://archive.ipython.org/release/>`__.

As an existing Python user, you may have installed Python from the Python website,
a system package manager, or using Anaconda. The command for installing Jupyter
Notebook is slightly different depending on how you installed Python. Depending on
whether or not you use Anaconda, follow one of these two instructions to install
Jupyter on your system.


.. _existing-anaconda-new-jupyter:

Anaconda and conda users
^^^^^^^^^^^^^^^^^^^^^^^^

If you have Anaconda installed, run the following command in the Terminal
(Mac/Linux) or CommandPrompt (Windows) to install Jupyter::

    conda install jupyter

Now, you may consider :ref:`installing kernels <installing-kernels>` and
:ref:`next steps <next-steps>`.


.. _python-using-pip:

pip users
^^^^^^^^^

If you already have Python installed and are **not** using `conda` or Anaconda,
you may install the Jupyter Notebook using Python's package manager `pip`::

    pip3 install jupyter

(*Use ``pip`` instead of ``pip3`` for legacy Python 2*)

.. note::

    Some of Jupyter's dependencies may require compilation,
    in which case you would need the ability to compile Python C-extensions.
    This means a C compiler and the Python headers.
    On Debian-based systems (e.g. Ubuntu), you can get this with::

        apt-get install build-essential python3-dev

    And on Fedora-based systems (e.g. Red Hat, CentOS)::

        yum groupinstall 'Development Tools'
        yum install python3-devel

    (Use ``python`` instead of ``python3`` for legacy Python 2)


Now, you may consider :ref:`installing kernels <installing-kernels>` and
:ref:`next steps <next-steps>`.


.. _upgrading:

Upgrading to Jupyter: Experienced Users
---------------------------------------

The Jupyter Notebook used to be called the IPython Notebook. If you are running
an older version of the IPython Notebook (version 3 or earlier) you can use the
following to upgrade to the latest version of the Jupyter Notebook.

**If using 'pip'**::

    pip install -U jupyter

OR

**If using Anaconda or `conda`**::

    conda update jupyter

.. seealso::

    The :ref:`Migrating from IPython <migrating>` document has additional
    information about migrating from IPython 3 to Jupyter.


.. _installing-kernels:

Installing kernels
------------------

Installing the Jupyter Notebook as described above will also install the `IPython
kernel <http://ipython.readthedocs.org/en/master/>`_ which allows working on
notebooks using the Python programming language.

To run notebooks in languages other than Python, you will need to install
additional kernels. For more information, see the full `list of available kernels
<https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages>`_.


.. _next-steps:

Next steps
----------

Congratulations. You have installed Jupyter Notebook and are ready to
:ref:`run the notebook <running>`.


.. seealso::

    For detailed installation instructions for individual Jupyter or IPython
    subprojects, please see the documentation or GitHub repos of the
    individual subprojects listed in :ref:`Jupyter Subprojects <subprojects>`
    document.
