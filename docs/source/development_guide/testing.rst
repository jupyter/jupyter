.. _testing:

Testing IPython for users and developers
========================================

.. attention::
    This is copied verbatim from the old IPython wiki and is currently under development. Much of the information in this part of the development guide is out of date.

Overview
--------

It is extremely important that all code contributed to IPython has
tests. Tests should be written as unittests, doctests or other entities
that the IPython test system can detect. See below for more details on
this.

Each subpackage in IPython should have its own ``tests`` directory that
contains all of the tests for that subpackage. All of the files in the
``tests`` directory should have the word "tests" in them to enable the
testing framework to find them.

In docstrings, examples (either using IPython prompts like ``In [1]:``
or 'classic' python ``>>>`` ones) can and should be included. The
testing system will detect them as doctests and will run them; it offers
control to skip parts or all of a specific doctest if the example is
meant to be informative but shows non-reproducible information (like
filesystem data).

If a subpackage has any dependencies beyond the Python standard library,
the tests for that subpackage should be skipped if the dependencies are
not found. This is very important so users don't get tests failing
simply because they don't have dependencies.

The testing system we use is an extension of the
`nose <https://code.google.com/archive/p/python-nose>`__ test runner. In
particular we've developed a nose plugin that allows us to paste
verbatim IPython sessions and test them as doctests, which is extremely
important for us.

Running the test suite
----------------------

You can run IPython from the source download directory without even
installing it system-wide or having configure anything, by typing at the
terminal:

.. code:: bash

       python2 -c "import IPython; IPython.start_ipython();"

To start the webbased notebook you can use:

.. code:: bash

       python2 -c "import IPython; IPython.start_ipython(['notebook']);"

In order to run the test suite, you must at least be able to import
IPython, even if you haven't fully installed the user-facing scripts yet
(common in a development environment). You can then run the tests with:

.. code:: bash

      python -c "import IPython; IPython.test()"

Once you have installed IPython either via a full install or using:

.. code:: bash

      python setup.py develop

you will have available a system-wide script called ``iptest`` that runs
the full test suite. You can then run the suite with:

.. code:: bash

       iptest  [args]

By default, this excludes the relatively slow tests for
``IPython.parallel``. To run these, use ``iptest --all``.

Please note that the iptest tool will run tests against the code
imported by the Python interpreter. If the command
``python setup.py symlink`` has been previously run then this will
always be the test code in the local directory via a symlink. However,
if this command has not been run for the version of Python being tested,
there is the possibility that iptest will run the tests against an
installed version of IPython.

Regardless of how you run things, you should eventually see something
like:

.. code:: text

       **********************************************************************
       Test suite completed for system with the following information:
       {'commit_hash': '144fdae',
        'commit_source': 'repository',
        'ipython_path': '/home/fperez/usr/lib/python2.6/site-packages/IPython',
        'ipython_version': '0.11.dev',
        'os_name': 'posix',
        'platform': 'Linux-2.6.35-22-generic-i686-with-Ubuntu-10.10-maverick',
        'sys_executable': '/usr/bin/python',
        'sys_platform': 'linux2',
        'sys_version': '2.6.6 (r266:84292, Sep 15 2010, 15:52:39) \n[GCC 4.4.5]'}

       Tools and libraries available at test time:
          curses matplotlib pymongo qt sqlite3 tornado wx wx.aui zmq

       Ran 9 test groups in 67.213s

       Status:
       OK

If not, there will be a message indicating which test group failed and
how to rerun that group individually. For example, this tests the
``IPython.utils`` subpackage, the ``-v`` option shows progress
indicators:

.. code:: bash

       $ iptest IPython.utils -- -v
       ..........................SS..SSS............................S.S...
       .........................................................
       ----------------------------------------------------------------------
       Ran 125 tests in 0.119s

       OK (SKIP=7)

Because the IPython test machinery is based on nose, you can use all
nose syntax. Options after ``--`` are passed to nose. For example, this
lets you run the specific test ``test_rehashx`` inside the
``test_magic`` module:

.. code:: bash

       $ iptest IPython.core.tests.test_magic:test_rehashx -- -vv
       IPython.core.tests.test_magic.test_rehashx(True,) ... ok
       IPython.core.tests.test_magic.test_rehashx(True,) ... ok

       ----------------------------------------------------------------------
       Ran 2 tests in 0.100s

       OK

When developing, the ``--pdb`` and ``--pdb-failures`` of nose are
particularly useful, these drop you into an interactive pdb session at
the point of the error or failure respectively:
``iptest mymodule -- --pdb``.

The system information summary printed above is accessible from the top
level package. If you encounter a problem with IPython, it's useful to
include this information when reporting on the mailing list; use::

.. code:: python

        from IPython import sys_info
        print sys_info()

and include the resulting information in your query.

Testing pull requests
---------------------

