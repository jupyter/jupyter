.. _install:


============
Installation
============

The following is a quick start overview of installing the Jupyter Notebook and
kernels. For detailed installation instructions for individual Jupyter or IPython
subprojects, please see the documentation and/or GitHub repos of the individual
subprojects listed :ref:`here <subprojects>`.

Installing the Jupyter Notebook
-------------------------------

While the Jupyter Notebook allows users to run code in many different
programming language, the Notebook itself is implemented in Python. Thus to
install the Notebook you will also need Python.

.. note::

     All commands shown below must be run in the Terminal (Mac/Linux) or Command
     Prompt (Windows)


If you are new to Python
~~~~~~~~~~~~~~~~~~~~~~~~

If you're new to Python we recommend installing `Anaconda
<http://continuum.io/downloads#py34>`_, which includes Python itself, the Jupyter
Notebook and other packges for scientific computing and data science. After you
install it, ensure that Jupyter is up to date by running the following in the
Terminal (Mac/Linux) or Command Prompt::

    conda update jupyter

You can also use the Anaconda Launcher application to update to the latest
version.

If you already have Python
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you already have Python and are **not** using `conda` or Anaconda, you can install
the Jupyter Notebook using pip::

    pip install jupyter

Upgrading
~~~~~~~~~

The Jupyter Notebook used to be called the IPython Notebook. If you are running
an older version of the IPython Notebook (3 or earlier) you can use the
following to upgrade to the latest version of the Jupyter Notebook.

If the older version of the IPython Notebook was installed using `pip`::

    pip install -U jupyter
    
If the older version of the IPython Notebook was installed using `conda`::

    conda update jupyter

Installing kernels
------------------

Installing the Jupyter Notebook as described above will also install the `IPython
kernel <http://ipython.readthedocs.org/en/master/>`_ for working in the Python programming language.


To run notebooks in languages other than Python, you will need to install
additional kernels. For more information, see the full `list of available kernels
<https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages>`_.

Next steps
----------

After installing you are ready to :ref:`run the notebook <running>`.


