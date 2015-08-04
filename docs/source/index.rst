.. _landing:


=======
Jupyter
=======

The Jupyter Notebook is a web application for interactive data science and scientific computing. It
allows users to author documents that combine live-code with narrative text, equations, images, video
and visualizations. These documents encode a complete and reproducible record of a computation that
can be shared with others on GitHub, Dropbox and the Jupyter Notebook Viewer.

The following is an overview of the documentation for the various open source projects in the Jupyter
and IPython organizations.

.. toctree::
    :maxdepth: 1

    install
    config
    system
    data_science

Applications
------------

The Jupyter Applications provide interactive computing environments across a wide range of programming
languages for scientific computing, data science and analytics.

- `Jupyter Notebook <http://jupyter-notebook.readthedocs.org/en/latest/>`__: web-based application for authoring documents that combine live-code with narrative text, equations and visulizations.
- `Jupyter Console <https://github.com/jupyter/jupyter_console>`__: terminal based console for interactive computing.
- `Jupyter QtConsole <https://github.com/jupyter/qtconsole>`__: Qt application for interactive computing with rich output

Kernels
-------

Kernels are separate processes that sit behind the Jupyter user interfaces and
run code in a particular programming language.

`IPython <http://ipython.org>`__ is the reference Jupyter kernel, providing a
powerful environment for interactive computing in Python.

- `IPython Kernel <http://ipython.readthedocs.org/en/master/>`__: interactive computing in Python.
- `ipyparallel <http://ipyparallel.readthedocs.org/en/latest/>`__: lightweight parallel computing in Python with seamless notebook integration.
- `ipywidgets <https://github.com/ipython/ipywidgets>`__: interactive widgets for Python in the Jupyter Notebook.

.. seealso::

   `Jupyter kernels <https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages>`_
      A full list of kernels available for other languages

Working with notebook files
---------------------------

Notebooks are interactive documents that combine live code, narrative text (markdown), visualizations
and other rich media. The following projects allow the programmatic conversion and manipulation of
notebook documents.


* `nbconvert <http://nbconvert.readthedocs.org/en/latest/>`__: convert notebooks to static formats such as HTML, Markdown, LaTeX/PDF and reStrucuredText.
* `nbformat <http://nbformat.readthedocs.org/en/latest/>`__: work with notebook documents programmatically.

Education
---------

The following projects are focused on addressing the pain points of using the Jupyter Notebook in educational settings.

* `nbgrader <http://nbgrader.readthedocs.org/en/stable/>`__: tools for managing and grading notebook based assignments.

Deployment
----------

These projects are being developed to support deploying the notebook in various contexts that include multiuser capabilities and secure/scalable cloud deployments.

* `jupyterhub <https://github.com/jupyter/jupyterhub>`__: multi-user notebook for organizations with plugglable authentication and scalability.
* `jupyter-drive <https://github.com/jupyter/jupyter-drive>`__: store notebooks on Google Drive.
* `nbviewer <https://github.com/jupyter/nbviewer>`__: share notebooks as static HTML on the web.
* `tmpnb <https://github.com/jupyter/tmpnb>`__: temporary, transient notebooks in the cloud.
* `dockerspawner <https://github.com/jupyter/dockerspawner>`__: deploy notebooks for jupyterhub inside docker containers.
* `tmpnb-deploy <https://github.com/jupyter/tmpnb-deploy>`__: deployment tools for tmpnb.

Architecture
------------

The following projects are lower level utilities used to build custom applications with the Jupyter architecture.

* `jupyter_client <http://jupyter-client.readthedocs.org/en/latest/>`__: the specification of the Jupyter message protocol and a clent library in Python.
* `jupyter_core <http://jupyter-core.readthedocs.org/en/latest/>`__: miscellaneous utilities and core functionality.


