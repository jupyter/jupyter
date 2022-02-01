# Building automatically on ReadTheDocs

This explains how to automatically rebuild documentation on ReadtheDocs
every time a pull request is merged into its corresponding GitHub repo.

## Using the ReadTheDocs service

Webhooks and services can be enabled in GitHub repo settings to allow third
party services such as ReadTheDocs. The ReadTheDocs service rebuilds the
project documentation whenever a pull request is merged into the GitHub repo.

### Navigate to Settings

Each GitHub repo has a Settings tab at the far right of the repo menubar. Navigate to Settings and then the **Webhooks & services** submenu tab.

![The ipywidgets GitHub repository's "Settings" tab has been opened, with the "Add service" submenu expanded. The "ReadTheDocs" menu item is highlighted to indicate where on the page this setting can be found.](static/gh-webhooks-services.png)

### Add the ReadTheDocs service

Select **Add service** and enter *ReadTheDocs* in the **Available Services** input box.

The Services/Add ReadTheDocs window will open. Press the green **Add service** button to activate the ReadTheDocs service.

![In GitHub, the "Settings" tab of the ipywidgets repository shows that the "ReadTheDocs" service was successfully added to the project. A checkbox with the label "Active" indicates that the service is currently running.](static/gh-add-rtd.png)

### Success

The ReadTheDocs service is added successfully. The service will take effect on the next merged pull request to the project repo.

![In GitHub, the ipywidgets repository page is open. A banner notification at the top of the page is displayed, reading "Okay, that hook was successfully created."](static/gh-rtd-hook-success.png)


*Created: 01-07-2016*
