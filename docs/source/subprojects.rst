.. _subprojects:


===================
Jupyter subprojects
===================

Project Jupyter is developed as a set of subprojects. The following is a topical
list of the officially supported and maintained subprojects with links to the
documentation or GitHub repo of each.



Jupyter user interfaces
-----------------------

The Jupyter user interfaces offer a foundation of interactive computing
environments where scientific computing, data science, and analytics can be
performed using a wide range of programming languages.


.. glossary::


    `Jupyter Notebook <http://jupyter-notebook.readthedocs.org/en/latest/>`__
        Web-based application for authoring documents that combine live-code
        with narrative text, equations and visualizations.

    `Jupyter Console <https://github.com/jupyter/jupyter_console>`__
        Terminal based console for interactive computing.

    `Jupyter QtConsole <https://github.com/jupyter/qtconsole>`__
        Qt application for interactive computing with rich output.


Kernels
-------

Kernels are `programming language specific` processes that run independently
and interact with the Jupyter Applications and their user interfaces. `IPython <http://ipython.org>`__ is the reference Jupyter kernel, providing a
powerful environment for interactive computing in Python.

.. glossary::

    `IPython <http://ipython.org>`__
        interactive computing in Python.

    `ipywidgets <https://github.com/ipython/ipywidgets>`__
        interactive widgets for Python in the Jupyter Notebook.

    `ipyparallel <http://ipyparallel.readthedocs.org/en/latest/>`__
        lightweight parallel computing in Python offering seamless notebook integration.

.. seealso::

   See the `Jupyter kernels <https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages>`_
      page for a full list of kernels available for other languages. Many of
      these kernels are developed by third parties and may or may not be stable.


Formatting and conversion
-------------------------

Notebooks are rich interactive documents that combine live code, narrative text
(using markdown), visualizations, and other rich media. The following utility
subprojects allow programmatic format conversion and manipulation of notebook documents.

.. glossary::

    `nbconvert <http://nbconvert.readthedocs.org/en/latest/>`__
        Convert dynamic notebooks to static formats such as HTML, Markdown,
        LaTeX/PDF, and reStrucuredText.

    `nbformat <http://nbformat.readthedocs.org/en/latest/>`__
        Work with notebook documents programmatically.


Education
---------

Jupyter Notebooks offer exciting and creative possibilities in education. The
following subprojects are focused on supporting the use of Jupyter Notebook in
a variety of educational settings.

.. glossary::

    `nbgrader <http://nbgrader.readthedocs.org/en/stable/>`__
        tools for managing, grading, and reporting of notebook based
        assignments.


Deployment
----------

To serve a variety of users and use cases, these subprojects are being
developed to support notebook deployment in various contexts, including
multiuser capabilities and secure, scalable cloud deployments.

.. glossary::

    `jupyterhub <https://github.com/jupyter/jupyterhub>`__
        Multi-user notebook for organizations with plugglable authentication
        and scalability.

    `jupyter-drive <https://github.com/jupyter/jupyter-drive>`__
        Store notebooks on Google Drive.

    `nbviewer <https://github.com/jupyter/nbviewer>`__
        Share notebooks as static HTML on the web.

    `tmpnb <https://github.com/jupyter/tmpnb>`__
        Create temporary, transient notebooks in the cloud.

    `tmpnb-deploy <https://github.com/jupyter/tmpnb-deploy>`__
        Deployment tools for tmpnb.

    `dockerspawner <https://github.com/jupyter/dockerspawner>`__
        Deploy notebooks for 'jupyterhub' inside Docker containers.
        
    `docker-stacks <https://github.com/jupyter/docker-stacks>`__
        Stacks of Jupyter applications and kernels as Docker containers.


Architecture
------------

The following projects are lower level utilities used to build custom
applications with the Jupyter architecture.

.. glossary::

    `jupyter_client <http://jupyter-client.readthedocs.org/en/latest/>`__
        The specification of the Jupyter message protocol and a client library
        in Python.

    `jupyter_core <http://jupyter-core.readthedocs.org/en/latest/>`__
        Core functionality and miscellaneous utilities.


