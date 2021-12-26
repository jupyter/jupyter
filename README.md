# Jupyter

*Read this in other languages: [English](README.md), [Español](README.es-ES.md), [Português](README.pt-BR.md)*

Jupyter metapackage for installation and docs.

## Documentation structure

This documentation uses the [Sphinx](https://sphinx-doc.org) documentation engine.

The documentation is located in the `docs/source` folder. When you build the documentation, it will be placed in the `docs/build` folder.
It is written in a combination of [reStructuredText](https://docutils.sourceforge.io/rst.html) and [MyST Markdown](https://myst-parser.readthedocs.io/).

## Build the documentation locally

There are a few ways to build the documentation, see below for instructions:

### Build the documentation automaticlaly with `nox`

The easiest way to build the documentation locally is by using the [`nox` command line tool](https://nox.thea.codes/). This tool makes it easy to automate commands in a repository, and we have included a `docs` command to quickly install the dependencies and build the the documentation.

To build and preview the site locally, follow these steps:

1. **Clone this repository**.
   
   ```console
   $ git clone https://github.com/jupyter/jupyter
   $ cd jupyter
   ```
2. **Install `nox`**

   ```console
   $ pip install nox
   ```
3. **Run the `docs` command**
   
   ```console
   $ nox -s docs
   ```

This will install the needed dependencies in a virtual environment using `pip`.
It will then place the documentation in the `docs/build/html` folder.
You may explore these HTML files in order to preview the site.

#### Create a live server to automatically preview changes

There is another `nox` command that will do the above, and also create a live server that watches your source files for changes, and auto-builds the website any time a change is made.

To start this live server, use the following `nox` command:

```console
$ nox -s docs-live
```

When the build is finished, go to the URL that is displayed. It should show a live preview of your doucmentation.

To stop serving the website, press **`Ctrl`**-`C` in your terminal

### Build the documentation manually

To build the documentation manually, follow these steps:

First, install [the `miniconda` Python distribution](https://conda.io/miniconda.html).

Next, navigate to the `/docs` directory and create a `conda` environment:

```bash
conda env create -f environment.yml  
```  

Activate the environment:

```bash
source activate jupyter_docs  
```

**Build the docs** using Sphinx with the following commands:

```bash
make clean  
make html
```

The docs will be built in `build/html`. They can be viewed by opening `build/html/index.html` or starting an HTTP server and navigating to `0.0.0.0:8000` in your web browser.

```bash
python3 -m http.server
```
