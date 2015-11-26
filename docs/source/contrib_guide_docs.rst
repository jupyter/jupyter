========================================
Submitting a Bug or Enhancement Request
========================================
While using the Notebook, you might experience a bug or discover room for a 
potential enhancement. If so, we encourage you to open issues on Github.
To make the navigating issues eaasier for both developers and users, we ask
that you take the following steps before submitting an issue.

1. Search through StackOverflow and existing Github issues to ensure that 
the issue has not already been reported by another user. If so, provide
your input on the existing issue if you think it would be valuable.

2. Prepare a small, self-contained snippet of code that will allow others
to reproduce the issue that you are experiencing.

3. Prepare information about the environment that you are executing the code
in, in order to aid in the debugging of the issue. You can use ``python 
-c "import IPython; print(IPython.sys_info())"`` to get some initial
information about the environment. You can also use ``pip list`` or 
``conda list`` and ``grep`` in order to identify the versions of the
libraries that are relevant to the issue that you are submitting.

4. Prepare a simple test that outlines the expected behavior of the code.

5. Prepare an explanation of why the current behavior is not desired and 
what it should be.


==================================
Contributing to the Python Backend
==================================

How can I help?
---------------
Individuals are welcome, and encourage, to submit issues, enhancements, and
new idea to the codebase. If you are a first-time contributor looking to get
involved with Jupyter, you can use the following query in a Github search to
find beginner-friendly issues to tackle across the Jupyter codebase.

**is:issue is:open is:sprint-friendly user:jupyter**

Once you've found an issue that you are eager to solve, you can use the guide
below to get started. If you experience any issues while working on the issue,
you can contact the mailing list or the approrpiate Gitter channel.

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
Once you are satisfied with your changes, submit a GitHub pull request. If the
documentation change is related to an open GitHub issue, please mention the
issue number in the pull request message.

A project reviewer will look over your changes and provide feedback or merge
your changes into the documentation.

Questions
---------
Feel free to ask questions in the Google Group for Jupyter or on an open issue
on GitHub.


