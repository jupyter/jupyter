# February 23rd, 2021

**Date:** February 23, 2021, at 9am Pacific (your [timezone](https://arewemeetingyet.com/Los%20Angeles/2021-02-23/9:00/Jupyter%20Community%20Call))

[**Discourse:**](https://discourse.jupyter.org/t/jupyter-community-calls/668)

[**Youtube Link**](https://youtu.be/TG0w6WLunTk )

**Please note:**
- Community calls are recorded and posted to this [playlist](https://www.youtube.com/playlist?list=PLUrHeD2K9Cmkoamm4NjLmvXC4Y6E1o8SP)
- These notes will be recorded and posted [here](https://jupyter.readthedocs.io/en/latest/community/community-call-notes/index.html)
- Everyone present is held to the [Jupyter Code of Conduct](https://jupyter.org/conduct)

## Purpose

Think of it as a monthly, virtual JupyterCon. It’s a place to announce and share fun things happening in the Jupyter community.

For more discussion on the format of these calls, see the thread [here](https://discourse.jupyter.org/t/reviving-the-all-jupyter-team-meetings/423).

## Short reports, celebrations, shout-outs

* **Nick B**: Are you excited by... **JS license compliance**? Feedback welcome on [lab#9779](https://github.com/jupyterlab/jupyterlab/pull/9779) ([screenshot](https://user-images.githubusercontent.com/45380/108773016-c25f4880-752b-11eb-945c-32a20f2133b3.png))!
* **Nick B**: The latest [Lab RTC PR](https://github.com/jupyterlab/jupyterlab/pull/9785) ([demo](https://mybinder.org/v2/gh/QuantStack/jupyterlab/yjupyter?urlpath=lab-dev)) is 🔥!
* **Isabela Presedo-Floyd**: If you are interested in helping run or host a community call, let me know (you won't have to do it alone :sunflower:)!
* **Mike**: pyls fork [python-ls](https://github.com/python-ls/python-ls) in cooperation with the Spyder team; preview of the changes to come in my [personal fork](https://github.com/krassowski/python-language-server) (**fast** and more clever autocompletion for [jupyterlab-lsp](https://github.com/krassowski/jupyterlab-lsp)!)
* **Matt S**: [testbook](https://testbook.readthedocs.io/) had a talk at PyCascades around unittesting Jupyter Notebooks.

## Agenda Items

* **Loic Huder**: short presentation of [jupyter-h5web](https://github.com/silx-kit/jupyterlab-h5web), a JLab extension to explore/visualize HDF5 files
* **Jagane Sundar**: short presentation of InfinStor's free hosted Jupyterhub service (https://infinstor.com), a Cloud hosted free Jupyterhub - our Jupyterhub service is free, you pay for Jupyterlab instance resources consumed
* **Frédéric Collonval**: short presentation of [papermill_report](https://github.com/ariadnext/papermill_report). JupyterHub service to generate report from notebooks combining [papermill](https://papermill.readthedocs.io/en/latest/) and [nbconvert](https://github.com/ariadnext/papermill_report/blob/master/nbconvert.readthedocs.io).
* **Nick B**: [demo](http://mybinder.org/v2/gh/deathbeds/ipydrawio/master?urlpath=lab/tree/docs/Poster.dio.svg) of [ipydrawio](https://github.com/deathbeds/ipydrawio) (🍴 with 💖 of [@quantstack/jupyterlab-drawio](https://github.com/QuantStack/jupyterlab-drawio)), the full [diagrams.net](https://https://www.diagrams.net/) UI (with all plugins, themes, shapes...) for Lab 3. Supports `*.{ipynb,drawio,png,svg}` (plus `.pdf`, sorta)

## Other Links Shared

This is a space to store links shared during community call discussions related to or separate from the agenda items.

- agenda from [1/26 (last time)](https://hackmd.io/l2yBruUATC6yH4F2gOUPgw)
- h5web
    - based on same backend as other hd5f extension, will share more code in the future
      - other one's based on lumino datagrid
         - [merged cells](https://github.com/jupyterlab/lumino/pull/124) would be awesome 
    - keras: export [neural network weights](https://keras.io/api/models/model_saving_apis/) as hdf5, potential use case
    - xray community currently
      - viewer should work for all formats
    - [drug discovery](https://academic.oup.com/bioinformatics/article/35/8/1427/5094509)
    - preventing jlab from sending all the data
      - quick fix: filetype `base64` to just send a little data (custom contentsmanager?)
      - would prefer basically _no_ data...
- infinistor product 
  - hub 
    - custom spawner/authenticator (FOSS tbd)
      - didn't want existing spawner (container/k8s)
      - vm interface granular enough
      - stoppable machines for lower idle cost
      - requires infinistor
      - aws auth
      - token refreshing
    - hub runs on infinistor
    - spawns in your own aws, shutdown on 15m of idle
    - stock Lab, BYO extensions
    - custom tool for extensions
      - snapshots
    - dashboard
    - s3 storage
    - users 
    - multicloud (aws, azure)
    - customize the python kernel?
      - in backend, have transforms, use dockerfile, modify dockerfile
      - stock open source distributions (pip, conda)
- [show and tell on discourse](https://discourse.jupyter.org/c/general/show-and-tell/45)
- papermill_report
  - speaks python (other libraries could be added)
  - install as a service on hub
  - pick notebook
  - fill out form from papermill
  - click button, get report
  - shareable url
  - if break, get full traceback
  - click to get annotated notebook report
  - next time: integration testing jupyterlab, screenshots w/ playwright, etc.
  - papermill inspect added for this purpose, first example of using in FOSS
  - multi-step wizard?
    - schedulers
      - cylc
      - dagster
      - prefect
  - hiding code?
    - nbconvert (use [tags](https://nbconvert.readthedocs.io/en/latest/removing_cells.html#removing-pieces-of-cells-using-cell-tags)?)
    - preprocessors
    - all standard stuff 

- ipydrawio
  - > nb: most important takeaway: write the mimerenderer first, then it's easier to write a widget/document 
  - More draw.io features available in notebooks

  ## Attendees

| Name                  | Institution                       | GitHub Handle                     |
|-----------------------|-----------------------------------|-----------------------------------|
| Jagane                | InfinStor, Inc.                   | @jagane-opensource                |
| Loïc Huder            | ESRF                              | @loichuder                        |
| Frédéric Collonval    | ARIADNEXT                         | @fcollonval                       |
| Layne Sadler          | AIQC                              | @aiqc                             |
| Nick Bollweg          | GTRI, Project Jupyter             | @nrbgt @bollwyvl                  |
| Isabela Presedo-Floyd | Quansight Labs                    | @isabela-pf                       | 
| M. Krassowski (Mike)  | UOxf (on own behalf)              | @krassowski                       | 
| Simon Li              | University of Dundee              | @manics                           |
| Dan Lester            | Ideonate                          | @danlester                        |
| Wayne Decatur         | Upstate University                | @fomightez                        |
| Michael Milligan      | MSI @ U of Minnesota              | @mbmilligan                       |
| Matthew Seal          | Noteable, Inc                     | @mseal                            |
| Jose Ferro.           | EPO (www.epo.org)                 | @joseberlines                     |
| Marvin Kastner        | Hamburg University of Technology  | @1kastner                         |
| Zach Sailer           | Apple | @Zsailer |
| A. T. Darian          | Two Sigma | @afshin |
| W Stein               | CoCalc | @williamstein |
| Raja Rajendran        | InfinStor, Inc. | @software-artisan |
| Adhitya Vadivel       | InfinStor, Inc. | @adhityav |
| Jeremy Tuloup | QuantStack | @jtpio |
| Steven Silvester | Apple | @blink1073 |
| Safia Abdalla | Microsoft, nteract | @captainsafia |
| Shelby Sturgis| Netflix | @stormpython
| Pete Blois            | Google                            | @blois                            |