=================
Submitting a Bug
=================
While using the Notebook, you might experience a bug that manifests itself in unexpected . If so, we encourage you 
to open issues on Github. To make the navigating issues eaasier for both 
developers and users, we ask that you take the following steps before 
submitting an issue.

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

4. Prepare a simple test that outlines the expected behavior of the code
or a description of the what the expected behavior should be.

5. Prepare an explanation of why the current behavior is not desired and 
what it should be.
