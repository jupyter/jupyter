.. _install:


============
Installation
============

The following is a quick start overview of installing the Jupyter Notebook and kernels. For detailed installation
instructions for individual Jupyter or IPython projects, please see the documentation and/or GitHub repos
of the individual projects listed :ref:`here <landing>`.

Installing the Jupyter Notebook
-------------------------------

.. note::

   We're still in the process of releasing Jupyter, and these instructions are
   being prepared for when it is released. In the meantime, we recommend
   `installing IPython 3 <http://ipython.org/install.html>`_ to use the notebook.

While the Jupyter Notebook allows users to run code in many different programming language, the Notebook itself is implemented in Python.

**If you already have Python**, you can install the notebook using pip::

    pip install jupyter


**If you're new to Python**, we recommend installing `Anaconda
<http://continuum.io/downloads#py34>`_, a Python distribution which includes
Jupyter. After you install it, ensure that Jupyter is up to date by running::

    conda update jupyter

To **upgrade from IPython 3 or older to Jupyter**, use pip or conda—according
to which one IPython was installed with—to install the ``jupyter`` package. This
should install the Jupyter Notebook and upgrade IPython to version 4.

Installing kernels
------------------

Installing the Jupyter Notebook should also have installed the `IPython kernel
<http://ipython.readthedocs.org/en/master/>`_ for the Python programming language.

To run notebooks in other languages, you'll need to install additional kernels:
see the `list of available kernels
<https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages>`_.