We have a script that fetches a pull request from Github, merges it with
master, and runs the test suite on different versions of Python. This
uses a separate copy of the repository, so you can keep working on the
code while it runs. To run it:

.. code:: bash

        python tools/test_pr.py -p 1234

The number is the pull request number from Github; the ``-p`` flag makes
it post the results to a comment on the pull request. Any further
arguments are passed to ``iptest``.

This requires the `requests <https://pypi.python.org/pypi/requests>`__
and `keyring <https://pypi.python.org/pypi/keyring>`__ packages.

For developers: writing tests
-----------------------------

By now IPython has a reasonable test suite, so the best way to see
what's available is to look at the ``tests`` directory in most
subpackages. But here are a few pointers to make the process easier.

Main tools: ``IPython.testing``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``IPython.testing`` package is where all of the machinery to test
IPython (rather than the tests for its various parts) lives. In
particular, the ``iptest`` module in there has all the smarts to control
the test process. In there, the ``make_exclude`` function is used to
build a blacklist of exclusions, these are modules that do not get even
imported for tests. This is important so that things that would fail to
even import because of missing dependencies don't give errors to end
users, as we stated above.

The ``decorators`` module contains a lot of useful decorators,
especially useful to mark individual tests that should be skipped under
certain conditions (rather than blacklisting the package altogether
because of a missing major dependency).

Our nose plugin for doctests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``plugin`` subpackage in testing contains a nose plugin called
``ipdoctest`` that teaches nose about IPython syntax, so you can write
doctests with IPython prompts. You can also mark doctest output with
``# random`` for the output corresponding to a single input to be
ignored (stronger than using ellipsis and useful to keep it as an
example). If you want the entire docstring to be executed but none of
the output from any input to be checked, you can use the
``# all-random`` marker. The ``IPython.testing.plugin.dtexample`` module
contains examples of how to use these; for reference here is how to use
``# random``:

.. code:: python

        def ranfunc():
        """A function with some random output.

           Normal examples are verified as usual:
           >>> 1+3
           4

           But if you put '# random' in the output, it is ignored:
           >>> 1+3
           junk goes here...  # random

           >>> 1+2
           again,  anything goes #random
           if multiline, the random mark is only needed once.

           >>> 1+2
           You can also put the random marker at the end:
           # random

           >>> 1+2
           # random
           .. or at the beginning.

           More correct input is properly verified:
           >>> ranfunc()
           'ranfunc'
        """
        return 'ranfunc'

and an example of ``# all-random``:

.. code:: python

        def random_all():
        """A function where we ignore the output of ALL examples.

        Examples:

          # all-random

          This mark tells the testing machinery that all subsequent examples
          should be treated as random (ignoring their output).  They are still
          executed, so if a they raise an error, it will be detected as such,
          but their output is completely ignored.

          >>> 1+3
          junk goes here...

          >>> 1+3
          klasdfj;

        In [8]: print 'hello'
        world  # random

        In [9]: iprand()
        Out[9]: 'iprand'
        """
        return 'iprand'

When writing docstrings, you can use the ``@skip_doctest`` decorator to
indicate that a docstring should *not* be treated as a doctest at all.
The difference between ``# all-random`` and ``@skip_doctest`` is that
the former executes the example but ignores output, while the latter
doesn't execute any code. ``@skip_doctest`` should be used for
docstrings whose examples are purely informational.

If a given docstring fails under certain conditions but otherwise is a
good doctest, you can use code like the following, that relies on the
'null' decorator to leave the docstring intact where it works as a test:

.. code:: python

      # The docstring for full_path doctests differently on win32 (different path
      # separator) so just skip the doctest there, and use a null decorator
      # elsewhere:
      
      doctest_deco = dec.skip_doctest if sys.platform == 'win32' else dec.null_deco

      @doctest_deco
      def full_path(startPath,files):
          """Make full paths for all the listed files, based on startPath..."""

          # function body follows...

With our nose plugin that understands IPython syntax, an extremely
effective way to write tests is to simply copy and paste an interactive
session into a docstring. You can writing this type of test, where your
docstring is meant *only* as a test, by prefixing the function name with
``doctest_`` and leaving its body *absolutely empty* other than the
docstring. In ``IPython.core.tests.test_magic`` you can find several
examples of this, but for completeness sake, your code should look like
this (a simple case):

.. code:: python

        def doctest_time():
        """
        In [10]: %time None
        CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
        Wall time: 0.00 s
        """

This function is only analyzed for its docstring but it is not
considered a separate test, which is why its body should be empty.

JavaScript Tests
~~~~~~~~~~~~~~~~

We currently use `casperjs <http://casperjs.org/>`__ for testing the
notebook javascript user interface.

To run the JS test suite by itself, you can either use ``iptest js``,
which will start up a new notebook server and test against it, or you
can open up a notebook server yourself, and then:

::

    cd IPython/html/tests/casperjs;
    casperjs test --includes=util.js test_cases

