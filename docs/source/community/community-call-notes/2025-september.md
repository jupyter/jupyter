---
tags: jupyter
---
# September 2025: Jupyter Community Call

**Date:** September 04, 2025, at 8am PDT / 15:00 UTC; your timezone ([your timezone](https://arewemeetingyet.com/Los%20Angeles/2025-09-04/08:00/Jupyter%20Community%20Call))

**Video-conference link:** [Zoom link](https://zoom.us/j/95228013874?pwd=Ep7HIk8t9JP6VToxt1Wj4P7K5PshC0.1)

**Feedback or questions?** You can either post publicly on the following thread on 
[Discourse](https://discourse.jupyter.org/t/jupyter-community-calls/668/101?u=ruv7) or email the DEI Committee - jupyter-dei@googlegroups.com

**Please note:**
- Community calls are recorded and posted to this [playlist](https://www.youtube.com/playlist?list=PLUrHeD2K9Cmkoamm4NjLmvXC4Y6E1o8SP)
- These notes will be recorded and posted [here](https://jupyter.readthedocs.io/en/latest/community/community-call-notes/index.html)
- Everyone present is held to the [Jupyter Code of Conduct](https://jupyter.org/confduct)

**Welcome!**

If you are joining the Jupyter Community Call, we ask that you sign in below at the start of the call so that we know who was here.

| Name | Institution | GitHub Handle |
| ---- | ----------- | ------------- |
|Min |UC Berkeley, BIDS | @minrk |
|Rosio Reyes | Anaconda | @RRosio |
|David Brochart | QuantStack | @davidbrochart |
| Alonso Silva | Nokia Bell Labs | @alonsosilvaallende |
| Paul Hoger | Karlsruhe Institute of Technology | @Paul2708 |
|Johan Mabille |QuantStack|@JohanMabille|
|Matt Fisher | Schmidt DSE | @mfisher87 |
| Ian Thomas | QuantStack | @ianthomas23 |
| Jason Grout | Independent | @jasongrout |
| Kirstie Whitaker | Berkeley Institute for Data Science, Berkeley, CA | @KirstieJane |
|Konstantin Taletskiy |Orange Bricks|@ktaletsk|
|Simon Li|University of Dundee|@manics|
|Wayne Decatur | Upstate Medical University | @fomightez |
| Zach Sailer | Apple | @Zsailer |


### Icebreaker

| Name | First programming language used? |
|--------|-----------|
| Min | TI-BASIC (TI-83 Calculator) |
| Matt Fisher | TI-BASIC (TI-89) / HyperCard |
| Kirstie | does getting weirdly good at writing bash scripts count?? I went to a neuroimaging summer school after my first year of my PhD and friends taught me to use sed to great success!! |
| Ian | FORTRAN (Back when it was written in capitals) |
| Konstantin | Basic |
| Alonso | Java |
| Wayne | Basic on Commodore64 |
| Zach | MatLab! |
| Johan | Java (yeah I know...) |

## Purpose

Think of it as a monthly, virtual JupyterCon. It’s a place to announce and share fun things happening in the Jupyter community.

For more discussion on the format of these calls, see the thread [here](https://discourse.jupyter.org/t/jupyter-community-calls/668/107).

## Short reports, celebrations, shout-outs

This is a place to make community announcements (without a need for discussion).

* The Jupyter Book community have submitted a paper describing Jupyter Book 2 and MyST to the Scientific Python proceedings
  * It's still in PR form but ready for you to read: [Jupyter Book 2 and the MyST Document Stack](https://github.com/scipy-conference/scipy_proceedings/pull/1096)
  * This was a huge amount of work and a wonderfully inclusive effort!
  * We're particularly proud of the case studies from [The Turing Way](https://book.the-turing-way.org/), [QuantEcon](https://quantecon.org/), [Project Pythia](https://projectpythia.org/), and the [QIIME 2](https://qiime2.org/) Framework (Q2F) documentation ecosystem :rocket: :star2: 
* The Jupyter Book community also merged some updates to our documentation, including a [pronunciation guide](https://mystmd.org/guide/guiding-principles#how-do-i-pronounce-myst) for MyST!
* [GeoJupyter](https://geojupyter.org/) hosted a really successful hackathon in Berkeley in August
  * There were 4 teams that organically emerged:
    * infrastructure developers exploring containers and development environment setup,
    * documentation specialists filling in gaps and testing tutorials with fresh eyes,
    * API developers working on Python integration and data manipulation workflows, and
    * strategists zooming out to question JupyterGIS’ fundamental purpose.
  * Read the blog post to find out more! https://geojupyter.org/blog/20250903-inperson-hackathon-and-design-dialog/index.html
* JupyterGIS was used as a supporting visualisation for a Nature article!
  * https://www.linkedin.com/posts/quantstack_jupytergis-jupyterlite-jupytergis-activity-7369272041537052673-RZO3/ 
![1756971367899](https://hackmd.io/_uploads/rJdvT7w9eg.jpg)

  * A prudent planetary limit for geologic carbon storage doi: [10.1038/s41586-025-09423-y](https://doi.org/10.1038/s41586-025-09423-y)
  * Explore the interactive map: https://cdr.apps.ece.iiasa.ac.at/sedimentary-basin-level-maps
* JupyterLab 4.5.0a3 is available for testing!
    * `pip install jupyterlab==4.5.0a3`
conda install conda-forge/label/jupyterlab_alpha::jupyterlab
https://github.com/jupyterlab/jupyterlab/releases/tag/v4.5.0a3
    * `pip install notebook==7.5.0a1`
conda install conda-forge/label/notebook_alpha::notebook
https://github.com/jupyter/notebook/releases/tag/v7.5.0a1
* JupyterCon! Schedule is live! 
  * https://events.linuxfoundation.org/jupytercon/program/schedule/
  * And travel funding requests being reviewed this week! (There were 43 applications!)

## Agenda Items

Add agenda items here **before** the meeting. The event host will reorganize the agenda so that it fits in the 60m meeting slot.

* Community workshops! Please submit proposals. **Due September 7th**! This year, workshops are focused on contributors, not users.
    * https://blog.jupyter.org/jupyter-community-workshops-are-back-3cca15d02975
    * Are there workshops **you want to see happen** but **don't have the capacity to organize**?
        * Matt F: Documentation!!!
* David Brochart: Microverse, a new in-browser JupyterLab based on Jupyverse.
    * https://david-brochart.medium.com/microverse-jupyverse-in-the-browser-c24894fa5438
* (10 minutes) Konstantin Taletskiy: JupyterLab Marketplace https://labextensions.dev
    * A community catalog that surfaces GitHub/PyPI signals
    * Completely automated with BigQuery->GitHub->Supabase pipeline
    * Next steps: end-to-end experience with deep-link hook in Extension Manager
* (5 minutes) Voices of JupyterHub soft launch!
  * https://voicesofjupyterhub.orgmycology.com/intro
* (3 minutes) [Jupyter Foundation CFP](https://blog.jupyter.org/your-ideas-our-support-jupyter-community-call-for-funding-proposals-f4642590ae76), open through Sunday, Sep 28.




## Other Links Shared
* Feel free to connect on the [Jupyter Zulip chat](https://jupyter.zulipchat.com/)! Lots of people are joining (nearly 400 users now) and there are a lot of active discussions. Zulip has a [desktop app](https://zulip.com/apps/) and a [new mobile app](https://zulip.com/apps/) that is really nice.
* The Executive Council is running an experiment adding Plausible web analytics to jupyter.org. You can see the stats at https://plausible.io/jupyter.org.