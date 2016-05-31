.. _content-projects:

Installation, Configuration, and Usage
======================================

Installation
------------

.. toctree::
   :maxdepth: 1

   ../install
   upgrade-notebook
   ../install-kernel

How do I decide which packages I need?
--------------------------------------

.. graphviz::

	digraph decide_project {
		size="10,4";
		// Top Level
		//label="How do I decide which pakages I need?";
		tooltip="How do I decide which pakages I need?";
		what [shape=parallelogram, label="What are you\ntrying to do?", style=filled, color=".3 .7 1.0"]
		// Second Level
		try [shape=box, label="Try the notebook"]
		install [shape=box, label="Install the notebook", tooltip="Go To Install Jupyter"]
		team [shape=box, label="Install notebooks\n for my team, class,\n or group"]
		convert [shape=box, label="Convert my\n notebook file to\n another format"]
		lang [shape=box, label="Use another\n programming\n language such as\n R or Java"]
		custom [shape=box, label="Customize the\n notebook for my\n needs"]
		// 3rd Level
		online [label="Try Online", href="https://try.jupyter.org/", target="_blank", tooltip="Try Online", style=underline, color=blue,]
		doinstall [label="Install Jupyter", tooltip="How to install", href="../install.html", target="_top", color=green,] // 4th level
		hub [label="Jupyter Hub", tooltip="Install Jupyter Hub", target="_blank", color=blue, href="https://github.com/jupyterhub/jupyterhub"]
		nbconvert [label="nbconvert", tooltip="How to convert notebooks", target="_blank", color=blue, href="https://nbconvert.readthedocs.io/en/latest/"]
		kernel [label="Install a\n language\nkernel", tooltip="How to install kernels", target="_top", color=green, href="../projects/subprojects.html?highlight=jupyterhub#kernels"]
		noinst [shape=plaintext, label="No installation\nneeded!", color=blue]
		like [shape=plaintext, label="I like it,\nand I wish to install it!", color=blue]
		my [shape=plaintext, label="On my system", tooltip="Local Installation", color=blue]
		// below kernel
		widgets [label="Widgets", tooltip="Install & use ipywidgets", target="_blank", color=blue, href="https://ipywidgets.readthedocs.io/en/latest/"]
		extend [label="Extensions", tooltip="Install & use extentions", target="_blank", color=blue, href="https://github.com/jupyter/help"]
		dash [label="Dashboards", tooltip="Install & use dashboards", target="_blank", color=blue, href="https://github.com/ipython-contrib/IPython-notebook-extensions"]
		help [label="Help", tooltip="Ask on jupyter help", target="_blank", color=blue, href="https://github.com/jupyter/help"]
		// Edges
		what -> {try install team convert lang custom}
		try -> noinst -> online
		online -> like -> doinstall
		install -> my -> doinstall
		team -> hub
		convert -> nbconvert
		lang -> kernel
		custom -> {widgets extend dash help}
		// Arangement
		{rank=same; what}
		{rank=same; try; install; team; convert; lang; custom;}
		{rank=same; widgets; extend;}
		{rank=same; my; dash; help;}
	}


Configuration
-------------

.. toctree::
   :maxdepth: 1

   jupyter-command
   jupyter-directories
   config

Usage and Projects
------------------

.. toctree::
   :maxdepth: 1

   subprojects
   ipython_projects
   incubator
   kernels
   doc-proj-categories
