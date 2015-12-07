==================================
Contributing to the Code
==================================

How can I help?
---------------
Individuals are welcome, and encouraged, to submit issues, enhancements, and
new idea to the codebase. If you are a first-time contributor looking to get
involved with Jupyter, you can use the following query in a Github search to
find beginner-friendly issues to tackle across the Jupyter codebase.

**is:issue is:open is:sprint-friendly user:jupyter**

Once you've found an issue that you are eager to solve, you can use the guide
below to get started. If you experience any issues while working on the issue,
you can contact the mailing list or the appropriate Gitter channel.

1. Fork the repository associated with the issue you are addressing and clone
it to a local directory on your machine.

2. ``cd`` into the directory and create a new branch using ``git checkout -b
insert-branch-name-here``. Pick a branch name that gives some insight into
what the issue you are fixing is. For example, if you are updating the text
that is logged out by the program when a certain error happens you might 
name your branch `update-error-text`.

3. Reference the README of the repository you have forked and cloned for
information about how to set up the repository in development mode.

4. Identify the module or class where the code change you will make will
reside and find the test file associated with this code change. In the test
file, add some tests that outline what you expect the behavior of the change
should be. If we continue with our example of updating the text that is logged
on error, we might write test cases that check to see if the exception raised
when you induce the error contains the appropriate string. When writing test
cases, make sure that you test for the following things.

* What is the simplest test case I can write for this issue?
* What will happen if your code is given messy inputs?
* What will happen if your code is given no inputs?
* What will happen if your code is given too few inputs?
* What will happen if your code is given too many inputs?

5. Once you have created some test cases, refer to the README of the repository
that you forked and cloned for information about how to run the test suite. This
will typical require that you run the ``nosetests`` command at the commandline.
Observe that when you run the tests, the new tests that you added will fail as you
have no updated the code yet.

6. Go back to the file that you are updating and begin adding the code for your
pull request.

7. Run the test suite again to see if your changes have caused any of the test
cases to pass. If any of the test cases have failed, go back to your code and 
make the updates necessary to have them pass.

8. Once all of your test cases have passed, commit both the test cases and the
updated module and push the updates to the branch on your forked repository. Once
you have done this, you can go back to your forked repository on Github. You'll
notice a bar at the top that will allow you to submit a pull request based on
the branch that you have just pushed.

9. When creating a pull request, make sure that the title clearly and concisely
described what your code does. For example, we might use the title "Updated
error message on ExampleException". In the body of the pull request, make sure 
that you include the phrase "Closes #issue-number-here", where the issue number is
the issue number of the issue that you are addressing in this PR. 

10. After you have submitted a pull request, a project reviewer will review your
code for quality. You can expect the reviewer to check for the documentation
provided in the changes you made, how thorougb the test cases you provided are,
and how efficient your code is. Your reviewer will provide feedback on your code
and you will have the chance to edit your code and apply fixes.

11. Once your PR is perfected, it will be merged into the master branch of the main
repository and you can celebrate!

Contribution Workflow
----------------------
.. image:: http://i.imgur.com/J0Q5H7s.png
