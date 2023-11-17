.. _less:

How to Compile .less Files
==========================

.. attention::
    This is copied verbatim from the old IPython wiki and is currently under development. Much of the information in this part of the development guide is out of date.

For testing your development work in CSS, you'll need to compile the
.less files to CSS. Make sure you have dependencies that LESS requires,
including fabric, node, and lessc. Follow the below steps to compile the
.less files:

::

    python setup.py css

Alternatively, you can:

::

    $ cd ipython/IPython/html
    $ fab css
    [localhost] local: components/less.js/bin/lessc -x  style/style.less style/style.min.css
    [localhost] local: components/less.js/bin/lessc -x  style/ipython.less style/ipython.min.css

    Done
