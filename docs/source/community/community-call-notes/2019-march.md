# All-Jupyter Community Video Call - March 2019

**Date:** 26 March 2019 at 9am PST (your [timezome](http://arewemeetingyet.com/Los%20Angeles/2019-03-26/09:00/Jupyter%20Team%20Meeting))

**Video-conference link:** https://calpoly.zoom.us/my/jupyter

[Link to prior meeting's virtual meeting report](https://paper.dropbox.com/doc/February-26-2019-Jupyter-Community-Meetings--AYQW8rw8lRF~M7gNT9WrtW4iAg-6pRznjq5hGOPcJARLFtld)

## Welcome to the Team Meeting

Hello!

If you are joining the team video meeting, sign in below so we know who was here. Roll call:

Name              | Institution             | Github Handle

* Zach              | Jupyter Cal Poly        | @Zsailer          
* Kyle              | Netflix                 | @rgbkrk           
* Pete              | Valassis Digital        | @parente          
* Carol             | Project Jupyter         | @willingc (will miss due to OpenEdX conference)        
* Brian             | AWS                     | @ellisonbg        
* Darian            | Two Sigma               | @afshin           
* Ward              | Google                  | @wkharold         
* Tim               | Project Jupyter         | @betatim          
* Chris             | Berkeley/Project Jupyter| @choldgraf        
* Pete              | Google Colab            | @blois            
* Matthias          | UC Merced               | @carreau          
* Saul              | Quansight               | @saulshanabrook   
* Vidar             | Simula Research         | @vidartf          
* Lindsey Heagy     | UC Berkeley             | @lheagy           
* Safia ABdalla     | Microsoft/nteract       | @captainsafia     
* Leticia Portella  | -                       | @leportella
* Damián Avila      | Project Jupyter                        | @damianavila      
* Craig Citro       | Google Colab            | @craigcitro       
* Nick Bollweg      | GTRI                    | @bollwyvl         
* Michael Milligan  | U Minnesota / MSI       | @mbmilligan       
* Liang Bin Hsueh   | InfuseAI                | @hlb              
* Thomas Vander Velde | -             | @tomasdelcampo            
* Luciano Resende   | IBM                     | @lresende         
* Tony Fast         |  Quansight              | @tonyfast         
* James Slack       | University of Edinburgh | @jamesaslack      
* Erik Sundell      | Sandvik                 | @consideratio     

## Purpose

The purpose of these monthly video conference calls is to share and demonstrate the awesome things happening in Jupyter community. We invite **anyone** to present their work, engage in discussion, or just sit in and listen. Whether you have a new [lab extension](https://github.com/jupyterlab) you've created, a new [jupyterhub deployment](https://github.com/jupyterhub) you're excited about, or an [nteract papermill](https://github.com/nteract) pipeline powering your business, we'd love to hear about it! And, we'll  record and publish these calls on YouTube for anyone unable to attend.

For more discussion on the format of these calls, see the thread [here](https://discourse.jupyter.org/t/reviving-the-all-jupyter-team-meetings/423).

## Short reports, celebrations, shout-outs

This is a place to make *short* announcements (without a need for discussion). This is also a great place to give shout-outs to contributors! We’ll read through these at the beginning of the meeting.

* [x] Shout out to Damian Avila for the second community docker stack: [umsimads/education-notebook](https://github.com/umsi-mads/education-notebook) [Peter Parente, jupyter/docker-stacks]
* [x] Thank you Tony Hirst for your weekly newsletter [*Tracking Jupyter*](https://tinyletter.com/TrackingJupyter) [Carol Willing, JupyterHub]
* [x] Thank you to Professor Lorena Barba at GWU for hosting the recent Jupyter team meeting [Carol Willing, JupyterHub]
* [x] Kudos, Zach Sailer et al, for kicking off the revitalization of this meeting over on the [Jupyter Discourse](https://discourse.jupyter.org/t/reviving-the-all-jupyter-community-meetings/423/11) site [Peter Parente (and everyone in attendance I suspect)]
* [x] Leave your feedback about our new all-Jupyter community call [here](https://discourse.jupyter.org/t/reviving-the-all-jupyter-community-meetings/423)
* [x] Come join us on the [Jupyter Discourse Forum](https://discourse.jupyter.org)! (in case you aren't already tired of me telling you this :-) )
    * https://discourse.jupyter.org/t/introduce-yourself/17
    * Turn off add blocker if you want to login with google or github. 

## Agenda Items

* Let’s collect all potential agenda items here before the start of the meeting (closing time **24h before**). We will then attempt to create a coherent agenda that fits in the 60m meeting slot. If there are similar items try and group them already.

* [x] Suggested demo: docker-stacks project now posts image build manifests back to the GitHub project wiki for inspection [Peter Parente, https://github.com/jupyter/docker-stacks/wiki, 5 minutes]
* [x] Introduction to mybinder.org, how to make a repository ready  for running on mybinder.org [Tim Head, 10minutes]
    * https://mybinder.org/
    * https://github.com/betatim/my-first-binder
    * Lots of example repositories: https://github.com/binder-examples/
    * Not just notebooks: https://github.com/betatim/vscode-binder
    * Documentation on how to specify dependencies and such https://repo2docker.readthedocs.io/en/latest/
    * Questions, comments and support: https://discourse.jupyter.org/c/questions
    * Write questions you have here:
        * ...
        * Is it true that you personally are the only user of https://github.com/Carreau/open-with-binder ?
        * If running an event/tutorial type thing with Binder, how many users should we feel comfortable sending to MyBinder vs setting up our own Z2JH infrastructure?
            * By default it prevents more than 100 concurent launches of the same repo. You can ask for more if you are nice. 
            * fun fact: apparently the reason this launch was slow is because somebody is teaching a "learn java" course on Binder just now and a bunch of people connected all at once https://github.com/santanche/java2learn
        * Show the log dashboard :P
            * sure thing: https://grafana.mybinder.org/d/fZWsQmnmz/pod-activity?refresh=1m&panelId=1&fullscreen&orgId=1
        * We'd love to figure out a funding model for binder


* [x] [10minutes ] Update from the nteract team [Safia].
    * Version 1.0 of papermill, notebook execution and parameterization library, will be released in early April. (https://github.com/nteract/papermill)
    * Scrapbook, tool for extracting and assembling generated outputs and data from notebooks, known as scraps, will allow you to host scraps remotely on various cloud providers. (https://github.com/nteract/scrapbook)
    * Plan laid out for version 1.0 of the kernel-relay, a GraphQL API for interfacing with Jupyter kernels. (https://github.com/nteract/kernel-relay)
    * Effort to modularize the Data Explorer, an automatic visualization library, is underway.
    * nteract is participating in Google Summer of Code (https://summerofcode.withgoogle.com/organizations/5447807656263680/)
    * Questions: 
        * How to learn more: 
            * Nteract slack https://slack.nteract.io/
            * Weekly meeting on Monday Afternoon
        * Where is the Data Explorer repo?
* [x] deathbeds stuff [Nick, github.com/deathbeds, 5min].
    * [lintotype](https://github.com/deathbeds/lintotype): interactive linting & formatting
    * [wxyz](https://github.com/deathbeds/wxyz): some crazy widgets
    * Questions:
        * The SVG messed with my eyes. <3
        * Can you expand upon the "cell-id" things?
            * [cell id in lintotype](https://github.com/deathbeds/lintotype/blob/4b83f784b56ef12a245c0ca92d48eb95a9b0f7da/packages/ipylintotype/src/ipylintotype/formatter.py#L116)
            * [cell id in irobotframework](https://github.com/gtri/irobotframework/blob/865311e0f89e2418e253f60cd7ae50990d4d6e6a/src/irobotframework/kernel.py#L90)
        * Are those suposed to be extension ? Built-in ?...?
            * ready to be packaged (not yet). Some of the stuff could go into ipywidgets
* [x] IPython releases [Matthias, IPython, https://github.com/ipython/ipython, 2min.]
    * Trying to do monthly release close to End Of Month. 
    * 7.4 has been released ! Thanks to everyone. 
    * If you want to help with 7.5 subscribe to the following issue.
        * https://github.com/ipython/ipython/issues/11657
* [x] Async Kernels startup : [Matthias, Jupyter Client , https://github.com/jupyter/jupyter_client/pull/428, 4min.]
    * https://github.com/jupyter/jupyter_client/pull/428 
* add item here [name, project name/url, estimated time for discussion].

Don't get limitted to technical discusions !