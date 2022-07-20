.. _running:

====================
Running the Notebook
====================

.. contents:: Contents
   :local:
   :depth: 2

Basic Steps
-----------

1. Start the notebook server from the :term:`command line`::

    jupyter notebook

2. You should see the notebook open in your browser.

Starting the Notebook Server
----------------------------

After you have installed the Jupyter Notebook on your computer, you are ready
to run the notebook server. You can start the notebook server from the
:term:`command line` (using :term:`Terminal` on Mac/Linux,
:term:`Command Prompt` on Windows) by running::

    jupyter notebook

This will print some information about the notebook server in your terminal,
including the URL of the web application
(by default, ``http://localhost:8888``):

.. code:: bash

    $ jupyter notebook
    [I 08:58:24.417 NotebookApp] Serving notebooks from local directory: /Users/catherine
    [I 08:58:24.417 NotebookApp] 0 active kernels
    [I 08:58:24.417 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/
    [I 08:58:24.417 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).

It will then open your default web browser to this URL.

When the notebook opens in your browser, you will see the :term:`Notebook Dashboard`,
which will show a list of the notebooks, files, and subdirectories in the
directory where the notebook server was started. Most of the time, you will
wish to start a notebook server in the highest level directory containing
notebooks. Often this will be your home directory.

**Notebook Dashboard**

 .. Alt text is intentionally left blank because the image content is described thoroughly in the surrounding text.

.. image:: _static/_images/tryjupyter_file.png
    :alt: 

Introducing the Notebook Server's Command Line Options
------------------------------------------------------

How do I open a specific Notebook?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following code should open the given notebook in the currently running notebook server, starting one if necessary. 

.. code:: bash

    jupyter notebook notebook.ipynb

How do I start the Notebook using a custom IP or port?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the notebook server starts on port 8888. If port 8888 is
unavailable or in use, the notebook server searches the next available port.
You may also specify a port manually. In this example, we set the server's
port to 9999:

.. code:: bash

    jupyter notebook --port 9999

How do I start the Notebook server without opening a browser?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start notebook server without opening a web browser:

.. code:: bash

    jupyter notebook --no-browser

How do I get help about Notebook server options?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The notebook server provides help messages for other command line arguments
using the ``--help`` flag:

.. code:: bash

    jupyter notebook --help

.. seealso::

   :ref:`Jupyter Installation, Configuration, and Usage <content-projects>`
        Detailed information about command line arguments, configuration, and usage.

Using a command-line interface
------------------------------

Notebooks can be executed from your terminal using the ``run`` subcommand. It expects notebook paths as input arguments and accepts optional flags to modify the default behavior.

Running a notebook is this easy.

.. code:: bash

    jupyter run notebook.ipynb

You can pass more than one notebook as well.

.. code:: bash

    jupyter run notebook.ipynb notebook2.ipynb

By default, notebook errors will be raised and printed into the terminal. You can suppress them by passing the ``--allow-errors`` flag.

.. code:: bash

    jupyter run notebook.ipynb --allow-errors

For more sophisticated execution options, consider the `papermill <https://pypi.org/project/papermill/>`_ library.
