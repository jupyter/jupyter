Getting started
===============

.. contents:: Contents
   :local:

Preparing for your first contribution
-------------------------------------
1. Our documentation uses reStructured Text, Markdown, and Jupyter notebooks.
2. We use Sphinx extensively to build documentation.
3. We use Transifex to help translate documentation to multiple languages.
4. We host our documentation on Read the Docs.

Developing your contribution
----------------------------

Jupyter's documentation is split across several projects, listed on the `Jupyter documentation home page <https://jupyter.readthedocs.io/en/latest/>`_. These instructions apply to all Jupyter projects, though some projects have further contribution guidelines.

Clone the repository
~~~~~~~~~~~~~~~~~~~~
1. Fork the appropriate project repository on GitHub, depending on which project's documentation you want to contribute to.
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

In addition, you may need the following packages: sphinxcontrib-spelling, sphinx_rtd_theme, nbsphinx, pyenchant, recommonmark 0.4.0 and jupyter_sphinx_theme, which can be installed via ``pip install sphinxcontrib-spelling sphinx_rtd_theme nbsphinx pyenchant recommonmark==0.4.0 jupyter_sphinx_theme``.

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



