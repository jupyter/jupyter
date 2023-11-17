# Jupyter Community Call 
## January 26th, 2021

**Date:** January 26, 2021, at 9am Pacific (your [timezone](https://arewemeetingyet.com/Los%20Angeles/2021-01-26/9:00/Jupyter%20Community%20Call))

[**Discourse**](https://discourse.jupyter.org/t/jupyter-community-calls/668)

[**YouTube Link**](https://youtu.be/DS_J3mzulCw)

**Please note:**
- Community calls are recorded and posted to this [playlist](https://www.youtube.com/playlist?list=PLUrHeD2K9Cmkoamm4NjLmvXC4Y6E1o8SP)
- These notes will be recorded and posted [here](https://jupyter.readthedocs.io/en/latest/community/community-call-notes/index.html)
- Everyone present is held to the [Jupyter Code of Conduct](https://jupyter.org/conduct)

## Purpose

Think of it as a monthly, virtual JupyterCon. It’s a place to announce and share fun things happening in the Jupyter community.

For more discussion on the format of these calls, see the thread [here](https://discourse.jupyter.org/t/reviving-the-all-jupyter-team-meetings/423).

## Short reports, celebrations, shout-outs

This is a place to make short announcements (without a need for discussion). 

* **Frédéric Collonval** To improve visibility and group volunteer time on maintenance of popular JupyterLab 
extensions, a unofficial GitHub organization has been created: [jupyterlab-contrib](https://github.com/jupyterlab-contrib).
* **Isabela Presedo-Floyd** In case you missed it, [JupyterLab 3.0 is out](https://blog.jupyter.org/jupyterlab-3-0-is-out-4f58385e25bb)! Congrats to the community and thanks for all 
the hard work that went into this release.
* **Isabela Presedo-Floyd** I've seen a resurgence of community interest in making multiple Jupyter projects accessible.
This is awesome! We also have a group of people meeting every other week to coordinate JupyterLab accessibility work (and 
talk about accessibility in general) that you can join from the [community calendar](https://jupyter.readthedocs.io/en/latest/community/content-community.html#jupyter-community-meetings).
* **Layne Sadler** Plotly updated jupyter-dash labextension for 3.0 and vows to prebuild. [issue](https://github.com/plotly/jupyter-dash/issues/49)

## Agenda Items

* **Nick Bollweg** [jupyterlab-lsp 3.2](https://pypi.org/project/jupyterlab-lsp/) on `pypi` & `conda-forge`. JupyterLab
:three:. :eight: _[Language Client](https://langserver.org)_ features. Ju(lia)+Py(thon)+R _Language Servers_+_Kernel_+_Notebook_, 
plus [more](https://jupyterlab-lsp.readthedocs.io/en/latest/Language%20Servers.html). [Pre-JEP Issue](https://github.com/jupyter/enhancement-proposals/issues/67)
to move towards an official sub-project 🚀.
* **Nick Bollweg** (_or someone better :muscle:_) [JupyterLab 2.3.0rc0](https://github.com/jupyterlab/jupyterlab/blame/2.3.x/docs/source/getting_started/changelog.rst#L6-L12)
is a performance-focused prerelease, on `pypi`/`conda-forge`, these features will land in 3.1. Ready for
[testing](https://github.com/robots-from-jupyter/robotframework-jupyterlibrary/pull/34)!
* **Frédéric Collonval**: Leverage JupyterLab modularity to customize the UI with a alternative 
[launcher](https://github.com/jupyterlab-contrib/jlab-enhanced-launcher) and a [cell toolbar](https://github.com/jupyterlab-contrib/jlab-enhanced-cell-toolbar) - demonstrate easier distribution thanks to JLab3.
* **Corentin Cadiou**: presentation of [ipysphaghetti](https://github.com/cphyc/node_editor) (name not settled yet) a JLab 
(3+) extension implementing a node-based approach to interact with your data.
* **Thorin Tabor:** Notebook Projects, a mechanism for encapsulating multiple user environments in a JupyterHub instance

## Other Links Shared

- Take the [Jupyter survey](https://blog.jupyter.org/survey-jupyterlab-and-beyond-88c7fbd27a79)!
- some nteract links after @raman's pre-demo:
  - https://docs.nteract.io/getting-started-with-nteract/
  - https://github.com/nteract/nteract
- semi-related "instant-on" compute/notebooks
  - [jyve](https://deathbeds.github.io/jyve/lab/), static JupyterLab build
  - [pyodide](https://github.com/iodide-project/pyodide), full CPython in the browser
- hackmd's FOSS flavor is now [HedgeDoc](https://github.com/hedgedoc/hedgedoc)
  - we need a Hub/Lab Extension :hedgehog:
- "run cells with tags"
  - from `cell-toolbar` demo
  - could this be supported in multiple clients, e.g. _JupyterLab Notebook_ UI and `nbclient`/`nbconvert` CLI
- workflows with (some) Jupyter integration
  - [cylc](https://github.com/cylc/cylc-ui/issues/90)
  - [dask](https://docs.dask.org/en/latest/graphs.html)
  - [dagster](https://github.com/dagster-io/dagster) ([binder](https://gist.github.com/bollwyvl/0fe7a6f89251992ab1a542ac2b4051c4))
  - [openmdao](https://github.com/OpenMDAO/OpenMDAO)
  - [prefect](https://stories.dask.org/en/latest/prefect-workflows.html)
- [GenePattern](https://github.com/genepattern) and [GenePatternNotebook](https://notebook.genepattern.org/#gsc.tab=0)
- [Integrative Genetics Viewer](http://software.broadinstitute.org/software/igv/) and their [Jupyter extension](https://github.com/igvteam/igv-jupyter)


## Q/A

> **As a company, how do we start contributing?**
> - @willingc follow the projects that seem most within your team's wheelhouse
>   - Visit the Jupyter [Discourse](https://discourse.jupyter.org/) and [community calendar](https://discourse.jupyter.org/t/jupyter-community-calendar/2485)!
> - @jasongrout JupyterLab [4.0 release plans](https://github.com/jupyterlab/jupyterlab/issues/9647) are underway. There may be items there, or things you want to contribute.
>   - translations always welcome! Check [CrowdIn](https://crowdin.com/project/jupyterlab) for more info.
>   - [corporate guidance](https://github.com/jupyterlab/jupyterlab/blob/master/CORPORATE.md)
>   - [team compass](https://github.com/jupyterlab/team-compass) is where many of these larger discussions may happen.
> - @jupyter/notebook is very starved for resources
>   - has a weekly meeting just trying to keep the issue count down.
>     - many are low-touch to at least get triaged
>   - really any help welcome
> - @isabela-pf accessibility on all projects.
>   - We have been starting with JupyterLab Components, etc. Notes for our meetings and all current team work live in [this issue](https://github.com/jupyterlab/team-compass/issues/98)
>   - And documentation in [pydata-sphinx-theme](https://github.com/pandas-dev/pydata-sphinx-theme/pull/294)  (upstream of `jupyter-book`, etc.)

> **What would you like to see in community calls?**
> - Overview of JupterLab 3

## Attendees
|   Name             |           Institution         | GitHub Handle                     |
|--------------------|-------------------------------|-----------------------------------|
| Ross Stokoe        | Refinitiv                     | @RR11WK                           |
| Julien Hoarau      | Refinitiv                     | @julienhoarau                     |
| Greg Olmstead      | Refinitiv                     | @maynardflies                     |
| Josias De Lima     | Refinitiv                     | @JoshDL                           |
| Loic Huder         | ESRF                          | @loichuder                        | 
| Thorin Tabor       | UCSD                          | @tmtabor                          |
| Gonzalo Gasca Meza | Google                        | @gogasca                          |
| Frédéric Collonval | ARIADNEXT                     | @fcollonval                       | 
| Layne Sadler       | free agent                    | @aiqc                             |
| Corentin Cadiou    | University College London     | @cphyc                            |
| Nick Bollweg       | Proj. Jupyter, GTRI, Deathbeds| @bollwyvl @nrbgt @deathbeds       |
| Wayne Decatur      | Upstate Medical Universtity   | @fomightez                        |
| Zach Sailer        | Apple                         | @Zsailer                          |
| Simon Li           | University of Dundee          | @manics                           |
| Raman Tehlan       | nteract, StockGro             | @ramantehlan                      |
| Pete Blois         | Google Colab                  | @blois                            |
| Ryan Spencer       | GTRI                          | @ryspnc                           |
| A. T. Darian       | Two Sigma                     | @afshin                           |
| Carol Willing      | Noteable / Jupyter            | @willingc                         |
| Karla Spuldaro     | IBM                           | @karlaspuldaro                    |
| Martha Cryan       | IBM                           | @marthacryan                      |
| Isabela Presedo-Floyd | Quansight Labs             | @isabela-pf                       |
