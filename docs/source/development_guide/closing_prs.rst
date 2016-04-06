.. _closing_prs:

Policy on Closing Pull Requests
===============================

.. attention::
    This is copied verbatim from the old IPython wiki and is currently under development. Much of the information in this part of the development guide is out of date.

IPython has the following policy on closing pull requests. The goal of
this policy is to keep our pull request queue small and allow us to
focus on code that is being actively developed and has a strong chance
of being merged in master soon.

A pull request will be closed when:

-  It has been reviewed, but has sat for a month or more waiting for the
   submitter to commit more code to address the comments.
-  The review process has uncovered larger design or technical issues
   that extend beyond the details of the specific pull request.

   -  In particular, we do not accept whole large "cleanup" changes
      which do not address any specific bug. This includes trailing
      whitespace, PEP8, etc. One of the reasons is that such massive
      cleanup provide plenty of opportunities to introduce new and
      subtle bugs.

In general we will not close pull requests because of a lack of review.
If a pull request has sat for a month or more without review, we need to
kick ourselves and get to reviewing it.

When a pull request is closed we will do the following:

-  Post a github message to the pull request to confirm that everyone is
   fine with closing the pull request. This message should cite this
   policy.
-  Open an issue to track the pull request. This issue should describe
   what would be needed in order to reopen the pull request.
-  Post a github message to the pull request encouraging the submitter
   to continue with the work and detail what issues need to be addressed
   in order for the pull request to be reopened.

This policy was discussed in the following thread:

https://mail.scipy.org/pipermail/ipython-dev/2012-August/010025.html

Example Message:
----------------

.. code:: text

    Hi,

    This PR has been inactive for 1 month now, so we are going to close it and open an
    issue to reference it. We try to keep our pull request queue small and focused on
    active work.  We encourage you to reopen the pull request if and when you
    continue to work on this. Please contact us if you have any questions.

    Thanks for contributing.

    see https://github.com/ipython/ipython/wiki/Dev%3A-Closing-pull-requests/ for 
    our policies on closing pull request.
