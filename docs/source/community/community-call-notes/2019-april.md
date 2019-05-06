# All-Jupyter Community Video Call - April 2019

**Date:** 30 April 2019 at 9am PST (your [timezome](http://arewemeetingyet.com/Los%20Angeles/2019-04-30/09:00/Jupyter%20Community%20Call))

**Video-conference link:** https://calpoly.zoom.us/my/jupyter


## Welcome to the Team Meeting

Hello!

If you are joining the team video meeting, sign in below so we know who was here. Roll call:

| Name              | Institution             | Github Handle     | 
| ----------------- | ----------------------- | ------------------|
| Zach              | Jupyter Cal Poly        | @Zsailer          |
| Pete              | Thorn                   | @parente          |
| James Slack       | University of Edinburgh | @jamesaslack      |
| Anton Akhmerov    | TU Delft                | @akhmerov         |
| Peter Rose        | UC San Diego            | @pwrose           |
| A. T. Darian      | Two Sigma               | @afshin           |
| Ward Harold       | Google                  | @wkharold         |
| Damián Avila      |                         | @damianavila      |
| Chico Venancio    | [BMC Group K.K.](http://www.bmc-group.co.jp/en/home/) | @chicocvenancio |
| Eric Lesch        | [BMC Group K.K.](http://www.bmc-group.co.jp/en/home/) | @EricLesch |
| James Munroe | Memorial University of Newfoundland | @jmunroe |
| Lindsey Heagy     | UC Berkeley             | @lheagy           |
| Daniel Smith      | The Molecular Sciences Software Institute | @dgasmith |
| Michael Milligan  | U. Minnesota/MSI        | @mbmilligan       |
| Kevin Bates      | IBM                     | @kevin-bates|
|Cindy Wu      | experiment.com                     | @cindywu|
| Joe Hamman  | NCAR        | @jhamman       |
| Nick Bollweg     | GTRI                    | @bollwyvl          |
| Tom Baldwin      | Cascade Data Labs           | @baldwint          |
| Pete Blois       | Google Colab             | @blois |
| Ana Ruvalcaba | Cal Poly, San Luis Obispo/Jupyter |@ruv7|
| Tim Head | Project Binder | Zurich | @betatim |
| Matthias Bussonnier | Jupyter Project | @carreau|
| Tim George | Cal Poly, San Luis Obispo/Jupyter |@tgeorgeux|



## Purpose

The purpose of these monthly video conference calls is to share and demonstrate the awesome things happening in Jupyter community. We invite **anyone** to present their work, engage in discussion, or just sit in and listen. Whether you have a new [lab extension](https://github.com/jupyterlab) you've created, a new [jupyterhub deployment](https://github.com/jupyterhub) you're excited about, or an [nteract papermill](https://github.com/nteract) pipeline powering your business, we'd love to hear about it! And, we'll  record and publish these calls on YouTube for anyone unable to attend.

For more discussion on the format of these calls, see the thread [here](https://discourse.jupyter.org/t/reviving-the-all-jupyter-team-meetings/423).

## Short reports, celebrations, shout-outs

This is a place to make *short* announcements (without a need for discussion). This is also a great place to give shout-outs to contributors! We’ll read through these at the beginning of the meeting.

* [x] Shout-out to @GrahamDumpleton for continued well-researched improvements to security (e.g., https://github.com/jupyter/docker-stacks/pull/845) [name=Peter Parente]
* [x] Some initial work on enabling Jupyter documentation translation is happening in https://github.com/jupyter/docker-stacks/issues/827. If you would like to contribute a translation, review one in progress, or help document the process itself, please reach out in the issue. Thanks to  @michiboo (Micky), @Nico769 (Nicola), and @Allanfs (Allan) for starting translations!  [name=Peter Parente]
* [x] [Work](https://discourse.jupyter.org/t/aws-integration-work/864) is being done to use BinderHub fully in AWS (hosted docker registry, ECR, and hosted git repository, CodeCommit are the current areas). [name=Chico Venancio]
* [x] JupyterLab 1.0.0a3 has been released since our last call. There are a ton of updates. One thing I specifically want to give a shout out to is the document search feature that Andrew Schlaepfer built which allows building custom search functionality for different document types. Install the new version to take it for a spin: `pip install --pre jupyterlab` [name=Darian]
* [x] RISE 5.5.0 was released, more info about the release in this blogpost: http://damianavila.github.io/blog/posts/rise-550-is-out.html [name=Damián]
* [x] A big shout-out to Paul Ivanov for helping organize a "Jupyter Open Studio Day" at Bloomberg in SF. Lots of great people came, shared ideas, learned, and generally celebrated open source stuff! [name=Chris H (but I won't be able to attend the meeting)]
* [x] (a few quick shout-outs from Chris) Papermill 1.0 is released! Congrats to the nteract community for releasing papermill 1.0, a tool for parametizing / pipelining notebooks. [See the Discourse for some more links](https://discourse.jupyter.org/t/release-of-papermill-1-0/875). [name=Chris H (but I won't be able to attend the meeting)]
* [x] Many thanks to @KirstieJane and @betatim for improving the contributing documentation in repo2docker ([link to one PR on this](https://github.com/jupyter/repo2docker/pull/655)) [name=Chris H (but I won't be able to attend the meeting)]
* [x] IPython 7.5 out ! (mostly bugfixes) [name=Matthias, at airport so will stay muted] (Shout out to Matthias for this too!)
* [x] Matthias,Paul,Carol... are at PyCon for a tutorial (Thursday), and have Jupyter stickers ! [name=Matthias, at airport so will stay muted]
* [ ] add item here [name=add your name]

## Agenda Items

Add your potential agenda item here **24 hours before** the meeting at the latest. We will reorganize the agenda so that it fits in the 60m meeting slot.

* [x] Updates from the nteract project [name=Safia Abdalla]
    - New release of the cross-platform nteract desktop app is out.
    - papermill v1.0 is released.
* [x] Jupyter at the University of Edinburgh, a walkthrough of the Noteable service [name=James Slack]
    * Overview of what's happening at University of Edinburgh
        * Large support teams.
        * Very open mindset.
    * http://open.ed.ac.uk/
    * How Jupyter came to the University
        * Small scale adoption to start
        * Students were installing Jupyter on university computers. 
        * Make Jupyter a shared central service.
        * JupyterHub service university wide for use in education.
    * Pilot phase of [Noteable](https://noteable.edina.ac.uk/).
    * 6 courses with 6 different schools (~600 students).
        * Political science, art, computer science...
    * Integrated with nbgrader.
    * [Jupyter Commnity Hackathon on NBGrader in Edinburgh](https://thinking.is.ed.ac.uk/noteable/2018/12/07/jupyter-community-workshop-proposal-nbgrader-and-jupyter-in-teaching/).
    * Questions and comments:
        * Connections or interactions with Canadian group? https://syzygy.ca [name=Lindsey Heagy]
        * Is this running in the cloud or university server? [name=Anton Akhmerov]
            * University server
        * Have you explored Binderhub? [name=Chico Vernancio]
            * BinderHub now can run with "auth" and persistent storage, see https://github.com/jupyterhub/binderhub/issues/794 for more details and a live demo (ask @betatim if you have more questions)
* [ ] Introducing the rewrite of [jupyter-sphinx](https://github.com/jupyter-widgets/jupyter-sphinx/) (example [here](https://adaptive.readthedocs.io/en/latest/tutorial/tutorial.Learner2D.html)) and a discussion about markup format in the notebooks (https://github.com/jupyter/nbformat/issues/80) [name=Anton Akhmerov]
    * Publishing documents with complex content and computed output.

- Questions/Comments:
        - [name=matthias (can't speak)]: I'd love to merge that with ipython built-in sphinx-ext, /(deprecate sphinx-ext potentially as it's not well maintained ([sphix-ext docs](https://ipython.readthedocs.io/en/stable/sphinxext.html))
    
* [ ] Quantum Chemistry Database exploration with Jupyter through the [QCArchive project](https://qcarchive.molssi.org), [name=Daniel Smith].
    * The Molecular Sciences Software Institute
        * NSF funded. 
        * Designed to serve and enhance software development efforts of broad field of computational molecular science.
        * 8 universities represented on Board of Directors
        * Github org: https://github.com/MolSSI
        * https://molssi.org
    * [QCFractal](https://github.com/MolSSI/QCFractal)
    * Join our [Slack](https://join.slack.com/t/qcdb/shared_invite/enQtNDIzNTQ2OTExODk0LWM3OTgxN2ExYTlkMTlkZjA0OTExZDlmNGRlY2M4NWJlNDlkZGQyYWUxOTJmMzc3M2VlYzZjMjgxMDRkYzFmOTE) to get involved.
    * Questions/comments:
        * Is this user created content or hostesd content?
            * Completely user created.
        * 
* [ ] May 13 & 14 [W4A Hackathon on Accessibility of JupyterLab](https://groups.google.com/forum/#!topic/jupyter/trUVgNj0deU)
* [ ] Add your item here [name=and your name]

## University of Edinburgh materials and contact:
Contact  james.slack@ed.ac.uk
Noteable - https://noteable.edina.ac.uk/
Blog https://thinking.is.ed.ac.uk/noteable/
nbgrader Hackathon - http://edin.ac/2SGmzNu
Presentation - https://edin.ac/2PBJc1T