If your testing notebook server uses something other than the default
port (8888), you will have to pass that as a parameter to the test suite
as well.

::

    casperjs test --includes=util.js --port=8889 test_cases

Running individual tests
^^^^^^^^^^^^^^^^^^^^^^^^

To speed up development, you usually are working on getting one test
passing at a time. To do this, just pass the filename directly to the
``casperjs test`` command like so:

::

    casperjs test --includes=util.js  test_cases/execute_code_cell.js

Wrapping your head around the javascript within javascript:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CasperJS is a browser that's written in javascript, so we write
javascript code to drive it. The Casper browser itself also has a
javascript implementation (like the ones that come with Firefox and
Chrome), and in the test suite we get access to those using
``this.evaluate``, and it's cousins (``this.theEvaluate``, etc).
Additionally, because of the asynchronous / callback nature of
everything, there are plenty of ``this.then`` calls which define steps
in test suite. Part of the reason for this is that each step has a
timeout (default of 5 or 10 seconds). Additionally, there are already
convenience functions in ``util.js`` to help you wait for output in a
given cell, etc. In our javascript tests, if you see functions which
``look_like_pep8_naming_convention``, those are probably coming from
``util.js``, whereas functions that come with casper
``haveCamelCaseNamingConvention``

Each file in ``test_cases`` looks something like this (this is
``test_cases/check_interrupt.js``):

::

    casper.notebook_test(function () {
        this.evaluate(function () {
            var cell = IPython.notebook.get_cell(0);
            cell.set_text('import time\nfor x in range(3):\n    time.sleep(1)');
            cell.execute();
        });


        // interrupt using menu item (Kernel -> Interrupt)
        this.thenClick('li#int_kernel');

        this.wait_for_output(0);

        this.then(function () {
            var result = this.get_output_cell(0);
            this.test.assertEquals(result.ename, 'KeyboardInterrupt', 'keyboard interrupt (mouseclick)');
        });

        // run cell 0 again, now interrupting using keyboard shortcut
        this.thenEvaluate(function () {
            cell.clear_output();
            cell.execute();
        });

        // interrupt using Ctrl-M I keyboard shortcut
        this.thenEvaluate( function() {
            IPython.utils.press_ghetto(IPython.utils.keycodes.I)
        });
        
        this.wait_for_output(0);
        
        this.then(function () {
            var result = this.get_output_cell(0);
            this.test.assertEquals(result.ename, 'KeyboardInterrupt', 'keyboard interrupt (shortcut)');
        });
    });

For an example of how to pass parameters to the client-side javascript
from casper test suite, see the ``casper.wait_for_output``
implementation in ``IPython/html/tests/casperjs/util.js``

Testing system design notes
---------------------------

This section is a set of notes on the key points of the IPython testing
needs, that were used when writing the system and should be kept for
reference as it eveolves.

Testing IPython in full requires modifications to the default behavior
of nose and doctest, because the IPython prompt is not recognized to
determine Python input, and because IPython admits user input that is
not valid Python (things like ``%magics`` and ``!system commands``.

We basically need to be able to test the following types of code:

-  

   (1) Pure Python files containing normal tests. These are not a
       problem, since Nose will pick them up as long as they conform to
       the (flexible) conventions used by nose to recognize tests.

-  

   (2) Python files containing doctests. Here, we have two
       possibilities:

-  The prompts are the usual ``>>>`` and the input is pure Python.
-  The prompts are of the form ``In [1]:`` and the input can contain
   extended IPython expressions.

In the first case, Nose will recognize the doctests as long as it is
called with the ``--with-doctest`` flag. But the second case will likely
require modifications or the writing of a new doctest plugin for Nose
that is IPython-aware.

-  

   (3) ReStructuredText files that contain code blocks. For this type of
       file, we have three distinct possibilities for the code blocks:

-  They use ``>>>`` prompts.
-  They use ``In [1]:`` prompts.
-  They are standalone blocks of pure Python code without any prompts.

The first two cases are similar to the situation #2 above, except that
in this case the doctests must be extracted from input code blocks using
docutils instead of from the Python docstrings.

In the third case, we must have a convention for distinguishing code
blocks that are meant for execution from others that may be snippets of
shell code or other examples not meant to be run. One possibility is to
assume that all indented code blocks are meant for execution, but to
have a special docutils directive for input that should not be executed.

For those code blocks that we will execute, the convention used will
simply be that they get called and are considered successful if they run
to completion without raising errors. This is similar to what Nose does
for standalone test functions, and by putting asserts or other forms of
exception-raising statements it becomes possible to have literate
examples that double as lightweight tests.

-  

   (4) Extension modules with doctests in function and method
       docstrings. Currently Nose simply can't find these docstrings
       correctly, because the underlying doctest DocTestFinder object
       fails there. Similarly to #2 above, the docstrings could have
       either pure python or IPython prompts.

Of these, only 3-c (reST with standalone code blocks) is not implemented
at this point.
