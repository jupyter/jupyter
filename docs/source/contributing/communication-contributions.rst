====================
Communications Guide
====================

.. contents:: Contents
   :local:

Blog
====

We publish our blog at `<https://blog.jupyter.org>`_. We welcome ideas for posts
or guest posts to the Jupyter blog. If you have a suggestion for a future post,
please feel free to share your idea with us. We would like to discuss the idea
with you.

Do you enjoy writing? Please contact us about becoming a guest blogger. We can
help guide you through the process of creating a post.

Technical overview
------------------

Jupyter's blog uses the Ghost blog platform for its contributor flexibility and
ease of use. Jupyter's blog is deployed at `<https://blog.jupyter.org>`_.

Basic workflow from blog idea to published post
-----------------------------------------------

There are several major steps in the workflow from blog idea to a published post
including:

* Be inspired to write a post
* Send us a message on the Jupyter mailing list and ask us for an author account on our blog
* Creating a draft
* Draft Review
* Editorial acceptance
* Publishing the post

We'll cover each of these as well as how to update a post once it has been
published.

Creating a draft
----------------

Title and metadata
~~~~~~~~~~~~~~~~~~

Always check in the metadata fields that a blog post has a title and a canonical
URL. It is possible to put the date in the canonical URL, in particular for events
like jupyter-day, that can occur several times. The date of the event can differ
from the date of the blog post.

Once a post is published, **never** change the post's title or the url. These
changes will break links of tweets and RSS feeds that have already referenced
the existing, published URL. Keep in mind that when publishing some platforms
cache the url immediately; as a result changing the title will direct people to
a 404 page.

Title and metadata can always be refined after the actual content of the blog
is written, but should not be changed after publication. As a guest you do not
have to worry about metadata, the editor or admins will take care of that.

Working with images
~~~~~~~~~~~~~~~~~~~

Try not to link to external images. If you want to put an image in the post,
insert ``![]()`` in the editor view and drag and drop an image from your
desktop into the newly created field in the preview. External images can
change, and can break the blog post if they are taken down. This cannot append
if you drag and drop images. Moreover, these images  will be served from the
same CDN (Content Delivery Network) as the blog, which will insure the best
overall experience for our readers.

The featured image you see at the top of a blog posts is set from within the
metadata field, not using the `![]()`. The featured image is treated differently
than inlined images by many feedreaders (especially on mobile) and allows a user
on a slow connection to read the content of the blog earlier, which is a much
better experience for the user than waiting for the featured image to render.

Links
~~~~~

Do not use minified links when possible. The multiple redirects of minified
links degrades the mobile browsing experience. If you need analytics of
the number of page views, this information is tracked by Google Analytics.

Draft review
------------

Ask for a review
~~~~~~~~~~~~~~~~

Once you think you are done, ask someone else to reread your post, and check
the various parameters that you might have forgotten before publishing.
You are not on your own, this is teamwork, we are here to help you.
If we do things in a hurry you will probably spend more time fixing mistakes
that actually doing things right in a first place.

Editorial acceptance
--------------------

Publishing the post
~~~~~~~~~~~~~~~~~~~

Usually an editor or admin will take care of publishing the post. The task of
the Editor/Admin is to check all metadata are correctly set, that no external
images are used, as well as all other quality check describe before.

It is then just a matter of making th post visible to everyone.

Changing an existing post
~~~~~~~~~~~~~~~~~~~~~~~~~

Posts Updates
^^^^^^^^^^^^^

Blog subscribers may receive notification at every update. So use updates and
fixes parsimoniously. It is OK to wait a few hours to fix a typo.

If some substantial updates have to be made, like change of location, time etc,
please insert an `[Update]` section at top (or bottom of the blog post
depending on importance) with the Date/Time of the update. If the information
in the body of the blog is wrong, try not to replace it, and just use
strike-through to mark it as obsolete. This would help reader determine which
information is correct when dealing with multiple source giving different
information.

Newsletter
==========

Newsletter Overview
-------------------

Jupyter periodically sends out newsletters to keep the community informed about
important updates, events, releases, and other relevant information. These are
typically shared via email and posted on our website.

Contributing to the Newsletter
------------------------------

If you have an announcement, event, or update you'd like to share with the
broader Jupyter community, you can submit it for inclusion in the next
newsletter. Please email the core team with your proposed content.

Content Guidelines
------------------

* Keep submissions brief, clear, and to the point.
* Include relevant dates, links, and contact information.
* Use proper grammar and avoid jargon when possible.
* Please submit any images or logos along with alt-text descriptions.

Schedule and Archive
--------------------

Newsletters are typically published monthly or quarterly. Past issues are
archived on the Jupyter website and may also be linked in future
communications for reference.

Website
=======

Overview
--------

The Jupyter website (https://jupyter.org) is the main portal for accessing
project information, documentation, downloads, and community resources.

Contributing to the Website
---------------------------

The website source is maintained as a GitHub repository. If you find a typo,
broken link, or want to improve content, you can:

1. Fork the repository
2. Make your changes
3. Submit a pull request

Website contributions go through the same review process as other
documentation and must follow the style and tone of the project.

Structure and Content
---------------------

The website is built using static site generators and includes:

* Overview of the Jupyter ecosystem
* Links to key projects like JupyterLab and Jupyter Notebook
* Tutorials and getting started guides
* Community and contributor information

Hosting and Deployment
----------------------

The site is deployed via GitHub Pages and updates automatically when changes
are merged into the main branch of the repository. Make sure to test your
changes locally before submitting them for review.
