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
Contributing to the Code
==================================

How can I help?
---------------
Individuals are welcome, and encouraged, to submit issues, enhancements, and
new idea to the codebase. If you are a first-time contributor looking to get
involved with Jupyter, you can use the following query in a Github search to
find beginner-friendly issues to tackle across the Jupyter codebase.

**is:issue is:open is:sprint-friendly user:jupyter**

Once you've found an issue that you are eager to solve, you can use the guide
below to get started. If you experience any issues while working on the issue,
you can contact the mailing list or the approrpiate Gitter channel.

1. Fork the repository associated with the issue you are addressing and clone
it to a local directory on your machine.

2. ``cd`` into the directory and create a new branch using ``git checkout -b
insert-branch-name-here``. Pick a branch name that gives some insight into
what the issue you are fixing is. For example, if you are updating the text
that is logged out by the program when a certain error happens you might 
name your branch `update-error-text`.

3. Reference the README of the repository you have forked and cloned for
information about how to set up the repository in development mode.

4. Identify the module or class where the code change you will make will
reside and find the test file associated with this code change. In the test
file, add some tests that outline what you expect the behavior of the change
should be. If we continue with our example of updating the text that is logged
on error, we might write test cases that check to see if the exception raised
when you induce the error contains the appropriate string. When writing test
cases, make sure that you test for the following things.

* What is the simplest test case I can write for this issue?
* What will happen if your code is given messy inputs?
* What will happen if your code is given no inputs?
* What will happen if your code is given too few inputs?
* What will happen if your code is given too many inputs?

5. Once you have created some test cases, refer to the README of the repository
that you forked and cloned for information about how to run the test suite. This
will typical require that you run the ``nosetests`` command at the commandline.
Observe that when you run the tests, the new tests that you added will fail as you
have no updated the code yet.

6. Go back to the file that you are updating and begin adding the code for your
pull request.

7. Run the test suite again to see if your changes have caused any of the test
cases to pass. If any of the test cases have failed, go back to your code and 
make the updates necessary to have them pass.

8. Once all of your test cases have passed, commit both the test cases and the
updated module and push the updates to the branch on your forked repository. Once
you have done this, you can go back to your forked repository on Github. You'll
notice a bar at the top that will allow you to submit a pull request based on
the branch that you have just pushed.

9. When creating a pull request, make sure that the title clearly and concisely
described what your code does. For example, we might use the title "Updated
error message on ExampleException". In the body of the pull request, make sure 
that you include the phrase "Closes #issue-number-here", where the issue number is
the issue number of the issue that you are addressing in this PR. 

10. After you have submitted a pull request, a project reviewer will review your
code for quality. You can expect the reviewer to check for the documentation
provided in the changes you made, how thorougb the test cases you provided are,
and how efficient your code is. Your reviewer will provide feedback on your code
and you will have the chance to edit your code and apply fixes.

11. Once your PR is perfected, it will be merged into the master branch of the main
repository and you can celebrate!

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

