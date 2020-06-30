# Supporting translations of documentation

We support and encourage the translation of Jupyter documentation to other languages as one way of
making our community more inclusive and diverse. We are working toward having a consistent model for
translation of [Sphinx](https://www.sphinx-doc.org/) documentation across Jupyter projects based on
prior work in the [Python](https://python.org) and [Django](https://www.djangoproject.com/)
communities. This project (https://jupyter.readthedocs.io) and the
[Jupyter Docker Stacks project](https://jupyter-docker-stacks.readthedocs.io/) are early adopters,
meant to prove out the workflows described on this page.

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

![Translation CI/CD](static/translation-ci-cd.png "Diagram of the translation continuous integration
and deployment flow")

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

We are delighted when members of the Jupyter community want to help translate documentation. We use
[Transifex](https://transifex.com) to on-board translators in a friendly web interface without
requiring knowledge of git, GitHub, Sphinx, or other software developer tools.

### Creating translations

[Getting Started as a Translator](https://docs.transifex.com/getting-started-1/translators>) is an
excellent on-boarding guide for new Transifex users. Follow the instructions to create an account.
When prompted to join a team, look for _jupyter-meta-documentation_ to start contributing
translations to this documentation site. Alternatively, visit
https://www.transifex.com/project-jupyter/jupyter-meta-documentation/ after creating your account
and request to join the project. A project maintainer or language team coordinator will review and
approve your request.

### Reviewing translations

Transifex supports
[Reviewing Translations](https://docs.transifex.com/translation/reviewing-strings), peer review by
members of a language team, to ensure translation quality. Project maintainers can choose whether
Transifex should immediately send a pull request when translations of all text in a document are
available or delay submitting a pull request until after all of those translations are also reviewed
(the
[current setting for this project](https://github.com/jupyter/jupyter/issues/430#issuecomment-552138547)).

### Coordinating translation teams

Project maintainers can also grant Transfex team members the role of
[language coordinator](https://docs.transifex.com/teams/understanding-user-roles#organization-administrator).
Language coordinators have permission to invite users to language teams, approve or deny join
requests, assign language team roles, and perform other administrative actions for a particular
project language. Empowering trusted members of the community as coordinators can help grow
translation teams without software developer involvement.

## Administrator workflows

The translation CI/CD workflow described above requires configuration in GitHub and in Transifex to
function. Project maintainers can follow the instructions below to enable translations for their
Sphinx documentation.

### Creating a Transifex organization

Transifex organizes translation projects under organizations that mirror organizations and
repositories on GitHub. At present, only the https://github.com/jupyter organization has a
corresponding org on Transifex (https://www.transifex.com/project-jupyter/public/) with the
following
[organization administrators](https://docs.transifex.com/teams/understanding-user-roles#organization-administrator):

- @choldgraf
- @parente
- @willingc

GitHub users with permissions to install applications in a GitHub org can follow these instructions
to create a new Transifex-GitHub organization link (e.g., for https://github.com/jupyterhub,
https://github.com/jupyterlab).

1. Create a new user account at https://transifex.com.
2. Complete the sign-up wizard.
3. Create and name a new organization.
4. Click the organization drop down in the top right of the Transifex dashboard page and select
   _Organization Settings_.
5. Click _Details_ in the left sidebar.
6. Click _inviting administrators_ in the _Management_ section to add additional admins to the
   Transifex org.
7. Click _Manage integrations_ in the left sidebar.
8. Click _Install the Transifex app_ in the GitHub section.
9. Select the GitHub organization to associate with the new Transifex organization.
10. Select the repositories that Transifex will have permission to access.
11. Return to the tab where you clicked _Install the Transifex app_ and click _authorize Transifex_
    in the GitHub section.
12. Choose the GitHub organization you just configured in the popup dialog.

Note that you can revise the GitHub-Transifex integration at any time by visiting
https://github.com/settings/installations.

### Creating a Transifex project

Transifex
[organization administrators](https://docs.transifex.com/teams/understanding-user-roles#organization-administrator)
can follow the instructions below to configure new translation projects for GitHub projects in the
GitHub org corresponding to the one on Transifex.

1. Visit https://www.transifex.com.
2. Sign in with the appropriate admin user account for the organization.
3. Click the organization drop down in the top right of the Transifex dashboard page and select
   _Organization Settings_.
4. Click _Create new project_ in the lower left sidebar.
5. Name the translation project after the project on GitHub.
6. Select _Public_ as the privacy type, indicate that the project is open source, and provide the
   GitHub URL for the repository.
7. Select a file-based project.
8. Create a new team for the project.
9. Select _English (en)_ as the source language.
10. Select known target languages. (You can add these later as well.)
11. Click _Create project_.
12. Click _Settings_ under the project name in the left sidebar.
13. Click the _Maintainers_ tab.
14. Invite additional
    [project maintainers](https://docs.transifex.com/teams/understanding-user-roles#project-maintainers),
    typically software developers who will be responsible for maintaining the continuous integration
    and bootstrapping language teams.

### Configuring languages and teams

Transifex organization admins and project managers can add translation languages to a project.

1. Visit https://www.transifex.com.
2. Sign in with the appropriate admin user account for the organization.
3. Click _Languages_ under the project name in the left sidebar.
4. Click _Edit languages_.
5. Add or remove target translation languages.
6. Click _Apply_.

Organization admins, project maintainers, and
[team managers](https://docs.transifex.com/teams/understanding-user-roles#team-managers) can add
users to translation teams with the roles of language coordinator, reviewer, or translator.

1. Click _Teams_ in the top nav bar.
2. Click the _Invite Collaborators_ button in the top right.
3. Enter the username, email address, or full name of a person to add to the project. Note that the
   autocomplete in this field does not always display a popup for the user you wish to invite.
   Confirm you've entered the correct value and move on.
4. Select [the role](https://docs.transifex.com/teams/understanding-user-roles) to assign to the
   user.
5. If the role applies to a specific team, select the team.
6. If the role applies to a specific language, select the language.
7. Click _Invite more_ to enter additional users or _Send invitation_.

### Configuring Transifex-GitHub integration

After configuring organization and project resources on Transifex, project developers can:

- configure Sphinx to produce `.po` files for the source language and read `.po` files containing
  translations
- configure Transifex to watch for source language `.po` file changes
- configure the project CI service to update source language `.po` files when contributors make
  changes to the source documentation

The instructions in this section assume a git repository already contains Sphinx documentation in
the following directory structure:

```
my-project/
  docs/
    build/              # built sphinx artifacts go here
    source/             # documentation source is in here
      conf.py           # sphinx config file
      index.rst         # root of the documentation
    requirements.txt    # sphinx, sphinx-intl, etc.
```

Project developers can do the following to configure Sphinx to seed source `.po` files and
recognization translation `.po` files.

1. Add `sphinx-intl` to your Sphinx project `requirements.txt` or `environment.yaml` if it does not
   already exist.
2. Run `sphinx-intl create-txconfig` in the `docs/` directory.
3. Add the following to the Sphinx `source/conf.py` file.

```python
# -- Translation -------------------------------------------------------------

gettext_uuid = True
locale_dirs = ["locale/"]
```

3. Run `make gettext` to extract all strings from the English source documentation.
4. Run `sphinx-intl update -l en` to generate the English source `.po` files.
5. Submit, review, and merge a pull request with the changes and generated `.po` files.

After merging the pull request, link to the Transifex project to the GitHub repository.

1. Visit https://www.transifex.com.
2. Click _Settings_ under the project name in the left sidebar.
3. Click the _Integrations_ tab.
4. Click _Link Repository_ in the GitHub section.
5. Select the appropriate GitHub repository and integration branch. Then click _Next_.
6. Copy and paste the following configuration into the dialog, adjusting the commented values as
   appropriate, and then click _Next_.

```yaml
filters:
  - filter_type: dir
    file_format: PO
    source_file_extension: po
    # Change this if you selected a different source language during project setup
    source_language: en
    # The path in the GitHub repository where the source .po files reside
    source_file_dir: "docs/source/locale/en/LC_MESSAGES"
    # The path in the GitHub repository where translation .po files reside
    translation_files_expression: "docs/source/locale/<lang>/LC_MESSAGES"
```

7. Select when Transifex will submit translations a back to the repository. Then click _Save &
   Sync_.
8. Click _Close_.
9. Watch the sync status progress.
10. Click _Resources_ in the left sidebar.
11. Click one of the `.po` files to see translation progress by language.
12. Click one of the languages to see details about translation progress, translate text, and review
    translations. See the [Translator workflows](#translator-workflows) section above for details.

After confirming the initial English `.po` files have reached Transifex, set up continuous
integration to ensure source strings are kept up-to-date in Transifex whenever the English
documentation changes. The steps to accomplish this end vary depending on the CI provider. The
following describes how what to do when using GitHub Actions.

1. Create a new GitHub actions workflow file `.github/workflows/gettext.yml` in the project.
2. Add the following content to the file:

```yaml
name: Extract Translatable Strings

# Run on all branch pushes
on:
  push:
    paths:
      - "docs/source/**"
      - "!docs/source/locale/**"
      - ".github/workflows/gettext.yml"

jobs:
  gettext:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@master
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: "3.x"
      - name: Install dependencies
        working-directory: docs
        run: pip install -r requirements.txt
      - name: Extract source strings
        working-directory: docs
        run: |
          make gettext
          sphinx-intl update -l en
      - name: Push to master
        # Only commit changes to master if master just changed
        if: github.ref == 'refs/heads/master'
        uses: mikeal/publish-to-github-action@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

3. Submit, review, and merge a pull request containing the workflow YAML.

Once you complete the steps in this section, any changes to the source English documentation merged
to master are pushed to Transifex for translation. Likewise, and translations completed on Trasifex
are submitted as pull requests back to the project on GitHub.

### Hosting translations on ReadTheDocs

TODO

- New project `<name>-<locale>`
- Set as translation of root project in Admin -> Translations

## Reference

https://github.com/parente/helloworld-transifex-rtd is a mini-project configured to support the
entire workflow described in this document.
