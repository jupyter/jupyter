.. _install:


============
Installation
============

The following is a quick start overview of installing the Jupyter Notebook and kernels. For detailed installation
instructions for individual Jupyter or IPython projects, please see the documentation and/or GitHub repos
of the individual projects listed :ref:`here <landing>`.

Installing the Jupyter Notebook
-------------------------------

While the Jupyter Notebook allows users to run code in many different programming language, the Notebook itself is implemented in Python.

You already have Python
~~~~~~~~~~~~~~~~~~~~~~~

If you already have Python installed and are familiar with installing packages, you can get all of the Jupyter projects, including the Notebook,
with pip::

    pip install jupyter

You are getting started with Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For new users who want to install a full Python environment and the Jupyter Notebook, we suggest installing the Anaconda or Canopy Python distributions, which provide Python 2.7 or 3.4, the Jupyter Notebook with all of its dependencies, as well as a complete set of open source packages for scientific computing and data science.

Download and install Continuum’s Anaconda or the free edition of Enthought’s Canopy.

Update IPython to the current version using the Terminal:

Anaconda::

    conda update conda
    conda update jupyter

Enthought Canopy::

    enpkg ipython

Installing kernels
------------------

To use the Jupyter Notebook, you need to install a kernel for the programming languages you want to use. 