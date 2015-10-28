.. _install:


============
Installation
============

Jupyter requires Python 2.7 or ≥ 3.3.

.. note::

    If you need to use Python 2.6 or 3.2, you can find IPython 1.2
    `here <http://archive.ipython.org/release/>`__.

This document will get you up and running with the the Jupyter Notebook.

These installation instructions explain how to install the Jupyter Notebook and
the IPython kernel.

.. seealso::

    For detailed installation instructions for individual Jupyter or IPython
    subprojects, please see the documentation or GitHub repos of the
    individual subprojects listed in :ref:`Jupyter Subprojects <subprojects>`
    document.


How to Install Jupyter Notebook
-------------------------------

While the Jupyter Notebook allows users to run code in many different
programming languages, the Jupyter Notebook itself is implemented in Python.
To install Jupyter Notebook, you will also need Python installed on your system.


**Installation Scenarios**

* :ref:`New to Python and Jupyter <new-to-python-and-jupyter>`
* :ref:`Existing Python user and new to Jupyter <existing-python-new-jupyter>`
* :ref:`Existing IPython Notebook user upgrading to Jupyter <existing-upgrading>`


.. note::

     All commands shown below must be run in the Terminal (Mac/Linux) or Command
     Prompt (Windows)

.. _new-to-python-and-jupyter:

If you are new to Python and Jupyter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're new to Python, we highly recommend installing `Anaconda
<http://continuum.io/downloads>`_. Anaconda includes and conveniently
installs Python, the Jupyter Notebook, and other commonly used packages for
scientific computing and data science. Follow Anaconda's instructions for
downloading the Python 3.4 version. You may need to click on the "I want
Python 3.4" link to download Anaconda for Python 3.4.

After you have Anaconda installed, you should make sure that Jupyter is up to
date. Run the following command in the Terminal (Mac/Linux) or Command
Prompt (Windows)::

    conda install jupyter

Alternatively, you may also use the Anaconda Launcher application to update to
the latest version.

Now, you may consider :ref:`installing additional kernels <installing-kernels>`
and :ref:`next steps <next-steps>` such as running the Jupyter Notebook.


.. _existing-python-new-jupyter:

If you are an existing Python user but new to Jupyter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As an existing Python user, you may have installed Python from the Python website,
a system package manager, or using Anaconda. The command for installing Jupyter
Notebook is slightly different depending on how you installed Python. Depending on
whether or not you use Anaconda, follow one of these two instructions to install
Jupyter on your system.


.. _existing-anaconda-new-jupyter:

If you use Python with Anaconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have Anaconda installed but have not yet installed or used Jupyter, you
should run the following command in the Terminal (Mac/Linux) or Command
Prompt (Windows) to install Jupyter::

    conda install jupyter

Now, you may consider :ref:`installing kernels <installing-kernels>` and
:ref:`next steps <next-steps>`.


.. _python-not-using-Anaconda:

If you use Python but do not use Anaconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


.. _existing-upgrading:

Existing IPython Notebook users upgrading to Jupyter Notebook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Jupyter Notebook used to be called the IPython Notebook. If you are running
an older version of the IPython Notebook (version 3 or earlier) you can use the
following to upgrade to the latest version of the Jupyter Notebook.

If the older version of the IPython Notebook was installed using `pip`,
upgrade using::

    pip install -U jupyter

If the older version of the IPython Notebook was installed using `conda` or Anaconda,
upgrade using::

    conda install jupyter


The :ref:`Migrating from IPython <migrating>` document gives additional information
about migrating from IPython 3 to Jupyter.


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


