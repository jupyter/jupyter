.. _landing:


=======
Jupyter
=======

The Jupyter Notebook is a web application for interactive data science and
scientific computing. Using Jupyter Notebook, users can author engaging
documents that combine live-code with narrative text, equations, images, video,
and visualizations. By encoding a complete and reproducible record of a
computation, the documents can be shared with others on GitHub, Dropbox, and
the `Jupyter Notebook Viewer <https://github.com/jupyter/nbviewer>`__.

The following summary highlights the various open source projects in the
Jupyter and IPython organizations.

.. toctree::
    :maxdepth: 1

    install
    config
    system
    data_science
    glossary


Jupyter Applications
--------------------

The Jupyter Applications create a foundation of interactive computing environments
where scientific computing, data science, and analytics can be performed using
a wide range of programming languages.

- `Jupyter Notebook <http://jupyter-notebook.readthedocs.org/en/latest/>`__:
  web-based application for authoring documents that combine live-code with
  narrative text, equations and visualizations.
- `Jupyter Console <https://github.com/jupyter/jupyter_console>`__: terminal
  based console for interactive computing.
- `Jupyter QtConsole <https://github.com/jupyter/qtconsole>`__: Qt application
  for interactive computing with rich output.


Kernels
-------

Kernels are `programming language specfic` processes that run independently
and interact with the Jupyter Applications and their user interfaces.

`IPython <http://ipython.org>`__ is the reference Jupyter kernel, providing a
powerful environment for interactive computing in Python.

- `IPython Kernel <http://ipython.readthedocs.org/en/master/>`__: interactive
  computing in Python.
- `ipyparallel <http://ipyparallel.readthedocs.org/en/latest/>`__: lightweight
  parallel computing in Python offering seamless notebook integration.
- `ipywidgets <https://github.com/ipython/ipywidgets>`__: interactive widgets
  for Python in the Jupyter Notebook.

.. seealso::

   `Jupyter kernels <https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages>`_
      A full list of kernels available for other languages


Formatting and Conversion Projects
----------------------------------

Notebooks are rich interactive documents that combine live code, narrative text
(using markdown), visualizations, and other rich media. The following utility
projects allow programmatic format conversion and manipulation of notebook documents.

* `nbconvert <http://nbconvert.readthedocs.org/en/latest/>`__: convert dynamic
  notebooks to static formats such as HTML, Markdown, LaTeX/PDF, and
  reStrucuredText.
* `nbformat <http://nbformat.readthedocs.org/en/latest/>`__: work with notebook
  documents programmatically.


Education Projects
------------------

Jupyter Notebooks offer exciting and creative possibilities in education. The
following projects are focused on supporting the use of Jupyter Notebook in
a variety of educational settings.

* `nbgrader <http://nbgrader.readthedocs.org/en/stable/>`__: tools for
  managing, grading, and reporting of notebook based assignments.


Deployment Projects
-------------------

To serve a variety of users and use cases, these projects are being
developed to support notebook deployment in various contexts, including
multiuser capabilities and secure, scalable cloud deployments.

* `jupyterhub <https://github.com/jupyter/jupyterhub>`__: multi-user notebook
  for organizations with plugglable authentication and scalability.
* `jupyter-drive <https://github.com/jupyter/jupyter-drive>`__: store notebooks
  on Google Drive.
* `nbviewer <https://github.com/jupyter/nbviewer>`__: share notebooks as static
  HTML on the web.
* `tmpnb <https://github.com/jupyter/tmpnb>`__: create temporary, transient
  notebooks in the cloud.
* `dockerspawner <https://github.com/jupyter/dockerspawner>`__: deploy
  notebooks for `jupyterhub` inside Docker containers.
* `tmpnb-deploy <https://github.com/jupyter/tmpnb-deploy>`__: deployment tools
  for tmpnb.


Architecture Projects
---------------------

The following projects are lower level utilities used to build custom
applications with the Jupyter architecture.

* `jupyter_client <http://jupyter-client.readthedocs.org/en/latest/>`__: the
  specification of the Jupyter message protocol and a client library in Python.
* `jupyter_core <http://jupyter-core.readthedocs.org/en/latest/>`__:
  core functionality and miscellaneous utilities.
