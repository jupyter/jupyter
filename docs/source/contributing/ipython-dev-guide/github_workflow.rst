.. _github_workflow:

IPython on GitHub
=================

.. attention::
    This is copied verbatim from the old IPython wiki and is currently under development. Much of the information in this part of the development guide is out of date.

Notes on working with GitHub

.. _github_workflow_milestones:

Milestones
----------

-  100% of confirmed issues should have a milestone.
-  An issue should never be closed without a milestone.
-  All pull requests should have a milestone.
-  All issues closed should be marked with the next release milestone,
   next backport milestone, or **no action**.
-  Open issues should only lack a milestone if:

   -  more clarification is required (label: ``needs-info``)

-  In general, there will be four milestones with open issues:

   -  **next minor release**. This milestone contains issues that should
      be backported for the next minor release. See
      `below <#backporting>`__ for information on backporting.
   -  **next major release**. This should be the default milestone of
      all issues. As the release approaches, issues can be explicitly
      bumped to next release + 1.
   -  **next major release + 1**. Only issues that we are confident will
      *not* be included in the next release go here. This milestone
      should be mostly empty until relatively close to release.
   -  **wishlist**. This is the milestone for issues that we have no
      immediate plans to address.

-  The remaining milestone is **no action** for open or closed issues
   that require no action:

   -  Not actually an issue (e.g. questions, discussion, etc.)
   -  Duplicate of an existing Issue
   -  Closed because we won't fix it
   -  When an issue is closed with **no action**, it means that the
      issue will not be fixed, or it was not an issue at all.

-  When closing an issue, it should always have one of these milestones:

   -  **next minor release** because the issue has been addressed
   -  **next major release** because the issue has been addressed
   -  **no action** because the issue *will not* be addressed, or it is
      a duplicate/non-issue.

In general: When in doubt, mark with **next release**. We can always
push back when we get closer to a given release.

Labels and issues
-----------------

Issues should always be labeled once they are confirmed (not necessary
for issues that are still being clarified, or may be duplicates or not
issues at all).

Some significant labels:

-  ``needs-info``: issue needs more information from submitter before
   progress can be made
-  ``bug``: errors are raised, or unintended behavior occurs
-  ``enhancement``: improvements that are not bugs
-  

   .. raw:: html

      <del>

   backport-X.Y.Z: Any fix for this issue should be backported to the
   maintenance branch. backports are expressed with milestones, starting
   with 2.1.
-  ``prio-foo``: a priority level for ranking issues - nonessential, but
   prio-high/low are useful for explicitly promoting/demoting issues,
   particularly when nearing release.
-  ``ClosedPR``: This issue is a reminder for a PR that was closed for
   going stale.
-  ``sprint-friendly``: Obvious or easy fixes, where

All confirmed issues should at least have a ``bug`` or ``enhancement``
label, and be marked with any affected components (e.g ``parallel``,
``qtconsole``, ``htmlnotebook``), or particular sources of error (e.g.
``py3k`` or ``unicode``) if we have appropriate labels.

The ``sprint-friendly`` label is probably the best place for new
contributors to start.

Pull Requests
-------------

-  All work is submitted via Pull Requests.
-  Pull Requests can be submitted as soon as there is code worth
   discussing. Pull Requests track the branch, so you can continue to
   work after the PR is submitted. Review and discussion can begin well
   before the work is complete, and the more discussion the better. The
   worst case is that the PR is closed.
-  Pull Requests that have stalled should be closed (see [[our policy on
   closing PRs\|Dev: Closing Pull Requests]])
-  Pull Requests should always be made against master (backporting PRs
   is described below).
-  Pull Requests should be tested, if feasible:

   -  bugfixes should include regression tests
   -  new behavior should at least get minimal exercise

`Travis <https://travis-ci.org/ipython/ipython>`__ does a pretty good
job testing IPython and Pull Requests, but it may make sense to manually
perform tests (possibly with our ``test_pr`` script), particularly for
PRs that affect ``IPython.parallel`` or Windows.

Opening an Issue
----------------

When opening a new issue, please take the following steps:

1. Search GitHub and/or Google for your issue to avoid duplicate
   reports. Keyword searches for your error messages are most helpful.
2. If possible, try updating to master and reproducing your issue,
   because we may have already fixed it.
3. Try to include a minimal reproducible test case
4. Include relevant system information. Start with the output of:

   ::

       python -c "import IPython; print(IPython.sys_info())"

And include any relevant package versions, depending on the issue, such
as matplotlib, numpy, Qt, Qt bindings (PyQt/PySide), tornado, web
browser, etc.

Backporting
-----------

-  We should keep an ``A.x`` maintenance branch for backporting fixes
   from master.
-  That branch shall be called ``A.x``, e.g. ``2.x``, not ``2.1``. This
   way, there is only one maintenance branch per release series.
-  When an Issue is determined to be appropriate for backporting, it
   should be marked with the ``A.B`` milestone.
-  Any Pull Request which addresses a backport issue should also receive
   the same milestone.
-  Patches are backported to the maintenance branch by applying the pull
   request patch to the maintenance branch (currently with the
   `backport\_pr <https://github.com/ipython/ipython/blob/master/tools/backport_pr.py>`__
   script).
