.. _testing_kernels:

Testing Kernels
===============

.. attention::
    This is copied verbatim from the old IPython wiki and is currently under development. Much of the information in this part of the development guide is out of date.

IPython makes it very easy to create wrapper kernels using its kernel
framework. It requires extending the Kernel class and implementing a set
of methods for the core functions like execute, history etc. Its also
possible to write a full blown kernel in a language of your choice
implementing listeners for all the zmq ports.

The key problem for any kernel implemented by these methods is to ensure
that it meets the message specification. The kerneltest command is a
means to test the installed kernel against the message spec and validate
the results.

The kerneltest tool
-------------------

The kerneltest tool is part of IPython.testing and is also included in
the scripts similar to iptest. This takes 2 parameters - the name of the
kernel to test and the test script file. The test script file should be
in json format as described in the next section.

::

    kerneltest python test_script.json

You can also pass in an optional message spec version to the command. At
the moment only the version 5 is supported, but as newer versions are
released this can be used to test the kernel against a specific version
of the kernel.

::

    kerneltest python test_script.json 5

The kernel to be tested needs to be installed and the kernelspec
available in the user IPython directory. The tool will instantiate the
kernel and send the commands over ZMQ. For each command executed on the
kernel, the tool will validate the reply to ensure that it matches the
message specification. In some cases the output is also checked, but the
reply is always returned and printed out on the console. This can be
used to validate that apart from meeting the message spec the kernel
also produced the correct output.

The test script file
--------------------

The test script file is a simple json file that specifies the command to
execute and the test code to execute for the command.

::

    {
        "command":{
               "test_code":<code>
        }
    }

For some commands in the message specification like kernel\_info there
is no need to specify the test\_code parameter. The tool validates if it
has all the inputs needed to execute the command and will print out an
error to the console if it finds a missing parameter. Since the
validation is built in, and only required parameters are passed, it is
possible to add additional fields in the json file for test
documentation.

::

    {
        "command":{
               "test_name":"sample test",
               "test_description":"sample test to show how the test script file is created",
               "test_code":<code>
        }
    }

A sample test script for the redis kernel will look like this

::

    {
      "execute":{
        "test_code":"get a",
        "comments":"test basic code execution"
      },
      "complete":{
        "test_code":"get",
        "comments":"test getting command auto complete"
      },
      "kernel_info":{
        "comments":"simple kernel info check"
      },
      "single_payload":{
        "test_code":"get a",
        "comments":"test one payload"
      },
      "history_tail":{
        "test_code":"get a",
        "comments":"test tail history"
      },
      "history_range":{
        "test_code":"get a",
        "comments":"test range history"
      },
      "history_search":{
        "test_code":"get a",
        "comments":"test search history"
      }
    }
