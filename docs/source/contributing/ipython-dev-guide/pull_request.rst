.. _pull_request:

The Perfect Pull Request
========================

.. attention::
    This is copied verbatim from the old IPython wiki and is currently under development. Much of the information in this part of the development guide is out of date.

A brief guide to making and reviewing pull requests.

1. It works
-----------

The code does what it's supposed to!

2. It works on all of the platforms that IPython officially supports
--------------------------------------------------------------------

IPython has to work on:

-  Linux of various kinds, Windows & Mac
-  Python 2 & 3

3. Handles unicode issues properly
----------------------------------

Much of our code base deals with strings and unicode. This needs to be
done in a manner that is unicode aware and works on Python 2 and 3.
`This article <http://www.joelonsoftware.com/articles/Unicode.html>`__ is
a good intro to unicode.

4. Adheres to our coding style
------------------------------

Coding style refers to how source code is formatted and how variables,
functions, methods and classes are named. Your code should follow our
coding style, which is described `here <coding_style.html>`__.

5. Clean & commented
--------------------

The code should be well organized, and have inline comments where
appropriate. When we look at the code, it should be clear what it's
doing and why. It should not break abstractions that we have established
in the project.

6. Tested
---------

If it fixes a bug, the pull request should ideally add an automated test
that fails without the fix, and passes with it. Normally it should be
sufficient to copy an existing test and tweak it. New functionality
should come with its own tests as well. Details about testing IPython
can be found `here <testing.html>`__.

7. Well documented
------------------

Don't forget to update docstrings, and any relevant parts of `the
official
documentation <https://ipython.readthedocs.io/en/stable/>`__. New
features or significant changes warrant an entry in the *What's New*
section too. Details about documenting IPython can be found `here <documenting_ipython.html>`__.