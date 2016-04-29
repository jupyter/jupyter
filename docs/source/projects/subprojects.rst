.. _subprojects:

================
Jupyter projects
================

Project Jupyter is developed as a set of subprojects. The following is a topical
list of the officially supported and maintained subprojects with links to the
documentation or GitHub repo of each.



Jupyter user interfaces
-----------------------

The Jupyter user interfaces offer a foundation of interactive computing
environments where scientific computing, data science, and analytics can be
performed using a wide range of programming languages.


.. glossary::

    `Jupyter Notebook <https://jupyter-notebook.readthedocs.io/en/latest/>`__
        Web-based application for authoring documents that combine live-code
        with narrative text, equations and visualizations.
        `Documentation <https://jupyter-notebook.readthedocs.io/en/latest/>`__ |
        `Repo <https://github.com/jupyter/notebook>`__

    `Jupyter Console <https://jupyter-console.readthedocs.io/en/latest/>`__
        Terminal based console for interactive computing.
        `Documentation <https://jupyter-console.readthedocs.io/en/latest/>`__ |
        `Repo <https://github.com/jupyter/jupyter_console>`__

    `Jupyter QtConsole <https://jupyter.org/qtconsole/stable/>`__
        Qt application for interactive computing with rich output.
        `Documentation <https://jupyter.org/qtconsole/stable/>`__ |
        `Repo <https://github.com/jupyter/qtconsole>`__


Kernels
-------

Kernels are `programming language specific` processes that run independently
and interact with the Jupyter Applications and their user interfaces. `IPython <https://ipython.org>`__ is the reference Jupyter kernel, providing a
powerful environment for interactive computing in Python.

.. glossary::

    `IPython <https://ipython.org>`__
        interactive computing in Python.
        `Documentation <https://ipython.org/documentation.html>`__ |
        `Repo <https://github.com/ipython/ipython>`__

    `ipywidgets <https://ipywidgets.readthedocs.io/en/latest/>`__
        interactive widgets for Python in the Jupyter Notebook.
        `Documentation <https://ipywidgets.readthedocs.io/en/latest/>`__ |
        `Repo <https://github.com/ipython/ipywidgets>`__

    `ipyparallel <https://ipyparallel.readthedocs.io/en/latest/>`__
        lightweight parallel computing in Python offering seamless notebook integration.
        `Documentation <https://ipyparallel.readthedocs.io/en/latest/>`__ |
        `Repo <https://github.com/ipython/ipyparallel>`__

.. seealso::

      `Jupyter kernels <https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages>`_
      for a full list of kernels available for other languages. Many of
      these kernels are developed by third parties and may or may not be stable.


Formatting and conversion
-------------------------

Notebooks are rich interactive documents that combine live code, narrative text
(using markdown), visualizations, and other rich media. The following utility
subprojects allow programmatic format conversion and manipulation of notebook documents.

.. glossary::

    `nbconvert <https://nbconvert.readthedocs.io/en/latest/>`__
        Convert dynamic notebooks to static formats such as HTML, Markdown,
        LaTeX/PDF, and reStrucuredText.
        `Documentation <https://nbconvert.readthedocs.io/en/latest/>`__ |
        `Repo <https://github.com/jupyter/nbconvert>`__

    `nbformat <https://nbformat.readthedocs.io/en/latest/>`__
        Work with notebook documents programmatically.
        `Documentation <https://nbformat.readthedocs.io/en/latest/>`__ |
        `Repo <https://github.com/jupyter/nbformat>`__


Education
---------

Jupyter Notebooks offer exciting and creative possibilities in education. The
following subprojects are focused on supporting the use of Jupyter Notebook in
a variety of educational settings.

.. glossary::

    `nbgrader <https://nbgrader.readthedocs.io/en/stable/>`__
        tools for managing, grading, and reporting of notebook based
        assignments.
        `Documentation <https://nbgrader.readthedocs.io/en/stable/>`__ |
        `Repo <https://github.com/jupyter/nbgrader>`__


Deployment
----------

To serve a variety of users and use cases, these subprojects are being
developed to support notebook deployment in various contexts, including
multiuser capabilities and secure, scalable cloud deployments.

.. glossary::

    `jupyterhub <https://github.com/jupyterhub/jupyterhub>`__
        Multi-user notebook for organizations with pluggable authentication
        and scalability.
        `Documentation <https://jupyterhub.readthedocs.io/en/latest/>`__ |
        `Repo <https://github.com/jupyterhub/jupyterhub>`__

    `jupyter-drive <https://github.com/jupyter/jupyter-drive>`__
        Store notebooks on Google Drive.
        `Documentation <https://github.com/jupyter/jupyter-drive>`__ |
        `Repo <https://github.com/jupyter/jupyter-drive>`__

    `nbviewer <https://nbviewer.jupyter.org/>`__
        Share notebooks as static HTML on the web.
        `Documentation <https://github.com/jupyter/nbviewer>`__ |
        `Repo <https://github.com/jupyter/nbviewer>`__

    `tmpnb <https://github.com/jupyter/tmpnb>`__
        Create temporary, transient notebooks in the cloud.
        `Documentation <https://github.com/jupyter/tmpnb>`__ |
        `Repo <https://github.com/jupyter/tmpnb>`__

    `tmpnb-deploy <https://github.com/jupyter/tmpnb-deploy>`__
        Deployment tools for tmpnb.
        `Documentation <https://github.com/jupyter/tmpnb-deploy>`__ |
        `Repo <https://github.com/jupyter/tmpnb-deploy>`__

    `dockerspawner <https://github.com/jupyterhub/dockerspawner>`__
        Deploy notebooks for 'jupyterhub' inside Docker containers.
        `Documentation <https://github.com/jupyterhub/dockerspawner>`__ |
        `Repo <https://github.com/jupyterhub/dockerspawner>`__

    `docker-stacks <https://github.com/jupyter/docker-stacks>`__
        Stacks of Jupyter applications and kernels as Docker containers.
        `Documentation <https://github.com/jupyter/docker-stacks>`__ |
        `Repo <https://github.com/jupyter/docker-stacks>`__


Architecture
------------

The following projects are lower level utilities used to build custom
applications with the Jupyter architecture.

.. glossary::

    `jupyter_client <https://jupyter-client.readthedocs.io/en/latest/>`__
        The specification of the Jupyter message protocol and a client library
        in Python.
        `Documentation <https://jupyter-client.readthedocs.io/en/latest/>`__ |
        `Repo <https://github.com/jupyter/jupyter_client>`__

    `jupyter_core <https://jupyter-core.readthedocs.io/en/latest/>`__
        Core functionality and miscellaneous utilities.
        `Documentation <https://jupyter-core.readthedocs.io/en/latest/>`__ |
        `Repo <https://github.com/jupyter/jupyter_core>`__
