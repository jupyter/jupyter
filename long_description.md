# Jupyter metapackage

Find more information on [the Jupyter homepage](https://jupyter.org).

## A default installation of most common Jupyter packages

`pip install jupyter` installs the Jupyter Notebook, JupyterLab, and the IPython Kernel.

This is an empty metapackage for user convenience,
only expressing dependencies on multiple Jupyter packages.
`jupyter` should not be used as a dependency for any packages.

For more efficient installation of what you need,
all Jupyter components installed by `pip install jupyter` can be installed separately.
For example:

- `notebook` - Jupyter Notebook
- `jupyterlab` - JupyterLab (added to metapackage v1.1)
- `ipython` - IPython (terminal)
- `ipykernel` - IPython Kernel for Jupyter
- `jupyter-console` - terminal Jupyter client
- `nbconvert` - convert notebooks between formats
- `ipywidgets` - interactive widgets package for IPython

No longer included in `pip install jupyter`, but still supported:

- `qtconsole` - Qt Console (removed in metapackage v1.1)
