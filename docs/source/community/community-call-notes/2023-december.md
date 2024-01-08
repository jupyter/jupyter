# Jupyter Community Call 12/13

**Date:** December 13, 2023, at 9:00AM PST (your [timezone](https://arewemeetingyet.com/Los%20Angeles/2023-12-13/9:00/Jupyter%20Community%20Call))

[**Discourse**](https://discourse.jupyter.org/t/jupyter-community-calls/668)

[**Youtube**](https://youtu.be/hUU77BfU-Kk)

**Please note:**
- Community calls are recorded and posted to this [playlist](https://www.youtube.com/playlist?list=PLUrHeD2K9Cmkoamm4NjLmvXC4Y6E1o8SP)
- These notes will be recorded and posted [here](https://jupyter.readthedocs.io/en/latest/community/community-call-notes/index.html)
- Everyone present is held to the [Jupyter Code of Conduct](https://jupyter.org/conduct)

## Purpose

Think of it as a monthly, virtual JupyterCon. It’s a place to announce and share fun things happening in the Jupyter community.

For more discussion on the format of these calls, see the thread [here](https://discourse.jupyter.org/t/reviving-the-all-jupyter-team-meetings/423).

## Short reports, celebrations, shout-outs

This is a place to make short announcements (without a need for discussion). 

* **tonyfast** - [dec community call introduction](https://github.com/tonyfast/tonyfast/blob/main/tonyfast/xxiii/2023-12-13-jupyter-community-call.ipynb)
* **Ana Ruvalcaba** Project Jupyter is now active on Mastodon! Follow us there for the latest Jupyter news and announcements. Please note that @mentions are not monitored. https://hachyderm.io/@ProjectJupyter
* **Mike Krassowski** JupyterLab 4.1 beta call for testing.


## Agenda Items

* **Michael Goerz** [A Python local `.venv` kernel](https://github.com/goerz/python-localvenv-kernel) (5 min)
* **Eric Gentry** A new in-development [JupyterLab hex editor](https://github.com/ericsnekbytes/hexlab)
* **Shravan Achar** A "Share" button for Jupyter Notebooks (5 min).
* **Nick Bollweg** [jupyak](https://github.com/deathbeds/jupyak): a pipeline pushing pulls of projects to pages of pixels for people, across the Jupyter stack
* **Kyle Kelley** demoing the Deno TypeScript kernel for jupyter.
  * [Deno Kernel Announce Post](https://blog.jupyter.org/bringing-modern-javascript-to-the-jupyter-notebook-fc998095081e)
  * [Deno Notebooks](https://github.com/rgbkrk/denotebooks)
* **Mason Williams** demoing [Pieces for Developers](https://pieces.app) and our [JupyterLab extension](https://docs.pieces.app/extensions-plugins/jupyterlab).
* **Andrey Velichkevich** A collaborative notebook training/tuning ML models on GPUs (powered by KubeFlow) (5 min).
    * KubeCon 2024 Talk for the full demo - https://youtu.be/sn2qe225E1o
    * Be involved into Kubeflow Community - https://www.kubeflow.org/docs/about/community/
* **Mike Krassowski** Inline completer API and integration with jupyter-ai.

## Notes and Other Links

This is a space to store links shared during community call discussions related to or separate from the agenda items.

### Python local-`.venv` kernel

* Project on Github: https://github.com/goerz/python-localvenv-kernel
* The FAQ: https://github.com/goerz/python-localvenv-kernel/blob/master/FAQ.md. This includes information on how to make the kernel work for something other than a `.venv` folder. For example (as asked during the call), this might be used to support `.jupyter` populated by https://github.com/jupyterlab/jupyterlab-desktop (TBD)
* Notes on the type of Makefile used in the demo: https://github.com/goerz/python-localvenv-kernel/wiki/Project-Makefile-using-Pip-Tools
* "Old" project example with an installable kernel: https://github.com/ARLQCI/2022-04_semiad_paper
* "New" project is not public yet. When published, links to example repos will be added to the `python-localvenv-kernel` README / Wiki

### Pieces for Developers | AI-Enabled Developer Workflow Assistant

* Install our JupyterLab Extension: [JupyterLab Extension Documenation page](https://docs.pieces.app/extensions-plugins/jupyterlab)
* Learn more about Pieces: [Pieces Documenation Site](https://docs.pieces.app)
* Check out our Open Source projects: [Pieces Open Source GitHub Repo](https://github.com/pieces-app/opensource)
* Join our Discord Server: [Pieces Discord Server](https://discord.gg/getpieces)

### Inline completer

- [Extension point documentation](https://jupyterlab.readthedocs.io/en/latest/extension/extension_points.html#inline-completer)
- [API documentation for `IInlineCompletionProvider`](https://jupyterlab.readthedocs.io/en/latest/api/interfaces/completer.IInlineCompletionProvider.html)
- https://github.com/krassowski/jupyterlab-transformers-completer
- https://github.com/jupyterlab/jupyter-ai/pull/465 (connecting models)
- https://github.com/jupyterlab/jupyterlab/pull/15160 (frontend)

## Attendees

|   Name   |           Institution     | GitHub Handle                     |
|----------|---------------------------|-----------------------------------|
| Shravan Achar | Apple | @shravan-achar
| Andrey Velichkevich | Apple | @andreyvelich
| Zach Sailer | Apple | @Zsailer
| [Michael Goerz](https://michaelgoerz.net) | U.S. Army Research Lab  | [@goerz](https://github.com/goerz/)
| Philipp Risius | Justus Liebig University Giessen | @philipprisius
| Nick Bollweg          | Georgia Tech           | @bollwyvl 
| Kyle Kelley | Noteable | @rgbkrk
| Amogha Kancharla     | WomeninCloudNative | @amoghak-ds
| [Mason Williams](https://masnwilliams.com) | [Pieces for Developers](https://pieces.app) | [@mason-at-pieces](https://github.com/mason-at-pieces) / [@masnwilliams](https://github.com/masnwilliams)
| Mike Krassowski | Quansight | [@krassowski](https://github.com/krassowski) |
| Eric Gentry | Anaconda | @ericsnekbytes |
| Sergey Kukhtichev | IBM | @skukhtichev |
| Ana Ruvalcaba | Project Jupyter | @Ruv7  |
| Luciano Resende | Apple | @lresende |
| Andrii Ieroshenko | AWS | @andrii-i |
| Jason Weill | AWS | @JasonWeill |
| Jeremy Tuloup | QuantStack | @jtpio |
| Simon Li | University of Dundee | @manics |
| Isabela Presedo-Floyd | Quansight Labs | @isabela-pf |
| Jared Thompson|Comcast| |
| Nicolas Brichet | QuantStack | @brichet |
| Rosio Reyes | Anaconda | @RRosio |
| Frederic Collonval | | @fcollonval |
| Carlos Brandt | Constructor University | @chbrandt |
| Rollin Thoams | NERSC | @rcthomas |
| Gabriel Fouasnon | Quansight Labs | @gabalafou |
| Jan-Hendrik Müller | University Göttingen | @kolibril13 |
| Arunav Gupta | AWS | @agupta01 |
| Ian Dong | Apple | @misterfads |
| Mehmet Bektas | Netflix | @mbektas |
| Amola Hinge | Apple | @amolahinge|
| Wayne Decatur | Upstate Medical University  | @fomightez |
| Martha Cryan | Mito | @marthacryan |
| R Ely | Bloomberg | @ohrely |
| Jialin Zhang| Apple | @jzhang20133 |
