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

- Notebook (`Documentation <http://jupyter-notebook.readthedocs.org/en/latest/>`_, `GitHub Repo <https://github.com/jupyter/notebook>`_, `Gitter Chat Room <https://gitter.im/jupyter/notebook>`_)  
- Console (`GitHub Repo <https://github.com/jupyter/jupyter_console>`_, `Gitter Chat Room <https://gitter.im/jupyter/jupyter_console>`_)
- QtConsole (`Documentation <http://qtconsole.readthedocs.org/en/latest/>`_, `GitHub Repo <https://github.com/jupyter/qtconsole>`_, `Gitter Chat Room <https://gitter.im/jupyter/qtconsole>`_)  

Kernels
-------

Kernels are separate processes that sit behind the Jupyter user interfaces and run code in a particular programming language.

* Python
    - IPython Kernel (`Documentation <http://ipython.readthedocs.org/en/master/>`_, `GitHub Repo <https://github.com/ipython/ipython>`_, `Gitter Chat Room <https://gitter.im/ipython/ipython>`_)  
    - Traitlets (`Documentation <http://traitlets.readthedocs.org/en/latest/>`_, `GitHub Repo <https://github.com/ipython/traitlets>`_, `Gitter Chat Room <https://gitter.im/ipython/ipython>`_)
    - Parallel Computing (`Documentation <http://ipyparallel.readthedocs.org/en/latest/>`_, `GitHub Repo <https://github.com/ipython/ipyparallel>`_, `Gitter Chat Room <https://gitter.im/ipython/ipyparallel>`_)
    - Interactive Widgets (`Documentation <http://ipyparallel.readthedocs.org/en/latest/>`_, `GitHub Repo <https://github.com/ipython/ipywidgets>`_, `Gitter Chat Room <https://gitter.im/ipython/ipywidgets>`_)
* R
    - IRkernel (`Documentation <http://irkernel.github.io/>`_, `GitHub Repo <https://github.com/IRkernel/IRkernel>`_)
    - IRdisplay (`GitHub Repo <https://github.com/IRkernel/IRdisplay>`_)
    - repr (`GitHub Repo <https://github.com/IRkernel/repr>`_)
* Julia
     - IJulia Kernel (`GitHub Repo <https://github.com/JuliaLang/IJulia.jl>`_)
     - Interactive Widgets (`GitHub Repo <https://github.com/JuliaLang/Interact.jl>`_)
* Bash (`GitHub Repo <https://github.com/takluyver/bash_kernel>`_)

See `this page <https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages>`_ for a full list of kernels available for other languages.

Working with Notebooks
----------------------

Notebooks are interactive documents that combine live code, narrative text (markdown), visualizations and other rich media. The following projects
allow the programmatic convertion and manipulation of notebook documents.

* nbconvert (`Documentation <http://nbconvert.readthedocs.org/en/latest/>`_, `GitHub Repo <https://github.com/jupyter/nbconvert>`_, `Gitter Chat Room <https://gitter.im/jupyter/notebook>`_)
* nbformat (`Documentation <http://nbformat.readthedocs.org/en/latest/>`_, `GitHub Repo <https://github.com/jupyter/nbformat>`_, `Gitter Chat Room <https://gitter.im/jupyter/notebook>`_)

Education
---------

The following projects are focused on addressing the pain points of using the Jupyter Notebook in educational settings.

* nbgrader (`Documentation <http://nbviewer.ipython.org/github/jupyter/nbgrader/blob/docs/Index.ipynb>`_) (`GitHub Repo <https://github.com/jupyter/nbgrader>`_) (`Gitter Chat Room <https://gitter.im/jupyter/nbgrader>`_)

Deployment
----------

The following projects are being developed to support deploying the notebook in various contexts that include multiuser capabilities
and secure/scalable cloud deployments.

* jupyterhub (`GitHub Repo <https://github.com/jupyter/jupyterhub>`_, `Gitter Chat Room <https://gitter.im/jupyter/jupyterhub>`_)
* jupyter-drive (`GitHub Repo <https://github.com/jupyter/jupyter-drive>`_, `Gitter Chat Room <https://gitter.im/jupyter/jupyter-drive>`_)
* nbviewer (`GitHub Repo <https://github.com/jupyter/nbviewer>`_, `Gitter Chat Room <https://gitter.im/jupyter/nbviewer>`_)
* tmpnb (`GitHub Repo <https://github.com/jupyter/tmpnb>`_, `Gitter Chat Room <https://gitter.im/jupyter/tmpnb>`_)
* dockerspawner (`GitHub Repo <https://github.com/jupyter/dockerspawner>`_)
* tmpnb-deploy (`GitHub Repo <https://github.com/jupyter/tmpnb-deploy>`_)

Developer
---------

The following projects are lower level utilities used to build custom applications with the Jupyter architecture.

* jupyter_client (`Documentation <http://jupyter-client.readthedocs.org/en/latest/>`_, `GitHub Repo <https://github.com/jupyter/jupyter_client>`_, `Gitter Chat Room <https://github.com/jupyter/jupyter_client>`_)
* jupyter_core (`GitHub Repo <https://github.com/jupyter/jupyter_core>`_)

.. toctree::
   :hidden:

   install
