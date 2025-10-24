#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Jupyter documentation build configuration file.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
import sys
import os
import shlex

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

html_theme = 'pydata_sphinx_theme'
html_logo = '_static/_images/jupyter.svg'
html_favicon = '_static/_images/favicon.png'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.graphviz', # Add the graphviz extension
    'sphinxext.rediraffe',
    'myst_parser',
    'sphinx_design',
]

panels_add_bootstrap_css = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Jupyter Documentation'
copyright = '2015, Jupyter Team, https://jupyter.org'
author = 'The Jupyter Team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '4.1'
# The full version, including alpha/beta/rc tags.
release = '4.1.1 alpha'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    # "github_url": "https://github.com", # or your GitHub Enterprise interprise
    "github_user": "jupyter",
    "github_repo": "jupyter",
    "github_version": "master",
    "doc_path": "docs/source",
}

html_theme_options = {
    "announcement": "🚀 Join us in San Diego · JupyterCon 2025 · Nov 4-5 · <a href=\"https://events.linuxfoundation.org/jupytercon/program/schedule/?ajs_aid=53afb00d-be65-4a99-9112-28cdaac99463\">SCHEDULE</a> · <a href=\"https://events.linuxfoundation.org/jupytercon/register/?ajs_aid=53afb00d-be65-4a99-9112-28cdaac99463\">REGISTER NOW</a>",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/jupyter/jupyter",
            "icon": "fab fa-github-square",
        },
        {
            "name": "Discourse",
            "url": "https://discourse.jupyter.org",
            "icon": "fab fa-discourse",
        },
    ],
  "external_links": [
      {"name": "jupyter.org", "url": "https://jupyter.org"},
  ],
  "use_edit_page_button": True,
  "logo": {
      "image_dark": "_static/_images/logo-rectangle-dark.svg",
  },
}

# Re-directs for pages that were moved
rediraffe_redirects = {
    "content-quickstart.rst": "start/index.md",
    "tryjupyter.rst": "start/index.md",
}

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%Y-%m-%d'

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {}

# Output file base name for HTML help builder.
htmlhelp_basename = 'Jupyter'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {

}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Jupyter.tex', 'Jupyter Documentation',
     'https://jupyter.org', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'jupyter', 'Jupyter Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Jupyter', 'Jupyter Documentation',
     author, 'Jupyter', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for intersphinx -----------------------------------------------

from intersphinx_registry import get_intersphinx_mapping

intersphinx_mapping = get_intersphinx_mapping(
    packages={
        "ipython",
        "nbconvert",
        "nbformat",
        "ipywidgets",
        "traitlets",
        "ipyparallel",
        "notebook",
        "jupyterclient",
        "qtconsole",
        "jupytercore",
        "hub",
        "lab",
    }
)


intersphinx_cache_limit = 5

# -- Options for graphviz ----------------------------------------------------
# The following section is needed to enable links within graphviz generated diagrams
# note that these will only work if, in addition to specifying href= they also give
# target="_top" or target="_blank" for open in the same window/tab or in a new one.
graphviz_output_format = 'svg'
# Note for Windows users:
# If you receive a warning about dot not found you may need make sure Graphviz is
# installed and to specify its location with:
# -D graphviz_dot="C:\Program Files (x86)\Graphviz2.38\bin\dot.exe"
# if calling sphinx-build directly - if using the make.bat file first do:
# set SPHINXOPTS=-D graphviz_dot="C:\Program Files (x86)\Graphviz2.38\bin\dot.exe"
# or similar, if all else fails, something like:
# graphviz_dot=r'c:\Program Files (x86)\Graphviz2.38\bin\dot.exe'
# with your path to graphviz in should work if added to this file.
# BUT Please do not commit with the path on your computer in place.

# -- Translation ----------------------------------------------------------

gettext_uuid = True
locale_dirs = ['locale/']


def setup(app):
    app.add_css_file("custom.css")
    app.add_css_file("jupyter.css")

    # Enable Plausible.io stats
    app.add_js_file("https://plausible.io/js/pa-B75UO5--FNXYQSG7GBWkf.js", loading_method="async")
    app.add_js_file(
        filename=None,
        body="window.plausible=window.plausible||function(){(plausible.q=plausible.q||[]).push(arguments)},plausible.init=plausible.init||function(i){plausible.o=i||{}};plausible.init({hashBasedRouting:true})",
    )
