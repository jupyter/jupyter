# Jupyter Community Call 04/26

**Date:** April 26, 2022, at 7am Pacific (in your [timezone](https://arewemeetingyet.com/Los%20Angeles/2022-04-26/7:00/Jupyter%20Community%20Call))

[**Discourse**](https://discourse.jupyter.org/t/jupyter-community-calls/668)

[**YouTube recording**](https://youtu.be/WDkudE2RvRk)

**Please note:**
- Community calls are recorded and posted to this [playlist](https://www.youtube.com/playlist?list=PLUrHeD2K9Cmkoamm4NjLmvXC4Y6E1o8SP)
- These notes will be recorded and posted [here](https://jupyter.readthedocs.io/en/latest/community/community-call-notes/index.html)
- Everyone present is held to the [Jupyter Code of Conduct](https://jupyter.org/conduct)

## Purpose

Think of it as a monthly, virtual JupyterCon. It’s a place to announce and share fun things happening in the Jupyter community.

For more discussion on the format of these calls, see the thread [here](https://discourse.jupyter.org/t/reviving-the-all-jupyter-team-meetings/423).

## Short reports, celebrations, shout-outs

This is a place to make short announcements (without a need for discussion). 

* **Sarah** Shout out to everyone who is here for handling time zones!

## Agenda Items

* **[JupyterLab-LaTeX UX improvements PR](https://github.com/jupyterlab/jupyterlab-latex/pull/192)** Result of 2 semesters of work by [Junior Design Capstone class](https://techstyle.lmc.gatech.edu/cs-tech-comm-junior-design-sequence/) team from Georgia Tech done for client (Axle Informatics/NIH). Project included a user reasearch section which is summarized in PR. New features highlights:
    * Preview button
    * Formatting buttons (bold, italic, underlined, subscript, superscript)
    * Autocomplete for common LaTeX tags (i.e. `\subsection`)
    * tikzplots templates
    * Table creation helper
    * Suggestion: UX to help with LaTeX install discovery, errors (even as documentation)

* **JupyterLab-Git usability improvements** 4 features added to [JupyterLab-Git](https://github.com/jupyterlab/jupyterlab-git) as a result of the [12-week Spring 2022 MLH Fellowship Open-Source Program](https://fellowship.mlh.io/programs/open-source). The majority of the work was done by [Dat Quach](https://github.com/quachtridat) and [Zeshan Fayyaz](https://github.com/ZeshanFayyaz) with help and feedback from [Frédéric Collonval](https://github.com/fcollonval).
    * [Credential cache](https://github.com/jupyterlab/jupyterlab-git/pull/1099): save Git login credentials temporarily
    * [Commit diff](https://github.com/jupyterlab/jupyterlab-git/pull/1108): compare two arbitrary commits in the *History* panel
    * [Reset to remote](https://github.com/jupyterlab/jupyterlab-git/pull/1087): force reset a branch to match its remote tracking branch
    * [A warning for unsaved staged files](https://github.com/jupyterlab/jupyterlab-git/pull/1075): warn the user when there are unsaved changes on files that are in the staged area

* **Frederic**
    * _Search and Replace across files_ extension (release in the coming week)
    * [GitHub repository](https://github.com/jupyterlab-contrib/search-replace)
    * Demo
        * The extension is using a CLI tool called [Ripgrep](https://github.com/BurntSushi/ripgrep)
        * This limits the usage of the extension to contents served from a file system.
    * Potential solutions for building index for other needs (like non OS filesystem) (thanks to Nick):
        * https://whoosh.readthedocs.io/en/latest/intro.html
        * https://pypi.org/project/lunr/
    
* **Gayle** - Jupyter Community Events Manager
    * 4th Round of CFP for Jupyter Community Workshop
    * Starting interviews for highlighted contributor write up in blog. If interested schedule time on calendar: https://calendly.com/gayle-numfocus/30min?month=2022-04
    
* **Steve**
    * New [cookiecutter](https://github.com/jupyter-server/extension-cookiecutter) template for creating Jupyter Server Extensions
    * We created it during the weekly Jupyter Server [contributing hour](https://github.com/jupyter-server/team-compass/issues/22)

* **Jason W**
    * Shout out for triage meetings! (Can be found on the [Jupyter Community Calendar](https://docs.jupyter.org/en/latest/community/content-community.html#jupyter-community-meetings))
    * Typically at 10:00 PDT, though not this week
    * You can triage on your own: [JupyterLab issues needing triage](https://github.com/jupyterlab/jupyterlab/labels/status%3ANeeds%20Triage)

## Other Links Shared

This is a space to store links shared during community call discussions related to or separate from the agenda items.

- [lyx]https://www.lyx.org/
- https://github.com/BurntSushi/ripgrep
- https://whoosh.readthedocs.io/en/latest/intro.html
- https://pypi.org/project/lunr/

## Attendees 

|   Name     |           Institution     | GitHub Handle|
|------------|---------------------------|--------------|
| Konstantin |Axle Informatics/NIH       | @ktaletsk |
| Dat Quach  | Major League Hacking (MLH) | @quachtridat |
| Jason Weill | AWS | @jweill-aws |
| Sarah Gibson | 2i2c     | @sgibson91 |
| A. T. Darian | QuantStack | @afshin | 
| Gayle Ollington|NumFOCUS|@gollington         |            | 
| Frederic Collonval | QuantStack | @fcollonval
| Alex Bozarth | IBM | @ajbozarth |
| Steven Silvester | MongoDB | @blink1073 |
| Chris Sewell           |      EPFL       | @chrisjsewell
| Wayne Decatur | Upstate Medical Univ. | @fomightez 
| Isabela Presedo-Floyd | Quansight Labs | @isabela-pf |

Plus 1 more.