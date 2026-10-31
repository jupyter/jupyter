.. _data_science:

========================
Jupyter for Data Science
========================

The purpose of this page is to highlight kernels and other projects that are
central to the usage of Jupyter in data science. This page is not meant to be
comprehensive or unbiased, but rather to provide an opinionated view of the
usage of Jupyter in data science based on our interactions with users.

The following Jupyter kernels are widely used in data science:

* python
    - IPython (`GitHub Repo <https://github.com/ipython/ipykernel>`__)
* R
    - IRkernel (`Documentation <https://irkernel.github.io/>`__, `GitHub Repo <https://github.com/IRkernel/IRkernel>`__)
    - IRdisplay (`GitHub Repo <https://github.com/IRkernel/IRdisplay>`__)
    - repr (`GitHub Repo <https://github.com/IRkernel/repr>`__)
* Julia
     - IJulia Kernel (`GitHub Repo <https://github.com/JuliaLang/IJulia.jl>`__)
     - Interactive Widgets (`GitHub Repo <https://github.com/JuliaLang/Interact.jl>`__)
* Bash (`GitHub Repo <https://github.com/takluyver/bash_kernel>`__)

Querying Redis from a Python notebook
=====================================

Python kernels can use the external Redis ADBC driver to query Redis SQL data
and fetch Arrow tables for pandas or NumPy analysis. Install the driver in the
kernel's Python environment, configure the Redis endpoint before starting the
kernel, and run Redis separately with Search enabled.

The `Redis ADBC notebook guide
<https://github.com/redis/redis-adbc-driver/blob/a48432273a0f9978e893bca27057b9f128e7603e/docs/integrations/jupyter.md>`_
includes installation, kernel selection and a complete query example.
A remote kernel needs its own driver installation and network access to Redis;
installing a package on the browser's computer does not configure that kernel.
This is a Python-client workflow, not a built-in Jupyter database connector.
