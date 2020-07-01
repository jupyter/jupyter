.. _install:

====================
Install Instructions
====================
.. contents:: Contents
   :local:
   :depth: 2

This section includes instructions on how to get started with **Jupyter Notebook**.
But there are multiple Jupyter user interfaces one can use, based on their needs.
Please checkout the list and links below for additional information and instructions about
how to get started with each of them.

* **Jupyter Notebook** - *Web-based application for authoring documents that combine
  live-code with narrative text, equations and visualizations.*

  * `GitHub Repo <https://github.com/jupyter/notebook>`_
  * `Docs <https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest>`_

* **JupyterLab** - *The next-generation web-based user interface for Project Jupyter.*

  * `GitHub Repo <https://github.com/jupyterlab/jupyterlab>`_
  * `Docs <https://jupyterlab.readthedocs.io/en/stable/>`_
  * `Install instructions <https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html>`_

* **Jupyter Console** - Terminal based console for interactive computing.

  * `GitHub Repo <https://github.com/jupyter/jupyter_console>`_
  * `Docs and Install instructions <https://jupyter-console.readthedocs.io/en/latest/>`_

* **Jupyter QtConsole** - Qt application for interactive computing with rich output.

  * `GitHub Repo <https://github.com/jupyter/qtconsole>`_
  * `Docs <https://qtconsole.readthedocs.io/en/stable/index.html>`_
  * `Install instructions <https://qtconsole.readthedocs.io/en/stable/installation.html>`_


Installing Jupyter Notebook
===========================

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
   downloading Anaconda's latest Python 3 version (currently Python 3.7).

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

*Optional:* Installing Kernels
==============================

This information gives a high-level view of using Jupyter Notebook with
different programming languages (kernels).

Are any languages pre-installed?
--------------------------------

Yes, installing the Jupyter Notebook will also install the
`IPython <https://ipython.readthedocs.io/en/latest/>`_ :term:`kernel`. This
allows working on notebooks using the Python programming language.

How do I install Python 2 and Python 3?
---------------------------------------

To install an additional version of Python, i.e. to have both Python 2 and 3
available, see the IPython docs on
`installing kernels <https://ipython.readthedocs.io/en/latest/install/kernel_install.html>`_.

How do I install other languages like R or Julia?
-------------------------------------------------

To run notebooks in languages other than Python, such as R or Julia, you will
need to install additional kernels. For more information, see the full
`list of available kernels`_.

.. seealso::

    :ref:`Jupyter Projects <subprojects>`
        Detailed installation instructions for individual Jupyter or IPython
        projects.

    :ref:`Kernels <kernels-langs>`
        Information about additional programming language kernels.

    :ref:`Kernels documentation for Jupyter client <kernels>`
        Technical information about kernels.

.. _`list of available kernels`: https://github.com/jupyter/jupyter/wiki/Jupyter-kernels
