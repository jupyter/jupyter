.. _coding_style:

Coding Style
============

.. attention::
    This is copied verbatim from the old IPython wiki and is currently under development. Much of the information in this part of the development guide is out of date.

This document describes our coding style. Coding style refers to the
following:

-  How source code is formatted (indentation, spacing, etc.)
-  How things are named (variables, functions, classes, modules, etc.)

General coding conventions
--------------------------

In general, we follow the standard Python style conventions as described
in Python's `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`__, the
official Python Style Guide.

Other general comments:

-  In a large file, top level classes and functions should be separated
   by 2 lines to make it easier to separate them visually.

-  Use 4 spaces for indentation, **never** use hard tabs.

-  Keep the ordering of methods the same in classes that have the same
   methods. This is particularly true for classes that implement similar
   interfaces and for interfaces that are similar.

Naming conventions
------------------

For naming conventions, we also follow the guidelines of `PEP
8 <https://www.python.org/dev/peps/pep-0008/>`__. Some of the existing
code doesn't honor this perfectly, but for all new and refactored
IPython code, we'll use:

-  All ``lowercase`` module names. Long module names can have words
   separated by underscores (``really_long_module_name.py``), but this
   is not required. Try to use the convention of nearby files.

-  ``CamelCase`` for class names.

-  ``lowercase_with_underscores`` for methods, functions, variables and
   attributes.

-  Implementation-specific *private* methods will use
   ``_single_underscore_prefix``. Names with a leading double underscore
   will *only* be used in special cases, as they makes subclassing
   difficult (such names are not easily seen by child classes).

-  Occasionally some run-in lowercase names are used, but mostly for
   very short names or where we are implementing methods very similar to
   existing ones in a base class (like ``runlines()`` where
   ``runsource()`` and ``runcode()`` had established precedent).

-  The old IPython codebase has a big mix of classes and modules
   prefixed with an explicit ``IP`` of ``ip``. This is not necessary and
   all new code should not use this prefix. The only case where this
   approach is justified is for classes or functions which are expected
   to be imported into external namespaces and a very generic name (like
   Shell) that is likely to clash with something else. However, if a
   prefix seems absolutely necessary the more specific ``IPY`` or
   ``ipy`` are preferred.

-  All JavaScript code should follow these naming conventions as well.

Attribute declarations for objects
----------------------------------

In general, objects should declare, in their *class*, all attributes the
object is meant to hold throughout its life. While Python allows you to
add an attribute to an instance at any point in time, this makes the
code harder to read and requires methods to constantly use checks with
hasattr() or try/except calls. By declaring all attributes of the object
in the class header, there is a single place one can refer to for
understanding the object's data interface, where comments can explain
the role of each variable and when possible, sensible deafaults can be
assigned.

If an attribute is meant to contain a mutable object, it should be set
to ``None`` in the class and its mutable value should be set in the
object's constructor. Since class attributes are shared by all
instances, failure to do this can lead to difficult to track bugs. But
you should still set it in the class declaration so the interface
specification is complete and documented in one place.

A simple example:

::

    class Foo(object):
        # X does..., sensible default given:
        x = 1
        # y does..., default will be set by constructor
        y = None
        # z starts as an empty list, must be set in constructor
        z = None
        
        def __init__(self, y):
            self.y = y
            self.z = []

New files
---------

When starting a new Python file for IPython, you can use the `following
template <./template.py>`__ as a starting point that has a few common
things pre-written for you.
