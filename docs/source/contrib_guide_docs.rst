=================================
Contributing to the Documentation
=================================

Documentation helps guide new users, foster communication between developers,
and share tips and best practices with other community members. That's why
the Jupyter project is focused on documenting new features and to keeping
the rest of the documentation up-to-date.

**This guide is under active development.**

Preparing for your first contribution
-------------------------------------
1. Our documentation uses reStructured Text as well as Jupyter notebooks.
2. We use Sphinx extensively to build documentation.
3. We host our documentation on Read the Docs.

Your first contribution
-----------------------

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

Test documentation changes
~~~~~~~~~~~~~~~~~~~~~~~~~~

Sphinx should be installed to test your documentation changes. For best results,
we recommend that you install the stable development version Sphinx
(``pip install git+https://github.com/sphinx-doc/sphinx@stable``) or the
current released version of Sphinx (``pip install sphinx``).

The following commands should be executed using the Terminal/command line from
the ``docs` directory:

* ``make html`` builds a local html version of the documentation. The output
  message will either display errors or provide the location of the html documents.
  For example, the location provided may be ``build/html`` and to view these
  documents in your browser enter ``open build/html/index.html``.

* ``make linkcheck`` will check whether the external links in the
  documentation are valid or if they are not longer current (i.e. cause a 500
  not found error).

Create a pull request
~~~~~~~~~~~~~~~~~~~~~
Once you are satisfied with your changes, submit a GitHub pull request, per 
the instructions above. If the documentation change is related to an open 
GitHub issue, please mention the issue number in the pull request message.

A project reviewer will look over your changes and provide feedback or merge
your changes into the documentation.

Questions
---------
Feel free to ask questions in the Google Group for Jupyter or on an open issue
on GitHub.

=========================
Git and Github Resources
=========================

If this is your first time working with Github or git, you can leverage the following
resources to learn about the tools.

* `Try Git  <https://try.github.io>`_
* `Github Guides  <https://guides.github.com>`_
* `Git Real  <https://www.codeschool.com/courses/git-real>`_

