# Jupyter Community Call 2/28

**Date:** February 28, 2023, at 8am Pacific ([your timezone](https://arewemeetingyet.com/Los%20Angeles/2023-02-28/08:00/Jupyter%20Community%20Call))

[**Discourse:**](https://discourse.jupyter.org/t/jupyter-community-calls/668)
[**Youtube**](https://youtu.be/718KFe6MMW4)

**Please note:**
- Community calls are recorded and posted to this [playlist](https://www.youtube.com/playlist?list=PLUrHeD2K9Cmkoamm4NjLmvXC4Y6E1o8SP)
- These notes will be recorded and posted [here](https://jupyter.readthedocs.io/en/latest/community/community-call-notes/index.html)
- Everyone present is held to the [Jupyter Code of Conduct](https://jupyter.org/conduct)

## Purpose

Think of it as a monthly, virtual JupyterCon. It’s a place to announce and share fun things happening in the Jupyter community.

For more discussion on the format of these calls, see the thread [here](https://discourse.jupyter.org/t/reviving-the-all-jupyter-team-meetings/423).

## Short reports, celebrations, shout-outs

This is a place to make short announcements (without a need for discussion). 

* **Isabela** Many thanks to the Security project team for being flexible and helping community call have this time on the calendar!
    * Security calls are now 1st and 3rd Tuesday of every month
    * Community call is last Tuesday
    * No collisions anymore, can move community call to more friendly time! :)
* **Isabela** Governance update: Software Steering Council is in the process of getting office hours on the calendar and resuming all other duties.

## Agenda Items

* @rowanc1 @agoose77 - `jupyterlab-myst` overview and demo https://github.com/executablebooks/jupyterlab-myst
    * MyST: Markup language incubated in executable books project, spun out last week
        * 10% of Python documentation is written MyST and increasing
    * Moving toward Javascript world => better integration with JupyterLab
    * See myst-tools.org, new website for the project
    * MyST: Support for scientific documents and publications, export to various high-quality PDF formats
        * Also rendered static versions of Jupyter notebooks
        * What metadata and front-matter needs to be added
        * How to bring computational thinkin into publishing
    * JupyterLab MyST extension
        * Rich metadata as data at the top of document (YAML)
            * Executing the metadata cells yields a nice top block for a notebook
            * Nicer than custom HTML, parseable, better to edit and view
        * Callout blocks:
            * Bracketed directives like ":::{important}"
            * Also class information like dropdown
        * Cross-references
        * Inline execution in markdown cells
            * Syntax subject to change
            * Roles and directives e.g. "{eval}`1+1`"
            * Embed Jupyter widgets directly in markdown, figures, sparklines
            * Better weaving of documentation and code
    * Ongoing nbformat workshop and MyST
        * Discussing the challenges of developing the extension
        * In particular, embedding computation in documentation, wasn't originally envisioned
        * Input types may need to expand
    * Static publishing, see also https://thebe.readthedocs.io/en/stable/
        * Write documents with interactivity
        * Publishing mechanisms
        * Help promote interactivity and computation experience to the end sharing of documents
    * Mixing HTML and MyST and accessibility?
        * Keeping these issues in mind during development
        * Gets more difficult with widgets
        * Efforts to use the same technology pieces as Jupyter
        * => as Jupyter improves things upstream in widgets space it propagates here
        * Archivability, semantic HTML, paying attention to accessibility scores
            * https://myst-tools.org/docs/mystjs/accessibility-and-performance
* Ongoing nbformat workshop discussion @isabela-pf
    * We don't have a type of Markdown we specify in notebooks
    * This has created some difficulty during user testing
    * Would be nice to at least know what kind of Markdown specification we're following
    * There are web accessibility guidelines, not clear always how they correlate
    * Greater clarity would help because accommodations get hooked in at the HTML level
    * At the workshop @rowanc1:
        * Split into 3 groups
            * Text-based format in addition to standard format (e.g. jupytext)
            * Cell types workflow
            * Markdown formats inside cells
        * The wild west of notebook, cell metadata, how do people use it?
            * Noteable example
                * Front-end interfaces that don't go through Jupyter/JupyterLab
                * Visualization state stored in cell metadata
                * Namespaced in noteable
            * Are there changes in terms of cell metadata being considered PR/discourse wise?
                * Discourse: ???
                * Maybe [Jupyter Discourse: Notebook Metadata UX](https://discourse.jupyter.org/t/notebook-metadata-ux/17507_)
            * Simplest use case (kinda) marking cell metadata for special treatment or processing 

## Other Links Shared

This is a space to store links shared during community call discussions related to or separate from the agenda items.

## Attendees

|   Name   |           Institution     | GitHub Handle                     |
|----------|---------------------------|-----------------------------------|
| Rollin   | NERSC                     | @rcthomas                         |
| Rowan          | Curvenote / ExecutableBooks | @rowanc1 |
| Gabriela Vives         |QuantStack            |GabrielaVives |
| Wayne Decatur  | Upstate Medical Univ. | @fomightez |
| Isabela Presedo-Floyd | Quansight Labs | @isabela-pf |

Plus 1 more.
