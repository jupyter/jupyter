# What is Jupyter?

"Jupyter" can mean a lot of things, so let's start from the beginning, and
break it down:

First and foremost, "Project Jupyter" is a large umbrella project that covers
many different software offerings and tools. That includes "Jupyter Notebook"
and "JupyterLab", which are both popular web-based notebook editor programs.
The Jupyter project, and its subprojects, all center around providing tools
(and standards) for interactive computing with computational notebooks. Each
of these will be explored further below.

The term "Jupyter" is often used as a shorthand to refer to one of those
products or ideas, which sometimes leads to confusion. Let's take a look at
each of those, one-by-one.

# What is a "Computational Notebook" anyway?

A famous computer programmer (Donald Knuth) popularized the idea to combine
explanatory plain english text with computer code, which is commonly called
"literate programming". By adopting this practice, computer programs, as well
as other complex information and ideas, could be better explained to a wide
range of people.

A program written in this way could be printed on paper and shared by hand
as an actual "notebook", but in modern times, they are shared digitally as
"notebook files", and can contain additional rich media like images, 3D models
and interactive figures, along with data and other program outputs.

By opening a notebook with an editor program like JupyterLab, you can also
run the code inside the notebook. Since a notebook can contain code that does
virtually anything, you can do nearly anything regular software can do inside
a notebook. For example, a notebook file might be used to:

- Read spreadsheets (or create them) to build reports about your household spending
- Show proof of a graduate student's thesis with interactive graphs and source data
- Generate an image of a black hole by processing telescope data (CHECK/LINK)
- Calculate the presence of gravitational waves from observatory data (CHECK/LINK)
- Process astronomical data from the James Webb Space Telescope (JWST) (CHECK/LINK)

Those last three are real world examples that demonstrate the scientific
community's usage of computational notebooks (CHECK). Because scientists,
engineers, and other technical people so often need to perform and communicate
sophisticated calculations to describe their work, these "computational
notebooks" became a very popular way to share their work and ideas.

Notebooks are not just for Nasa scientists either: Students, hobbyists, and
business people commonly use the fast, interactive workflows in JupyterLab to
make notebooks that help solve everyday problems. You can use them to explain
your own ideas to others, to learn, to automate tasks at home or work,
visualize complex information, and more.

When someone uses the term "notebook", they might be referring to:

- A notebook file on their computer
- The idea of combining computer code, explanatory text, images and more into
  the "notebook format"
- The "Jupyter Notebook" application, used to author and edit digital notebook
  files
- Jupyter's ``.ipynb`` notebook file format, interpreted by the ``nbformat``
  software library

And the term "Jupyter" might refer to:

- "Project Jupyter", the overarching umbrella project
- The "Jupyter Notebook" or "JupyterLab" editing programs (or other Jupyter
  products)

The name Jupyter comes from the three programming languages the project
originally supported: Julia (ju), Python (pyt) and R (r).

# How do the Jupyter notebook-editor programs work?

It is common for notebook editor programs like JupyterLab, or Jupyter
Notebook, to share some features and workflows, because they are influenced
by a common set of ideas about computational notebooks, their advantages,
and how best to work with them effectively.

Let's break down some of those ideas.

## Interactive programming (the REPL)

In the past, writing programs, running them, and seeing results was commonly
a slower and more deliberative process than it is today.

As time passed, new techniques were discovered that sped up the process between
writing code, running it, and seeing results. Languages like Python were also
later introduced that offered some unique advantages over older languages.

For instance, Python is an interpreted language, so it does not need to be
compiled (LINK) before it can be run (saving programmers steps and time).
It is also a dynamically-typed language that does not require the programmer
to specify the type of their data ahead of time before using it, which can
sometimes save time and reduce the complexity of code (particularly for
smaller, simpler programs).

Another programming technique (which is key to the Jupyter notebook-editing
programs) is the Read-Eval-Print-Loop (REPL), which allows a programmer to
interactively write code, run it, keep their data and variables intact, then
rewrite, re-run, and refine their code on-the-fly (without losing data
after the program finishes running).

A REPL is so named because the programmer writes snippets of code that are
first read (R), then Evaluated (E) or in other words executed, the results
are printed (P) to some kind of display or output, and that process happens
repeatedly in a loop (L), where the REPL waits until the programmer has
another snippet of code to execute.

