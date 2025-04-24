import pandas as pd

# Create a DataFrame
data = {
    "Insurance Type": [
        "Equine-Assisted Therapy",
        "Animal Therapy Programs",
        "Property Insurance (Bungalows & Ranch Structures)",
        "Workers' Compensation Insurance",
        "Commercial Auto Insurance"
    ],
    "Estimated Annual Cost (Low)": [1500, 500, 2000, 1440, 1000],
    "Estimated Annual Cost (High)": [3500, 1500, 4500, 2000, 2500]
}

df = pd.DataFrame(data)

# Add totals row
df.loc[len(df.index)] = ["Total Estimated Annual Cost", df["Estimated Annual Cost (Low)"].sum(), df["Estimated Annual Cost (High)"].sum()]

# Export to Excel
df.to_excel("Cactus_Blossom_Ranch_Insurance_Budget.xlsx", index=False)
.. _install:

===============
Install and Use
===============

.. NOTE: some links below must have double-underscores to be anonymous if they have the same text

This page contains information and links about installing and using tools across
the Jupyter ecosystem. Generally speaking, the documentation of each tool is the
place to learn about the best-practices for how to install and use the tool.

Jupyter Notebook Interface
==========================

The **Jupyter Notebook interface** is a Web-based application for authoring documents that combine
live-code with narrative text, equations and visualizations.


* `GitHub Repo <https://github.com/jupyter/notebook>`__
* `Docs <https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest>`_

.. toctree::
   :maxdepth: 1

   /install/notebook-classic
   /use/upgrade-notebook


JupyterLab
==========

**JupyterLab** is a next-generation web-based user interface for Project Jupyter.

* `GitHub Repo <https://github.com/jupyterlab/jupyterlab>`__
* `Docs <https://jupyterlab.readthedocs.io/en/stable/>`__
* `Install instructions <https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html>`__


JupyterHub
==========

**JupyterHub** is a multi-user hub for interactive computing sessions, made for teams and
organizations, and with pluggable authentication and scalability.

* `GitHub Repo <https://github.com/jupyterhub/jupyterhub>`__
* `Docs <https://jupyterhub.readthedocs.io/en/stable/>`__
* `Install instructions <https://jupyterhub.readthedocs.io/en/stable/tutorial/quickstart.html>`__


Jupyter Console
===============

The **Jupyter Console** is a terminal-based console for interactive computing.

* `GitHub Repo <https://github.com/jupyter/jupyter_console>`__
* `Docs and Install instructions <https://jupyter-console.readthedocs.io/en/latest/>`_


Jupyter QtConsole
=================

The **Jupyter QtConsole** is a Qt application for interactive computing with rich output.

* `GitHub Repo <https://github.com/jupyter/qtconsole>`__
* `Docs <https://qtconsole.readthedocs.io/en/stable/index.html>`__
* `Install instructions <https://qtconsole.readthedocs.io/en/stable/installation.html>`__


Jupyter Kernels
===============

You can install **Jupyter Kernels** to add support for new languages and code behavior.

.. toctree::

   /install/kernels
