.. _landing:


=======
Jupyter
=======

The following is an overview of the documentation and developer resources for the various open source projects in the Jupyter
and IPython ecosystem.

Installation
------------

See the :doc:`installation overview <install>`.

User Interfaces
---------------

The Jupyter user interfaces provide a uniform interactive computing experience for users across a wide range of programming languages.

- Notebook (`Documentation <http://jupyter-notebook.readthedocs.org/en/latest/>`__, `GitHub Repo <https://github.com/jupyter/notebook>`__, `Gitter Chat Room <https://gitter.im/jupyter/notebook>`__)
- Console (`GitHub Repo <https://github.com/jupyter/jupyter_console>`__, `Gitter Chat Room <https://gitter.im/jupyter/jupyter_console>`__)
- QtConsole (`Documentation <http://qtconsole.readthedocs.org/en/latest/>`__, `GitHub Repo <https://github.com/jupyter/qtconsole>`__, `Gitter Chat Room <https://gitter.im/jupyter/qtconsole>`__)

Kernels
-------

Kernels are separate processes that sit behind the Jupyter user interfaces and run code in a particular programming language.

* Python
    - IPython Kernel (`Documentation <http://ipython.readthedocs.org/en/master/>`__, `GitHub Repo <https://github.com/ipython/ipython>`__, `Gitter Chat Room <https://gitter.im/ipython/ipython>`__)
    - Traitlets (`Documentation <http://traitlets.readthedocs.org/en/latest/>`__, `GitHub Repo <https://github.com/ipython/traitlets>`__, `Gitter Chat Room <https://gitter.im/ipython/ipython>`__)
    - Parallel Computing (`Documentation <http://ipyparallel.readthedocs.org/en/latest/>`__, `GitHub Repo <https://github.com/ipython/ipyparallel>`__, `Gitter Chat Room <https://gitter.im/ipython/ipyparallel>`__)
    - Interactive Widgets (`Documentation <http://ipyparallel.readthedocs.org/en/latest/>`__, `GitHub Repo <https://github.com/ipython/ipywidgets>`__, `Gitter Chat Room <https://gitter.im/ipython/ipywidgets>`__)
* R
    - IRkernel (`Documentation <http://irkernel.github.io/>`__, `GitHub Repo <https://github.com/IRkernel/IRkernel>`__)
    - IRdisplay (`GitHub Repo <https://github.com/IRkernel/IRdisplay>`__)
    - repr (`GitHub Repo <https://github.com/IRkernel/repr>`__)
* Julia
     - IJulia Kernel (`GitHub Repo <https://github.com/JuliaLang/IJulia.jl>`__)
     - Interactive Widgets (`GitHub Repo <https://github.com/JuliaLang/Interact.jl>`__)
* Bash (`GitHub Repo <https://github.com/takluyver/bash_kernel>`__)

See `this page <https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages>`_ for a full list of kernels available for other languages.

Working with Notebooks
----------------------

Notebooks are interactive documents that combine live code, narrative text
(markdown), visualizations and other rich media. The following projects
allow the programmatic conversion and manipulation of notebook documents.

* nbconvert (`Documentation <http://nbconvert.readthedocs.org/en/latest/>`__, `GitHub Repo <https://github.com/jupyter/nbconvert>`__, `Gitter Chat Room <https://gitter.im/jupyter/notebook>`__)
* nbformat (`Documentation <http://nbformat.readthedocs.org/en/latest/>`__, `GitHub Repo <https://github.com/jupyter/nbformat>`__, `Gitter Chat Room <https://gitter.im/jupyter/notebook>`__)

Education
---------

The following projects are focused on addressing the pain points of using the Jupyter Notebook in educational settings.

* nbgrader (`Documentation <http://nbviewer.ipython.org/github/jupyter/nbgrader/blob/docs/Index.ipynb>`__) (`GitHub Repo <https://github.com/jupyter/nbgrader>`__) (`Gitter Chat Room <https://gitter.im/jupyter/nbgrader>`__)

Deployment
----------

The following projects are being developed to support deploying the notebook in various contexts that include multiuser capabilities
and secure/scalable cloud deployments.

* jupyterhub (`GitHub Repo <https://github.com/jupyter/jupyterhub>`__, `Gitter Chat Room <https://gitter.im/jupyter/jupyterhub>`__)
* jupyter-drive (`GitHub Repo <https://github.com/jupyter/jupyter-drive>`__, `Gitter Chat Room <https://gitter.im/jupyter/jupyter-drive>`__)
* nbviewer (`GitHub Repo <https://github.com/jupyter/nbviewer>`__, `Gitter Chat Room <https://gitter.im/jupyter/nbviewer>`__)
* tmpnb (`GitHub Repo <https://github.com/jupyter/tmpnb>`__, `Gitter Chat Room <https://gitter.im/jupyter/tmpnb>`__)
* dockerspawner (`GitHub Repo <https://github.com/jupyter/dockerspawner>`__)
* tmpnb-deploy (`GitHub Repo <https://github.com/jupyter/tmpnb-deploy>`__)

Developer
---------

The following projects are lower level utilities used to build custom applications with the Jupyter architecture.

* jupyter_client (`Documentation <http://jupyter-client.readthedocs.org/en/latest/>`__, `GitHub Repo <https://github.com/jupyter/jupyter_client>`__, `Gitter Chat Room <https://github.com/jupyter/jupyter_client>`__)
* jupyter_core (`GitHub Repo <https://github.com/jupyter/jupyter_core>`__)

.. toctree::
   :hidden:

   install
   config
