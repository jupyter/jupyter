# What is Jupyter?

"Jupyter" can mean a lot of things, so let's start from the beginning (and break it down):

First and foremost, "Project Jupyter" is a large umbrella project that covers many different software offerings and tools. That includes "Jupyter Notebook" and "JupyterLab", which are both popular web-based notebook authoring and editing applications. The Jupyter project, and its subprojects, all center around providing tools (and standards) for interactive computing with computational notebooks. Each of these will be explored further below.

The term "Jupyter" is often used as a shorthand to refer to one of those products or ideas, which sometimes leads to confusion. Let's take a look at each one of those, one-by-one.

# What is a "Computational Notebook" anyway?

A famous computer programmer (Donald Knuth) popularized the idea to combine explanatory plain english text with computer code, which is commonly called "literate programming".

A program written in this way could be printed on paper and shared by hand as an actual "notebook", but in modern times, they are shared digitally as "notebook files", and can contain additional rich media like images, 3D models and interactive figures, along with data and other program outputs.

By adopting this practice, computer programs, as well as other complex information and ideas, could be better explained to a wide range of people. Because scientists, engineers, and other technical people so often need to perform and communicate sophisticated calculations to describe their work, these "computational notebooks" became a very popular way to share their work and ideas.

When someone uses the term "notebook", they might be referring to:

- A notebook file on their computer
- The idea of combining computer code, explanatory text, images and more into the "notebook format"
- The "Jupyter Notebook" application, used to author and edit digital notebook files

And the term "Jupyter" might refer to:

- "Project Jupyter", the overarching umbrella project
- The "Jupyter Notebook" or "JupyterLab" editing programs

The name Jupyter comes from the three programming languages the project originally supported: Python, Julia, and R.


### What's the structure of Jupyter?

Jupyter is developed completely in the open, by the community, but there is a
personnel structure guiding the developments and taking care of the resources.
The actual development of the software components are done in the scope of
[Jupyter (sub)projects][subprojects].

While some subprojects take care of the development of a specific software 
component, other projects will take care of broader discussions, such as the
[Accessibility][] and [Security][] projects.

> - If you are completely new to *Jupyter*, the project's [About][]
> page is a good reading.
>
> - If you want to know more about the organizational structure: 
> [Governance][] pages.
> 
> - And if you would like to contribute to the project, have a look at 
> the [Get Involved][] page.

In the following sections we are going to define the major components of the 
Jupyter ecosystem. This is *not* a complete reference of every aspect of Jupyter,
but rather a clarification document of the complexity of Jupyter content.

## Jupyter software

The graph below presents the best known software components of the Project.
There are many other components -- like Jupyter-Server, Jupyter-Kernels --
that we will talk about later, but for starter we go with the most common ones.

Connections and groups in this diagram are not formal relationships but
simple indicators to help us draw the big picture in the next sections.

```mermaid
graph TD
    IPython
        click IPython href "https://ipython.org" _blank

    subgraph source/code
        Nbformat[["Notebook file format (.ipynb)"]]
            click Nbformat href "https://nbformat.readthedocs.io" _blank

        JupyterWidgets>Jupyter-Widgets]
            click JupyterWidgets href "http://ipywidgets.readthedocs.io" _blank
    end

    subgraph frontends
        direction LR

        JupyterLab(Jupyter-Lab)
            click JupyterLab href "https://jupyterlab.readthedocs.io" _blank

        JupyterNotebook(Jupyter-Notebook)
            click JupyterNotebook href "https://jupyter-notebook.readthedocs.io" _blank
    end

    subgraph viewers
        direction LR

        Binder(Binder)
            click Binder href "https://mybinder.org" _blank

        Voila(Voilà)
            click Voila href "https://voila.readthedocs.io" _blank

        Nbviewer[nbviewer]
            click Nbviewer href "https://nbviewer.org" _blank

        Nbconvert[nbconvert]
            click Nbconvert href "https://nbconvert.readthedocs.io" _blank
    end

    JupyterHub(Jupyter-Hub)
        click JupyterHub href "https://jupyterhub.readthedocs.io" _blank

    JupyterHub --> frontends
    IPython ~~~ source/code
    frontends --> source/code
    viewers --> source/code
```


### *Notebook* vs *notebook*
[nbformat.readthedocs.io]: https://nbformat.readthedocs.io
[jupyter-notebook.readthedocs.io]: https://jupyter-notebook.readthedocs.io

Probably the most overloaded term within the community is "notebook".

Formally, "notebook" has two meanings: the **notebook file format** -- the `.ipynb` 
files -- where data/content are stored (ie, the digital document); 
And the **Jupyter-Notebook** application for editing and running notebook files.

