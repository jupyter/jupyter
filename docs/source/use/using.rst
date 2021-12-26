=====
Usage
=====

Information relevant to using the various tools in the Jupyter
ecosystem.

.. TODO: this is hidden because there's a bug in the pydata theme that won't render TOC items under headers

.. toctree::
   :hidden:

   use-cases/content-user
   ../install
   jupyter-command
   jupyter-directories
   config
   advanced/content-advanced


Use and Configure
=================

.. toctree::
   :maxdepth: 1

   jupyter-command
   jupyter-directories
   config


How do I decide which packages I need?
======================================

Jupyter can be used for many different use-cases. Below are a few user stories
for when and how you might use tools in the Jupyter ecosystem, as well as a diagram
that helps lay out some of your options.

.. toctree::

   use-cases/content-user

.. graphviz::

	digraph decide_project {
		size="10,4";
		graph [fontname = "helvetica", fontsize="18"];
		node [fontname = "helvetica", fontsize="18"];
		edge [fontname = "helvetica", fontsize="18"];
        label = "Note:\nGreen ringed shapes are links on this site and open in this window\nBlue ones are links to external sites and open in a new tab/window."
		tooltip="How do I decide which packages I need?";
		// Top Level
		what [
			shape=parallelogram,
			label="What are you\ntrying to do?",
			tooltip="You have several possibilities!",
			style=filled, color=".3 .7 1.0"]
		// Second Level
		try [
			shape=box,
			label="Try the notebook",
			tooltip="Try the Jupyter notebook!"]
		install [shape=box,
			label="Install the notebook",
			tooltip="Go To Install Jupyter!"]
		team [
			shape=box,
			label="Install notebooks\n for my team, class,\n or group",
			tooltip="Install for teams, etc!"]
		convert [
			shape=box,
			label="Convert my\n notebook file to\n another format",
			tooltip="Convert to other formats."]
		lang [
			shape=box,
			label="Use another\n programming\n language such as\n R or Java",
			tooltip="Use other programming languages."]
		custom [
			shape=box,
			label="Customize the\n notebook for my\n needs",
			tooltip="Customize Notebooks."]
		// 3rd Level
		online [
			label="Try Online",
			tooltip="Try Notebooks Online - without any installation!",
			target="_blank", color=blue, // External Link
			href="https://try.jupyter.org/"]
		doinstall [
			label="Install Jupyter",
			tooltip="How to install",
			target="_top", color=green, // Local Link
			href="../install.html"] // 4th level
		hub [
			label="JupyterHub",
			tooltip="Install JupyterHub",
			target="_blank", color=blue, // External Link
			href="https://github.com/jupyterhub/jupyterhub"]
		nbconvert [
			label="nbconvert",
			tooltip="How to convert notebooks",
			target="_blank", color=blue, // External Link
			href="https://nbconvert.readthedocs.io/en/latest/"]
		kernel [
			label="Install a\nlanguage\nkernel",
			tooltip="How to install kernels",
			target="_top", color=green, // Local Link
			href="../projects/subprojects.html?highlight=jupyterhub#kernels"]
		// Path labels
		noinst [
			shape=plaintext,
			label="No installation\nneeded!",
			tooltip="Don't wish to install yet?"]
		like [
			shape=plaintext,
			label="I like it,\nand I wish to install it!",
			tooltip="You like it!"]
		my [
			shape=plaintext,
			label="On my system",
			tooltip="Local Installation"]
		// below kernel
		widgets [
			label="Widgets",
			tooltip="Install & use ipywidgets",
			target="_blank", color=blue, // External Link
			href="https://ipywidgets.readthedocs.io/en/latest/"]
		extend [
			label="Extensions",
			tooltip="Install & use extensions",
			target="_blank", color=blue, // External Link
			href="https://github.com/ipython-contrib/IPython-notebook-extensions"]
		dash [
			label="Dashboards",
			tooltip="Install & use dashboards",
			target="_blank", color=blue, // External Link
			href="https://github.com/jupyter/dashboards"]
		help [
			label="Help",
			tooltip="Ask on jupyter help",
			target="_blank", color=blue, // External Link
			href="https://github.com/jupyter/help"]
		// Edges
		what -> {try install team convert lang custom}
		try -> noinst -> online
		online -> like -> doinstall
		install -> my -> doinstall
		team -> hub
		convert -> nbconvert
		lang -> kernel
		custom -> {widgets extend dash help}
		// Arrangement
		{rank=same; what}
		{rank=same; try; install; team; convert; lang; custom;}
		{rank=same; widgets; extend;}
		{rank=same; my; dash; help;}
	}

Advanced topics
===============

.. toctree::

   advanced/content-advanced
