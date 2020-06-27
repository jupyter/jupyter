# Supporting document translations

**Work in progress**: Rough notes to be replaced with a first draft
(https://github.com/jupyter/jupyter/issues/511#issuecomment-644221822)

We support and encourage the translation of Jupyter documentation to other languages as one way of
making our community more inclusive and diverse. We are working toward having a consistent model for
translation of Sphinx documentation across Jupyter projects based on prior work in the
[Python](https://python.org) and [Django](https://www.djangoproject.com/) communities. This
documentation (https://jupyter.readthedocs.io) and the
[Jupyter Docker Stacks documentation](https://jupyter-docker-stacks.readthedocs.io/) are early
adopters, meant to prove out the workflows described on this page.

## Overview

- Diagram of the translation CI/CD flow _after_ setup
- Summary: CI creates en_US po files from English documentation, transifex watches for po file
  changes and makes strings available for translators, transifex creates pull requests when a
  document is 100% translated and/or reviewed, read the docs makes translations available under
  separate paths, changes to the English source trigger po file updates from travis, process repeats
- Examples: Travis updates en_US po files
  https://github.com/jupyter/jupyter/commit/1330bc409842d8b8a7bbb3a1c63259c34a543be0, Transifex
  publishes completed translations https://github.com/jupyter/jupyter/pull/485,

## Translator workflows

(Copied almost directly from
https://jupyter-docker-stacks.readthedocs.io/en/latest/contributing/translations.html to start)

We are delighted when members of the Jupyter community want to help translate documentation to other
languages. We use [Transifex](https://transifex.com), a localization platform with free plans for
open source projects, to on-board translators in a friendly web interface without requiring
knowledge of git, GitHub, Sphinx, or other software developer tools.

### Creating translations

[Getting Started as a Translator](https://docs.transifex.com/getting-started-1/translators>) is an
excellent on-boarding guide for new Transifex users. Follow the instructions to create and account.
When prompted to join a team, look for _jupyter-meta-documentation_ to start contributing
translations to this documentation site. Alternatively, visit
https://www.transifex.com/project-jupyter/jupyter-meta-documentation/ after creating your account
and request to join the project.

### Reviewing translations

- Optional step before changes go live
- Useful when teams become large to ensure quality

### Coordinating translation teams

- Can manage translation team members
- Empower members of the community to grow translator teams

## Administrator workflows

- Responsible for configuring Transifex-GitHub to work together, CI/CD

### Creating a project on Transifex

- Jupyter org
- New project
- Make sure to mark it as open source

### Adding a new translation team to Transifex

- Create language
- Assign coordinators
- Assign translators
- Decide reviews required or not

### Configuring Transifex-GitHub integration

See https://github.com/jupyter/jupyter/pull/432

- Set up GitHub integration + filters config in Transifex UI
- Configure locale dir for Sphinx
- Create docs/.tx/config
- Create en_US templates
- PR it

See https://github.com/jupyter/jupyter/pull/440 plus follow-ons to fix bugs: #445-447

- Update en_US locale on merge to master
- PR it
- Should we also be updating the docs/.tx/config mapping for new files?

### Hosting translations on ReadTheDocs

- New project `<name>-<locale>`
- Set as translation of root project in Admin -> Translations