New snippets of code can refer to variables defined in previous Eval steps,
because the REPL keeps objects that were created (by previous runs of the
loop) in-memory, until the user closes their REPL.

## Kernels

Notebook editor programs like JupyterLab create a REPL (read more about those
above) for each of your open notebook files, in a language of your choice. In
the Jupyter ecosystem, each of these REPL's is called a kernel, and it holds
the data and objects you create with your notebook code in a long-running
program on your computer (the management and creation of these kernels
is orchestrated by the Jupyter Server (LINK), more on that later).

This is why you don't lose your data and variables when you execute multiple
notebook cells in a row, they stay alive inside the REPL so that you can
continue to use them to explore the data and problem you are investigating
(though if you shut down the Jupyter server that holds the kernels, you will
lose those variables).

The kernels that run in the background for each of your notebooks are what
power the fast, exploratory programming workflows that Jupyter notebook
editor programs excel at.

## Multiple programs, one experience (client-server architecture)

Most Notebook editor programs in Project Jupyter, like JupyterLab, may seem like
a single experience, but when you run JupyterLab on your laptop, there are
actually several programs running independently that all coordinate with
each other to offer you the notebook editing experience you may already be
familiar with.

This might seem like an unnecessary background detail, but some clarity on
the inner workings can help demystify your notebook authoring experience, and
open up new features, ideas and workflows that you can take advantage of.

A many-pieces (modular) approach also has advantages for people using Jupyter
software, and to the people who write it.

Let's break down some of the pieces.

JupyterLab's interface is a web app that you open in a browser program
like FireFox or Google Chrome (websites themselves commonly have code
that defines their behavior, and JupyterLab's interface is no exception).

Jupyter Server (LINK) runs in the background, and it orchestrates the creation,
management of, and communication with, your notebook kernels while you're
running your notebooks.

Jupyter kernels themselves are independent programs (operating system
processes), and each one is its own REPL in whatever language you
requested (commonly Python, though hundreds of other languages and
kernels are also available LINK_HERE).

With this design, any program (that you enable) can talk to your kernels
using common internet communication technologies like HTTP. This gives
you the power to edit, view, share, and manipulate your data across many
different programs. One kernel can even connect to multiple editing programs
simultaneously! (Similarly, in JupyterLab, you can connect a notebook and a
console to the same kernel!)

Project Jupyter actually defines a standard (LINK) that other programs can
follow that will allow them to hook into your kernels in virtually any way
you can imagine. You can invent new editing and viewing experiences for your
data this way, using the interactive computing capabilities provided by
the kernels.

## Benefits of a many-piece design

By breaking up a program like JupyterLab into multiple component pieces, you
can customize the software to meet your needs. If one piece is missing something,
you can replace it with a custom version made by yourself or another person to
add whatever features you would like to see.

You can also invent completely new experiences using those pieces that the
designers may not have imagined when they started, and they can often inter-
operate seamlessly with existing Jupyter software.

Because Jupyter Server provides kernel communication and management features
in a cohesive, self-contained package, for instance, new notebook editor
programs can focus solely on adding new interface and editing experiences,
leaving the task of creating and managing new kernels completely up to the
Jupyter Server.

JupyterCAD is a 3D modeling tool built on top of Jupyter software, for
instance, and there are other examples too (LINK HERE).

## Talking to Kernels (The Jupyter Protocol)

Anyone can make new software that talks to Jupyter's kernels (read more
about those above), by using the Jupyter Protocol. The protocol provides
a standardized blueprint for passing information back and forth between
the kernels and other software.

By implementing the designs described in the Jupyter Protocol, you could
invent a completely new interactive programming experience, or add support
for a new programming language to Jupyter.

Because Project Jupyter is free and open, it encourages anyone to explore
new ways of working with their notebooks and kernels, and likes to offer
compatibility and interoperation with other software.

TODO add more here? examples? etc.

# What else should I know about Project Jupyter?

Jupyter software is free and open-source, developed by a global community
of volunteers and contributors, available for the benefit of all.

Project Jupyter welcomes people from all backgrounds and with many types
of skills (not just software!) so we encourage you to join us!

You can share feedback about your experiences directly with the people who
make Jupyter software, or volunteer and contribute to help Jupyter in many
different ways, like:

- Writing tutorials
- Testing newly released versions
- Adding software features
- Hosting the weekly video meetings (LINK)
- Helping others in the community
- ...and more!

