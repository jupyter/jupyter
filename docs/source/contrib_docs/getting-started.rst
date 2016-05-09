Getting started
===============

.. contents::
   :local:

Preparing for your first contribution
-------------------------------------
1. Our documentation uses reStructured Text as well as Jupyter notebooks.
2. We use Sphinx extensively to build documentation.
3. We host our documentation on Read the Docs.

Developing your contribution
----------------------------

Clone the repository
~~~~~~~~~~~~~~~~~~~~
1. Fork the project repository found on GitHub.
2. Clone the repository to your system.

Edit the documentation source file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Source files for projects are typically found in the project's ``docs/source``
directory. The reStructured text filenames end with ``.rst``, and Jupyter
notebook files end with ``.ipynb``.

1. In your favorite text editor, make desired changes to the ``.rst`` file when
   working with a reStructured text source file.
2. If a notebook file requires editing, you will need to install Jupyter
   notebook according to the :ref:`Installation <install>` document. Then,
   run the Jupyter notebook and edit the desired file. Before saving the
   Jupyter ``.ipynb`` file, please clear the output cells. Save the file and
   test your change.

Testing changes
---------------

Sphinx should be installed to test your documentation changes. For best results,
we recommend that you install the stable development version Sphinx
(``pip install git+https://github.com/sphinx-doc/sphinx@stable``) or the
current released version of Sphinx (``pip install sphinx``).

In addition, you may need the following packages: sphinxcontrib-spelling, sphinx_rtd_theme, and pyenchant, which can be installed via ``pip install sphinxcontrib-spelling sphinx_rtd_theme pyenchant``.

If you are on Linux, you may also need to install the Enchant C library by running ``sudo apt-get install enchant``.

Once everything is installed, the following commands should be executed using the Terminal/command line from
the ``docs`` directory:

* ``make html`` builds a local html version of the documentation. The output
  message will either display errors or provide the location of the html documents.
  For example, the location provided may be ``build/html`` and to view these
  documents in your browser enter ``open build/html/index.html``.

* ``make linkcheck`` will check whether the external links in the
  documentation are valid or if they are not longer current (i.e. cause a 500
  not found error).

Note: We recommend using Python 3.4+ for building the documentation. If you are editing the documentation, you can use Python 2.7.9+ or the Github editor. 

Creating a pull request
-----------------------
Once you are satisfied with your changes, submit a GitHub pull request, per 
the instructions above. If the documentation change is related to an open 
GitHub issue, please mention the issue number in the pull request message.

A project reviewer will look over your changes and provide feedback or merge
your changes into the documentation.

Asking questions
----------------
Feel free to ask questions in the Google Group for Jupyter or on an open issue
on GitHub.



