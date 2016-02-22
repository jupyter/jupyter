.. _running:


====================
Running the Notebook
====================

After you have installed the Jupyter Notebook on your computer, you are ready to run the Notebook. You can start the notebook server from the command line (Terminal on Mac/Linux, CMD prompt on Windows) by running the following command::

    jupyter notebook

This will print some information about the notebook server in your terminal,
including the URL of the web application (by default, ``http://127.0.0.1:8888``).
It will then open your default web browser to this URL.

When the notebook opens, you will see the notebook dashboard, which will show a list of the notebooks, files, and subdirectories in the directory where the notebook server was started (as seen in the next section, below). Most of the time, you will want to start a notebook server in the highest directory in your filesystem where notebooks can be found. Often this will be your home directory.

====================
Additional options
====================

By default, the notebook server starts on port 8888. If port 8888 is unavailable, the notebook server searches the next available port.
You can also specify the port manually::

    jupyter notebook --port 9999

Or start notebook server without opening a web browser::
    
    jupyter notebook --no-browser

The notebook server has a number of other command line arguments that can be displayed with the --help flag::
    
    jupyter notebook --help
