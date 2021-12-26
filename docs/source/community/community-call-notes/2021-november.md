# November 30, 2021

**Date:** Novermber 30, 2021, at 8am Pacific (your [timezone](https://arewemeetingyet.com/Los%20Angeles/2021-11-30/8:00/Jupyter%20Community%20Call))

**[Discourse](https://discourse.jupyter.org/t/jupyter-community-calls/668)**

**[YouTube link](https://youtu.be/_YdiFgWUHNI)** 

**Please note:**
- Community calls are recorded and posted to this [playlist](https://www.youtube.com/playlist?list=PLUrHeD2K9Cmkoamm4NjLmvXC4Y6E1o8SP)
- These notes will be recorded and posted [here](https://jupyter.readthedocs.io/en/latest/community/community-call-notes/index.html)
- Everyone present is held to the [Jupyter Code of Conduct](https://jupyter.org/conduct)

## Purpose

Think of it as a monthly, virtual JupyterCon. It’s a place to announce and share fun things happening in the Jupyter community.

For more discussion on the format of these calls, see the thread [here](https://discourse.jupyter.org/t/reviving-the-all-jupyter-team-meetings/423).

## Short reports, celebrations, shout-outs

This is a place to make short announcements (without a need for discussion). 

* **@loichuder:** Release 1.0.0 of [jupyterlab-h5web](https://github.com/silx-kit/jupyterlab-h5web) bringing support for JLab3 as prebuilt extension 🎉
* **@bollwyvl** `jupyterlite 0.1.0a17` speaks self-hosted/custom wheels and MathJax
  * [offline pyodide](https://jupyterlite--425.org.readthedocs.build/en/425/_static/lab/index.html) coming
    * [jupyter-server-proxy 3.2.0](https://github.com/jupyterhub/jupyter-server-proxy/blob/main/CHANGELOG.md#320---2021-11-29) including full control of request re-writing, sub-paths in Lab launchers 

## Agenda Items

* **@ltetrel** jupyter book workflow on [NeuroLibre](https://www.neurolibre.org/)
    * [NeuroLibre Documentation](https://docs.neurolibre.org/en/latest/) (you are welcome to be an alpha tester!))
    * This is the [pull request for initContainer on binderhub](https://github.com/jupyterhub/binderhub/pull/1081). It should be already possible with [Zero to JupyterHub singleuser.initContainers](https://zero-to-jupyterhub.readthedocs.io/en/latest/resources/reference.html#singleuser-initcontainers) but not optimal (better to do our process once during build). The missing piece is to give that initContainer an environment variable ([as discussed on the github issue](https://github.com/jupyterhub/binderhub/issues/1429) and [Jupyter discourse](https://discourse.jupyter.org/t/feature-idea-jupyterhub-binderhub-jupyter-book-as-a-publishing-platform/8359/8?u=ltetrel)).
* **@fcollonval** [WIP RISE in JupyterLab PR](https://github.com/damianavila/RISE/pull/605)

  To test the PR locally, here are the commands to execute:
  ```sh
    yarn 
    yarn build
    python3 -m pip install -e .
    jupyter server extension enable --sys-prefix rise
    jupyter serverextension enable --sys-prefix rise
    jupyter labextension develop --overwrite .
  ```

* **@afshin** `[DRAFT]` Jupyter Enhancement Proposal (JEP) for [Jupyter Notebook version 7](https://github.com/jupyter/enhancement-proposals/pull/79)
    * Also mentioned on the [Jupyter Discourse](https://discourse.jupyter.org/t/jep-draft-open-for-the-notebook-v7-transition/11769)

## Other Links Shared

This is a space to store links shared during community call discussions related to or separate from the agenda items.

- [The Journal of Open Source Software](https://joss.theoj.org/)
- [Comment on Jupyter Discourse post Feature Idea: JupyterHub/BinderHub + Jupyter Book as a publishing platform](https://discourse.jupyter.org/t/feature-idea-jupyterhub-binderhub-jupyter-book-as-a-publishing-platform/8359/3)
- [Darian's sweet potato pie recipe](https://food.darian.link/sweet-potato-pie/)
- [Cooking for Engineers](http://www.cookingforengineers.com/)
- [jupyterlab/jupyterlab issue #10207 Side-by-side rendering](https://github.com/jupyterlab/jupyterlab/issues/10207)

## Comments

- Gabriel: being able to draw on the slides in Frederic's demo (over the figures, charts) looked very cool to me

## Attendees 

|   Name   |           Institution     | GitHub Handle                     |
|----------|---------------------------|-----------------------------------
|loic tetrel | SIMEXP (UDEM)           | @ltetrel  
|jeremy ravenel | Naas          | @jupyter-naas
| Frederic Collonval | QuantStack | @fcollonval
| Afshin T. Darian | Two Sigma | @afshin | 
| Zach Sailer         |  Apple          | @Zsailer 
| Sarah Gibson | 2i2c | @sgibson91 |
| Martha Cryan | IBM | @marthacryan |
| Karla Spuldaro | IBM | @karlaspuldaro |
| Jessica Xu | | @jess-x |
| Nick Bollweg | Georgia Tech | @bollwyvl @nrbgt | 
|   Wayne Decatur |  Upstate Medical Univ. | @fomightez 
|Dane Freeman | Georgia Tech | @dfreeman06
|Gabriel Fouasnon|Quansight Labs|@gabalafou
| Rollin Thomas | NERSC | @rcthomas |
| Loic Huder| ESRF | @loichuder |
|Isabela Presedo-Floyd | Quansight Labs | @isabela-pf |

Plus 6 more