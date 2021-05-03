# April 27, 2021

**Date:** April 27, 2021, at 8am Pacific (your [timezone](https://arewemeetingyet.com/Los%20Angeles/2021-04-27/8:00/Jupyter%20Community%20Call))

[**Discourse:**](https://discourse.jupyter.org/t/jupyter-community-calls/668)

[**Youtube Link**](https://youtu.be/k-oaQG459A0)

**Please note:**
- Community calls are recorded and posted to this [playlist](https://www.youtube.com/playlist?list=PLUrHeD2K9Cmkoamm4NjLmvXC4Y6E1o8SP)
- These notes will be recorded and posted [here](https://jupyter.readthedocs.io/en/latest/community/community-call-notes/index.html)
- Everyone present is held to the [Jupyter Code of Conduct](https://jupyter.org/conduct)

## Purpose

Think of it as a monthly, virtual JupyterCon. It’s a place to announce and share fun things happening in the Jupyter community.

For more discussion on the format of these calls, see the thread [here](https://discourse.jupyter.org/t/reviving-the-all-jupyter-team-meetings/423).

## Short reports, celebrations, shout-outs

- **Loïc Huder** New release of [jupyterlab-h5web](https://github.com/silx-kit/jupyterlab-h5web) that brings HDF5 file exploration and visualization to the notebook.

-  **Isabela Presedo-Floyd** As always, if anyone is interested in hosting, co-hosting, or getting involved with planning a community call, please reach out to me.

## Agenda Items

- **Jeremy**:
    - [JupyterLite](https://github.com/jtpio/jupyterlite), a JupyterLab distribution that runs entirely in the browser
    - Many thanks to Nick!
    - Try it online: https://jupyterlite.readthedocs.io/en/latest/_static/lab/index.html

- **Gonzalo** Internationalization workflow for extension developers

    - Some feedback... :man-facepalming: 
        - ![Text asking why there is a delay for publishing the language packs needed for internationalization](https://i.imgur.com/mho6Ka9.png)

    - Releasing language packages :world_map::card_file_box: 
        - [Current packages and state](https://crowdin.com/project/jupyterlab)  (showing first 10)
          ![The top 10 translations by percent completed are Spanish at 100%, Chinese Simplified at 100%, Hebrew at 88%, Turkish at 86%, Brazilian Portuguese at 83%, Ukranian at 83%, Japanese at 83% French at 83%, Russian at 74%, and Polish at 60%](https://i.imgur.com/vNeRe8s.png)
        - Releasing Spanish and Chinese simplified today evening. :eyes:
        - Please attend the JLab dev meeting for more information on the internal process for managing the translations and language packs.

    - Resources :books: 
        1. [Example PR to internationalize your extension](https://github.com/jupyterlab/jupyterlab-git/pull/888) adding internationalization to [Jupyterlab-Git](https://github.com/jupyterlab/jupyterlab-git) extension.
        1. [Yaml File to update on the language packs centralized repo](https://github.com/jupyterlab/language-packs/blob/master/repository-map.yml) to update on the language packs repository.
        1. [Language packs repository](https://github.com/jupyterlab/language-packs).
        1. [Start translating on Crowdin](https://crowdin.com/project/jupyterlab)
        1. [JupyterCON slides](https://cfp.jupytercon.com/2020/schedule/presentation/239/bienvenido-bienvenue-welcome-jupyterlab-and-language-extensions/) - [[Video]](https://www.youtube.com/watch?v=8-3eo1y5IrA)

- **David**:
    - **Nbterm**
        - [Blog: Jupyter Notebooks in the terminal](https://blog.jupyter.org/nbterm-jupyter-notebooks-in-the-terminal-6a2b55d08b70)
        - [Github Repository](https://github.com/davidbrochart/nbterm)
          ![Notebook cell input and outputs represented in the terminal](https://i.imgur.com/kzNyCno.png)

## Other Links Shared

This is a space to store links shared during community call discussions related to or separate from the agenda items.

- https://github.com/jupyterlab/jupyterlab-hdf5
- https://github.com/jtpio/jupyterlite/issues/41
- https://deathbeds.github.io/jyve/lab/
- https://github.com/capytale/capytale

## Attendees

| Name | Institution | GitHub Handle |
|------|-------------|---------------|
|A. T. Darian| Two Sigma | @afshin | 
|Layne Sadler|AIQC |@aiqc|
|Sylvain Corlay   | QuantStack | @SylvainCorlay |
|Loïc Huder|ESRF|@loichuder| 
|Claudia Regio          |@Microsoft            |@claudiaregio 
|Joyce Er          |@Microsoft            |@joyceerhl| 
| Jeremy Tuloup | @QuantStack | @jtpio |
| Steven Silvester | @Apple | @blink1073 |
| Zach Sailer | @Apple | @Zsailer |
| Gonzalo Peña-C. | @Quansight | @goanpeca |
| Damián Avila | MADS & 2i2c | @damianavila |
| Pete Blois   | Google      | @blois       |
| Marvin Kastner | Hamburg University of Technology | @1kastner |
| David Brochart | QuantStack | @davidbrochart |
| Tony Fast | Quansight | @tonyfast |
| Isabela Presedo-Floyd | Quansight Labs | @isabela-pf |