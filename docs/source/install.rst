.. _install:

===========================
Installing Jupyter Notebook
===========================

.. contents:: Contents
   :local:
   :depth: 2

This information explains how to install the Jupyter Notebook and the IPython
kernel.

Prerequisite: Python
--------------------

While Jupyter runs code in many programming languages, **Python** is
a requirement (Python 3.3 or greater, or Python 2.7) for installing
Jupyter notebook.

We recommend using the `Anaconda <https://www.continuum.io/downloads>`_
distribution to install Python and Jupyter. We'll go through its installation
in the next section.

.. _new-to-python-and-jupyter:

Installing Jupyter using Anaconda and conda
-------------------------------------------

For new users, we **highly recommend** `installing Anaconda
<https://www.continuum.io/downloads>`_. Anaconda conveniently
installs Python, the Jupyter Notebook, and other commonly used packages for
scientific computing and data science.

Use the following installation steps:

1. Download `Anaconda <https://www.continuum.io/downloads>`_. We recommend
   downloading Anaconda's latest Python 3 version (currently Python 3.5).

2. Install the version of Anaconda, which you downloaded.

3. Congratulations, you have installed Jupyter Notebook. To run the notebook:

   .. code-block:: bash

       jupyter notebook

   See :ref:`Running the Notebook <running>` for more details.

.. _existing-python-new-jupyter:

*Optional for experienced Python developers:* Installing Jupyter with pip
-------------------------------------------------------------------------

.. important::

    Jupyter installation requires Python 3.3 or greater, or
    Python 2.7. Older releases of IPython are available
    `here <http://archive.ipython.org/release/>`__.

We recommend Anaconda for installing Jupyter. Though as an existing Python
user, you may wish to use Python's package manager, :term:`pip`, as an
alternative.

.. _python-using-pip:

Install the Jupyter Notebook using:

.. code-block:: bash

    pip3 install jupyter
    

On Linux/Ubuntu, you may need to install Jupyter with sudo privilegs.
.. code-block:: bash

    sudo pip install jupyter

(Use ``pip`` if using legacy Python 2.)

.. note::

    Some of Jupyter's dependencies may require compilation,
    in which case you would need the ability to compile Python C-extensions.
    You will need a C compiler and the Python headers.
    On Debian-based systems (e.g. Ubuntu), you can get this with:

    .. code-block:: bash

        apt-get install build-essential python3-dev

    And on Fedora-based systems (e.g. Red Hat, CentOS):

    .. code-block:: bash

        yum groupinstall 'Development Tools'
        yum install python3-devel

    (Use ``python`` for legacy Python 2.)

Congratulations. You have installed Jupyter Notebook. See
:ref:`Running the Notebook <running>` for more details.
