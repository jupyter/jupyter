================================
Contributing to the Jupyter Blog
================================

We publish our blog at `<https://blog.jupyter.org>`_. We welcome ideas for posts
or guest posts to the Jupyter blog. If you have a suggestion for a future post,
please feel free to share your idea with us. We would like to discuss the idea
with you.

Do you enjoy writing? Please contact us about becoming a guest blogger. We can
help guide you through the process of creating a post.

Technical overview
------------------
Jupyter's blog uses the Ghost blog platform for its contributor flexiblity and
ease of use. Jupyter's blog is deployed at `<https://blog.jupyter.org>`_.

Basic workflow from blog idea to published post
-----------------------------------------------
There are several major steps in the workflow from blog idea to a published post
including:

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

Alway check in the metadata fields that a blog post has a title and a canonical
URL. It is possible to put the date in the canonical URL, in particular for events
like jupyter-day, that can occur several times. The date of the event can differ
from the date of the blog post. 

Once a post is published, **never** change the post's title or the url. These
changes will break links of tweets and RSS feeds that have already referenced
the existing, published URL. Keep in mind that when publishing some
platforms cache the url immediately; as a result changing the title may direct
people to a 404 page.

Working with images
~~~~~~~~~~~~~~~~~~~

Try not to link to external images. If you want to put an image in the post,
insert ``![]()`` in the editor and drag and drop an image from your desktop
into the newly created field. External images can change, and can break the
blog post if they are taken down, if you drag and drop images they will be
served from the same CDN (Content Delivery Network) as the blog, which will
insure the best overall experience for our readers.

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
You are not on your own, this is teamwork !
If we do things in a hurry you will probably spend more time fixing mistakes 
that actually doing things right in a first place. 

Editorial acceptance
--------------------

Publishing the post
-------------------

Changing an existing post
-------------------------

Posts Updates
~~~~~~~~~~~~~

Blog subscribers may receive notification at every update. So use updates and
fixes parsimoniously. It is OK to wait a few hours to fix a typo. 
