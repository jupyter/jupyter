# Supporting document translations

**Work in progress**: Rough notes to be replaced with a first draft
(https://github.com/jupyter/jupyter/issues/511#issuecomment-644221822)

We support and encourage the translation of Jupyter documentation to other languages as one way of
making our community more inclusive and diverse. We are working toward having a consistent model for
translation of [Sphinx](https://www.sphinx-doc.org/) documentation across Jupyter projects based on
prior work in the [Python](https://python.org) and [Django](https://www.djangoproject.com/)
communities. This documentation (https://jupyter.readthedocs.io) and the
[Jupyter Docker Stacks documentation](https://jupyter-docker-stacks.readthedocs.io/) are early
adopters, meant to prove out the workflows described on this page.

## Overview

After initial project setup, changes to Sphinx documentation and its translations follow a
continuous integration (CI) and continuous deployment (CD), much like project source code. This flow
has a handful of actors:

- A person who makes changes to the English project documentation
- A person who translates snippets of text in the English documentations into another language
  (locale)
- A continuous integration system like TravisCI, CircleCI, GitHub Actions
- [ReadTheDocs](https:/readthedocs.org), our preferred service for building and hosting
  documentation
- [Transifex](https://transifex.com), a localization platform with free plans for open source
  projects, a friendly web interface, and support for the defacto
  [portable object (`.po`)](https://en.wikipedia.org/wiki/Gettext) translation format

TODO: diagram

1. A user creates or edits restructuredText (`.rst`) or Markdown (`.md`) documents written in U.S.
   English.
2. The user submits a pull request on GitHub.
3. A project maintainer reviews and merges the pull request.
4. ReadTheDocs converts the U.S. English source documents into HTML (e.g.,
   https://jupyter.readthedocs.io/en/latest/architecture/how_jupyter_ipython_work.html)
5. ReadTheDocs substitutes string translations for the English originals for all other configured
   locales and converts those documents into HTML also (e.g.,
   https://jupyter.readthedocs.io/pt_BR/latest/architecture/how_jupyter_ipython_work.html)
6. Meanwhile, the CI service runs a Sphinx command to extract translatable text from U.S. English
   documents into `en_US` portable object (`.po`) files.
7. The CI service commits the `.po` files to the project on GitHub. (e.g.,
   https://github.com/jupyter/jupyter/commit/1330bc409842d8b8a7bbb3a1c63259c34a543be0)
8. Transifex makes new strings found in the `.po` files available for translation in all configured
   languages.
9. Over time, translation teams use the Transifex web application to create, review, and update
   translations for extracted strings (e.g.,
   https://docs.transifex.com/translation/translating-with-the-web-editor)
10. Transifex submits a pull request to the GitHub project containing a `.po` file when all of its
    strings have been translated, and optionally reviewed, for a given locale (e.g.,
    https://github.com/jupyter/jupyter/pull/485)
11. A project maintainer reviews and merges the pull request.
12. ReadTheDocs once again builds HTML documentation for the the U.S. English source and other
    configured locales, including the latest translations.

Note: We recognize this flow assumes documentation starts life written in U.S. English. We should
look into removing this assumption in the future if it becomes a significant barrier to new
contributions.

## Translator workflows

(Copied almost directly from
https://jupyter-docker-stacks.readthedocs.io/en/latest/contributing/translations.html to start)

We are delighted when members of the Jupyter community want to help translate documentation. We use
[Transifex](https://transifex.com) to on-board translators in a friendly web interface without
requiring knowledge of git, GitHub, Sphinx, or other software developer tools.

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
