.. _quickstart:

==========
Quickstart
==========

Try Jupyter without Installing
------------------------------
Would you like to try Jupyter in your web browser? You may try out the current
version of Jupyter Notebook in your browser.

**Try Jupyter Notebook**
https://try.jupyter.org


Installing Jupyter for New Users
--------------------------------
If you are new to Jupyter, we highly recommend reading and using our detailed
:ref:`installation guide <install>`.


Quickstart for Experienced Users
--------------------------------

Jupyter and Anaconda
~~~~~~~~~~~~~~~~~~~~

1. Install `Anaconda <http://continuum.io/downloads>`_ following Anaconda's
   instructions.

2. Run the following command in the Terminal (Mac/Linux) or Command
   Prompt (Windows)::

    conda install jupyter

3. Start Jupyter::

    jupyter notebook


Jupyter and Python's pip
^^^^^^^^^^^^^^^^^^^^^^^^

1. If you already have Python installed and are **not** using `conda` or Anaconda,
   install the Jupyter Notebook using Python's package manager `pip`::

    pip install jupyter

3. Start Jupyter::

    jupyter notebook


Existing IPython Notebook users upgrading to Jupyter Notebook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the older version of the IPython Notebook was installed using `pip`,
upgrade using::

    pip install -U jupyter

If the older version of the IPython Notebook was installed using `conda` or
Anaconda, upgrade using::

    conda update jupyter

The :ref:`Migrating from IPython <migrating>` document gives additional
information about migrating from IPython 3 to Jupyter.


Start Jupyter::

    jupyter notebook
