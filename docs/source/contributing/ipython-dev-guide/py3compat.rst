.. _py3compat:

Python 3 Compatibility Module
=============================

.. attention::
    This is copied verbatim from the old IPython wiki and is currently under development. Much of the information in this part of the development guide is out of date.

The ``IPython.utils.py3compat`` module provides a number of functions to make it easier to write code for Python 2 and 3. We also use 2to3 in the setup process to change syntax, and the ``io.open()`` function, which is essentially the built in open function from Python 3.

The names provided are:

* **PY3**: True in Python 3, False in Python 2.

Unicode related
---------------
* **decode**, **encode**: Shortcuts to decode or encode strings, using ``sys.stdin.encoding`` by default, and using replacement characters on errors.
* **str_to_unicode**, **unicode_to_str**, **str_to_bytes**, **bytes_to_str**: Convert to/from the platform's standard ``str`` type (bytes in Python 2, unicode in Python 3). Each function is a no-op on one of the two platforms.
* **cast_unicode**, **cast_bytes**: Accept unknown unicode or byte strings, and convert them accordingly.
* **cast_bytes_py2**: Casts unicode to byte strings on Python 2, but doesn't do anything on Python 3.

Miscellaneous
-------------
* **input**: Refers to ``raw_input`` on Python 2, ``input`` on Python 3 (needed because 2to3 only converts calls to raw_input, not assignments to other names).
* **builtin_mod_name**: The string name you import to get the builtins (``__builtin__`` --> ``builtins``).
* **isidentifier**: Checks if a string is a valid Python identifier.
* **open**: Simple wrapper for Python 3 unicode-enabled open. Similar to ``codecs.open``, but allows universal newlines. The current implementation only supports the very simplest use.
* **MethodType**: ``types.MethodType`` from Python 3. Takes only two arguments: function, instance. The class argument for Python 2 is filled automatically.
* **doctest_refactor_print**: Can be called on a string or a function (or used as a decorator). In Python 3, it converts print statements in doctests to print() calls. 2to3 does this for real doctests, but we need it in several other places. It simply uses a regex, which is good enough for the current cases.
* **u_format**: Where tests use the repr() of a unicode string, it should be written ``'{u}"thestring"'``, and fed to this function, which will produce ``'u"thestring"'`` for Python 2, and ``'"thestring"'`` for Python 3. Can also be used as a decorator, to work on a docstring.
* **execfile**: Makes a return on Python 3 (where it's no longer a builtin), and upgraded to handle Unicode filenames on Python 2.