The project is split into largely independent subprojects which handle
different aspects of Jupyter software and the community. A central council,
the Jupyter Executive Council (LINK), makes decisions about project-wide
goals and policies, while different subprojects handle the actual development
of the various software components.

Some subprojects take care of broader topics, such as the [Accessibility][],
[Security][], [Community][], and [Documentation][] projects.

# A (Partial) Tour of the Jupyter Universe

In the following sections, we are going to look at some popular components of
the Jupyter ecosystem. This is *not* a comprehensive reference of every aspect
of Jupyter, but rather a big-picture summary that should help illustrate some
important parts that were discussed earlier.

If you are completely new to *Jupyter*, the project's [About][] page is good
reading that will introduce you to many of the different subprojects.

If you want to know more about the organizational structure, check out the
[Governance][] pages.

And if you would like to contribute to the project, have a look at the
[Get Involved][] page.

The graph below presents the best known software components of the Project.

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

### Notebook Editor Programs

[jupyterlab.readthedocs.io]: https://jupyterlab.readthedocs.io
TODO Notebook link

The two most popular notebook editor programs are Jupyter-Notebook and
JupyterLab, though there are others. Which one you choose to use is
mostly a matter of preference (both Notebook and Lab provide many of the
same capabilities for editing and running notebooks):

- Jupyter Notebook offers a simplified, lightweight notebook authoring
  experience

- JupyterLab offers a more customizable, feature-rich, tabbed multi-notebook
  editing environment, and has additional tools like a customizable layout
  and system console (a common tool used by programmers)

- And more...read about additional notebook interfaces here (LINK)!

A professor, for instance, might use JupyterLab for their daily work as a data
analyst, and Jupyter Notebook while teaching to provide a cleaner, more focused
view of the notebook's content.

### The notebook format

Jupyter uses the .ipynb format to store your notebook files (where the data
and outputs of your notebook reside for long term storage). The .ipynb format
is interpreted and modified by the nbformat software library.

TODO: features, more info, basic exmaplanation of how it works/structure

[nbformat.readthedocs.io]: https://nbformat.readthedocs.io

### JupyterHub

[jupyterhub.readthedocs.io]: https://jupyterhub.readthedocs.io

JupyterHub provides a multi-user management system where many different people
can log in and use their own isolated notebook editor program and environment.

With JupyterHub, editing and running notebook files is still performed by an
editor program like Lab or Notebook. The Hub is responsible for authenticating
users and providing them their corresponding Lab/Notebook instance connection.

Jupyter-Hub can be set up in different system configurations:

- In a single computer
- In a cluster of computers
- In containers in the cloud

JupyterHub is quite flexible for many different multi-user scenarios.

### IPython

- XXXXX Jupyter-Widgets and IPyWidgets

[ipywidgets.readthedocs.io]: https://ipywidgets.readthedocs.io
[ipython.readthedocs.io/interactive/tutorial]: https://ipython.readthedocs.io/en/stable/interactive/tutorial.html
[ipython.readthedocs.io/interactive/magics]: https://ipython.readthedocs.io/en/stable/interactive/magics.html
[ipykernel.readthedocs.io]: https://ipykernel.readthedocs.io
[ipython.org]: https://ipython.org

A long time ago, a precursor to Jupyter was created, called ipython (see
the [History of Jupyter][] to learn more about that). It provided some of
the same fast, advanced REPL features that Jupyter still has today, and it
is the default Python kernel bundled with JupyterLab and Notebook. Some of
the features ipython provides:

- Foobar
- Bizbaz
- WikRakRum
- interactive shell: [ipython.readthedocs.io/interactive/tutorial][]
- magic commands: [ipython.readthedocs.io/interactive/magics][]

For more details on IPython features check [`docs.jupyter.org > Projects > IPython`](https://docs.jupyter.org/en/latest/projects/ipython_projects.html).

### Interactive Buttons, Sliders and more with ipywidgets

ipywidgets provides interactive interface elements that you can add directly
into your notebooks.

- Note: The subproject and high-level references to the widgets were renamed to
Jupyter-Widgets, but Jupyter-Widgets and IPyWidgets are the very same thing. To
not break compatibility with older code-bases, the software library is
still called `ipywidgets`.

- Jupyter-Widgets: [ipywidgets.readthedocs.io][]

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
