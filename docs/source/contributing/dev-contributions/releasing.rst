.. _releasing-Jupyter-Project:

==============================================
Basic template for releasing a Jupyter project
==============================================

Jupyter consists of a bunch of small projects, and a few larger ones.
This lays out the basic process of releasing a smaller project,
which should also apply to larger projects,
though they may have some added steps.


Milestones
==========

Most Jupyter projects use a GitHub milestone system for marking issues and pull requests in releases.
Each release should have a milestone associated with it.
The first step in preparing for a release is to make sure that every issue and pull request has the right milestone.

1. Go through any **open** Issues and Pull Requests marked with the current milestone.
   If there are any, they need to be resolved or bumped to the next milestone.
   It's fine to bump issues - they are typically marked with the earliest feasible milestone,
   but many such optimistically marked tasks aren't complete when it's time to release.
   There's always next time!
2. Check **closed** Issues and Pull Requests,
   using the milestone filter "Issues with no milestone".
   There should never be any closed issues or pull requests without a milestone.
   If you find any, go through and mark them with the current milestone or "no action"
   as appropriate.

A release may be ready to go when it has zero open issues or pull requests.


Release notes
=============

Once all the issues and pull requests are dealt with,
it's time to make release notes.
The smaller projects generally have a :file:`changelog.rst` in the docs directory,
where you can add a section for the new release.
Look through the pull requests merged for the current milestone (this is why we use milestones),
and write a short summary of the highlights of the changes in this release.
There should generally be a link to the milestone itself for more details.

Make a pull requests with these notes.
It's a good idea to cc @willingc for review of this PR.
Make sure to mark this PR with your release's milestone!


Making the release
==================

Now that your changelog is merged, we can actually build and publish the release.
We'll assume that ``V`` has been declared as a shell variable containing the release version::

    export V=5.1.2

Start by making sure you have a clean checkout of master, with no extra files::

    git pull
    git clean -xfd

First, update the version of the package, often in the file :file:`<pkg>/_version.py` or similar.

Commit that change::

    git commit -am "release $V"

.. note::

    At this point, I like to run the tests
    just to be sure that setting the version didn't confuse anything.

Build the distributions::

    python setup.py sdist --formats=gztar
    python setup.py bdist_wheel

Tag the commit::

    git tag -am "release $V" $V

And finally, publish everything, to GitHub and PyPI using `twine <https://github.com/pypa/twine>`_::

    twine upload dist/*
    git push origin
    git push origin --tags

We have a release! You can now bump the version to the next '.dev' version,
by editing :file:`<pkg>/_version.py` (or similar) again, and commit::

    git commit -am "back to dev"
    git push origin

.. note::

    The pushes assume that `origin` points to the main jupyter/ipython repo.
    Depending on how you use git, this could be `upstream` or something else.