Jupyter-Notebook -- the application -- may be referred simply as "Notebook".
As in many situations in life, discerning between the (notebook) file/document
and the (Notebook) application should be clear from the context.

In Jupyter official documentation we refer to the application as Jupyter-Notebook 
or simply Notebook with capital "N". 
The digital file/document is written as a common name (ie, lower-case) notebook.

You can find detailed information about notebook file format, `nbformat`, and
the frontend application in their respective official documentation:

- Notebook file format: [nbformat.readthedocs.io][]
- Jupyter-Notebook: [jupyter-notebook.readthedocs.io][]


### *Notebook* and *Lab*
[jupyterlab.readthedocs.io]: https://jupyterlab.readthedocs.io

There are two applications (aka, frontends) to edit and run notebooks:
Jupyter-Notebook and Jupyter-Lab. Jupyter-Lab is an evolution of Jupyter-Notebook, 
it provides a more concise and customizable user interface.

It is mostly a matter of preference which application/interface to use, 
they both provide pretty much the same functionalities on what regards editing 
and running notebook documents.
The *Lab* provides a richer graphical user interface (GUI), whereas *Notebook*
provides a simpler GUI.

Personally, I like to use Jupyter-Lab on my daily work as a data analyst, and 
Jupyter-Notebook while teaching so we can all focus on the notebook's content.

Regarding ambiguous use of terms, sometimes people will refer to Jupyter-Lab 
as "Notebook"; This is certainly the case among old practitioners, that used
the Notebook application extensively in a time prior to Jupyter-Lab.

- Jupyter-Lab: [jupyterlab.readthedocs.io][]


### What about *Hub*?
[jupyterhub.readthedocs.io]: https://jupyterhub.readthedocs.io

Jupyter-Hub is a manager of Jupyter-Lab and Jupyter-Notebook instances in
multi-user settings. 

In a Jupyter-Hub setup editing and running notebook files is
still performed by Lab and Notebook, the Hub is responsible for authenticating
users and handling them their corresponding Lab/Notebook instance connection.

Jupyter-Hub can be set up in different system configurations: in a single computer,
in a cluster of computers, in containers in the cloud.
The Hub is quite flexible and easy to extend for specific multi-user scenarios.

For details:

- Jupyter-Hub: [jupyterhub.readthedocs.io][]


### IPython, Jupyter-Widgets and IPyWidgets
[ipywidgets.readthedocs.io]: https://ipywidgets.readthedocs.io
[ipython.readthedocs.io/interactive/tutorial]: https://ipython.readthedocs.io/en/stable/interactive/tutorial.html
[ipython.readthedocs.io/interactive/magics]: https://ipython.readthedocs.io/en/stable/interactive/magics.html
[ipykernel.readthedocs.io]: https://ipykernel.readthedocs.io
[ipython.org]: https://ipython.org

Once upon a time, there was only IPython, and among many other things
(see the [History of Jupyter][]) `ipywidgets` as the library providing 
interactive widgets (buttons, sliders, etc) to be used in Jupyter notebooks.

It took some time for IPyWidgets to be renamed after "Jupyter", but it eventually
happened (or *is happening*).
To not break compatibility with older code-bases, the  software library is
still called `ipywidgets`.
The subproject and high-level references to the widgets were renamed to
Jupyter-Widgets.
By all means, **Jupyter-Widgets** and IPyWidgets are the very same thing.

- Jupyter-Widgets: [ipywidgets.readthedocs.io][]

Going back to IPython... The **IPython** project is responsible for many
important packages, some are fundamental and some are *just* very helpful.
For the readers of this document, I want to highlight IPython's:

- interactive shell: [ipython.readthedocs.io/interactive/tutorial][]
- magic commands: [ipython.readthedocs.io/interactive/magics][]

For more details on IPython features check [`docs.jupyter.org > Projects > IPython`](https://docs.jupyter.org/en/latest/projects/ipython_projects.html).


<!-- 
    References 
-->

[Accessibility]: https://github.com/jupyter/accessibility
[About]: https://jupyter.org/about
[Get Involved]: https://jupyter.org/community
[History of Jupyter]: ./history_of_jupyter.md
[Jupyter-Lab]: https://jupyterlab.readthedocs.io
[Governance]: https://jupyter.org/governance/intro.html
[Python]: https://en.wikipedia.org/wiki/Python_(programming_language)
[Security]: https://github.com/jupyter/security
[subprojects]: https://jupyter.org/governance/list_of_subprojects.html
