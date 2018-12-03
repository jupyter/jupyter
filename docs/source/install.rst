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
the Jupyter Notebook.

We recommend using the `Anaconda <https://www.anaconda.com/download>`_
distribution to install Python and Jupyter. We'll go through its installation
in the next section.

.. _new-to-python-and-jupyter:

Installing Jupyter using Anaconda and conda
-------------------------------------------

For new users, we **highly recommend** `installing Anaconda
<https://www.anaconda.com/download>`_. Anaconda conveniently
installs Python, the Jupyter Notebook, and other commonly used packages for
scientific computing and data science.

Use the following installation steps:

1. Download `Anaconda <https://www.anaconda.com/download>`_. We recommend
   downloading Anaconda's latest Python 3 version (currently Python 3.5).

2. Install the version of Anaconda which you downloaded, following the
   instructions on the download page.

3. Congratulations, you have installed Jupyter Notebook. To run the notebook:

   .. code-block:: bash

       jupyter notebook

   See :ref:`Running the Notebook <running>` for more details.

.. _existing-python-new-jupyter:

*Alternative for experienced Python users:* Installing Jupyter with pip
-----------------------------------------------------------------------

.. important::

    Jupyter installation requires Python 3.3 or greater, or
    Python 2.7. IPython 1.x, which included the parts that later became Jupyter,
    was the last version to support Python 3.2 and 2.6.

As an existing Python user, you may wish to install Jupyter using Python's
package manager, :term:`pip`, instead of Anaconda.

.. _python-using-pip:

First, ensure that you have the latest pip;
older versions may have trouble with some dependencies:

.. code-block:: bash

    pip3 install --upgrade pip

Then install the Jupyter Notebook using:

.. code-block:: bash

    pip3 install jupyter

(Use ``pip`` if using legacy Python 2.)

Congratulations. You have installed Jupyter Notebook. See
:ref:`Running the Notebook <running>` for more details.
