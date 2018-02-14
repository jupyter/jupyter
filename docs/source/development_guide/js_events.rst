.. _js_events:

JavaScript Events
=================

.. attention::
    This is copied verbatim from the old IPython wiki and is currently under development. Much of the information in this part of the development guide is out of date.

(Note: this page is not currently consistent with IPython/Jupyter master)

Javascript events are used to notify unrelated parts of the notebook
interface when something happens. For example, if the kernel is busy
executing code, it may send an event announcing as such, which can then
be picked up by other services, like the notification area. For details
on how the events themselves work, see the `JQuery
documentation <http://api.jquery.com/on/>`__.

This page documents the core set of events, and explains when and why
they are triggered.

Cell-related events
-------------------

-  `command\_mode.Cell <#command_modecell>`__
-  `create.Cell <#createcell>`__
-  `delete.Cell <#deletecell>`__
-  `edit\_mode.Cell <#edit_modecell>`__
-  `select.Cell <#selectcell>`__
-  `output\_appended.OutputArea <#output_appendedoutputarea>`__

CellToolbar-related events
--------------------------

-  `preset\_activated.CellToolbar <#preset_activatedcelltoolbar>`__
-  `preset\_added.CellToolbar <#preset_addedcelltoolbar>`__

Dashboard-related events
------------------------

-  `app\_initialized.DashboardApp <#app_initializeddashboardapp>`__
-  `sessions\_loaded.Dashboard <#sessions_loadeddashboard>`__

app\_initialized.DashboardApp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the Jupyter Notebook browser window opens for the first time and
initializes the Dashboard App. The Dashboard App lists the files and
notebooks in the current directory. Additionally, it lets you create and
open new Jupyter Notebooks.

Kernel-related events
---------------------

-  `execution\_request.Kernel <#execution_requestkernel>`__
-  `input\_reply.Kernel <#input_replykernel>`__
-  `kernel\_autorestarting.Kernel <#kernel_autorestartingkernel>`__
-  `kernel\_busy.Kernel <#kernel_busykernel>`__
-  `kernel\_connected.Kernel <#kernel_connectedkernel>`__
-  `kernel\_connection\_failed.Kernel <#kernel_connection_failedkernel>`__
-  `kernel\_created.Kernel <#kernel_createdkernel>`__
-  `kernel\_created.Session <#kernel_createdsession>`__
-  `kernel\_dead.Kernel <#kernel_deadkernel>`__
-  `kernel\_dead.Session <#kernel_deadsession>`__
-  `kernel\_disconnected.Kernel <#kernel_disconnectedkernel>`__
-  `kernel\_idle.Kernel <#kernel_idlekernel>`__
-  `kernel\_interrupting.Kernel <#kernel_interruptingkernel>`__
-  `kernel\_killed.Kernel <#kernel_killedkernel>`__
-  `kernel\_killed.Session <#kernel_killedsession>`__
-  `kernel\_ready.Kernel <#kernel_readykernel>`__
-  `kernel\_reconnecting.Kernel <#kernel_reconnectingkernel>`__
-  `kernel\_restarting.Kernel <#kernel_restartingkernel>`__
-  `kernel\_starting.Kernel <#kernel_startingkernel>`__
-  `send\_input\_reply.Kernel <#send_input_replykernel>`__
-  `shell\_reply.Kernel <#shell_replykernel>`__
-  `spec\_changed.Kernel <#spec_changedkernel>`__

kernel\_created.Kernel
^^^^^^^^^^^^^^^^^^^^^^

The kernel has been successfully created or re-created through
``/api/kernels``, but a connection to it has not necessarily been
established yet.

kernel\_created.Session
^^^^^^^^^^^^^^^^^^^^^^^

The kernel has been successfully created or re-created through
``/api/sessions``, but a connection to it has not necessarily been
established yet.

kernel\_reconnecting.Kernel
^^^^^^^^^^^^^^^^^^^^^^^^^^^

An attempt is being made to reconnect (via websockets) to the kernel
after having been disconnected.

kernel\_connected.Kernel
^^^^^^^^^^^^^^^^^^^^^^^^

A connection has been established to the kernel. This is triggered as
soon as all websockets (e.g. to the shell, iopub, and stdin channels)
have been opened. This does not necessarily mean that the kernel is
ready to do anything yet, though.

kernel\_starting.Kernel
^^^^^^^^^^^^^^^^^^^^^^^

The kernel is starting. This is triggered once when the kernel process
is starting up, and can be sent as a message by the kernel, or may be
triggered by the frontend if it knows the kernel is starting (e.g., it
created the kernel and is connected to it, but hasn't been able to
communicate with it yet).

kernel\_ready.Kernel
^^^^^^^^^^^^^^^^^^^^

Like kernel\_idle.Kernel, but triggered after the kernel has fully
started up.

kernel\_restarting.Kernel
^^^^^^^^^^^^^^^^^^^^^^^^^

The kernel is restarting. This is triggered at the beginning of an
restart call to ``/api/kernels``.

kernel\_autorestarting.Kernel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The kernel is restarting on its own, which probably also means that
something happened to cause the kernel to die. For example, running the
following code in the notebook would cause the kernel to autorestart:

::

    import os
    os._exit(1)

kernel\_interrupting.Kernel
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The kernel is being interrupted. This is triggered at the beginning of a
interrupt call to ``/api/kernels``.

kernel\_disconnected.Kernel
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The connection to the kernel has been lost.

kernel\_connection\_failed.Kernel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Not only was the connection lost, but it was lost due to an error (i.e.,
we did not tell the websockets to close).

kernel\_idle.Kernel
^^^^^^^^^^^^^^^^^^^

The kernel's execution state is 'idle'.

kernel\_busy.Kernel
^^^^^^^^^^^^^^^^^^^

The kernel's execution state is 'busy'.

kernel\_killed.Kernel
^^^^^^^^^^^^^^^^^^^^^

The kernel has been manually killed through ``/api/kernels``.

kernel\_killed.Session
^^^^^^^^^^^^^^^^^^^^^^

The kernel has been manually killed through ``/api/sessions``.

kernel\_dead.Kernel
^^^^^^^^^^^^^^^^^^^

This is triggered if the kernel dies, and the kernel manager attempts to
restart it, but is unable to. For example, the following code run in the
notebook will cause the kernel to die and for the kernel manager to be
unable to restart it:

::

    import os
    from IPython.kernel.connect import get_connection_file
    with open(get_connection_file(), 'w') as f:
        f.write("garbage")
    os._exit(1)

kernel\_dead.Session
^^^^^^^^^^^^^^^^^^^^

The kernel could not be started through ``/api/sessions``. This might be
because the requested kernel type isn't installed. Another reason for
this message is that the kernel died or was killed, but the session
wasn't.

Notebook-related events
-----------------------

-  `app\_initialized.NotebookApp <#app_initializednotebookapp>`__
-  `autosave\_disabled.Notebook <#autosave_disablednotebook>`__
-  `autosave\_enabled.Notebook <#autosave_enablednotebook>`__
-  `checkpoint\_created.Notebook <#checkpoint_creatednotebook>`__
-  `checkpoint\_delete\_failed.Notebook <#checkpoint_delete_failednotebook>`__
-  `checkpoint\_deleted.Notebook <#checkpoint_deletednotebook>`__
-  `checkpoint\_failed.Notebook <#checkpoint_failednotebook>`__
-  `checkpoint\_restore\_failed.Notebook <#checkpoint_restore_failednotebook>`__
-  `checkpoint\_restored.Notebook <#checkpoint_restorednotebook>`__
-  `checkpoints\_listed.Notebook <#checkpoints_listednotebook>`__
-  `command\_mode.Notebook <#command_modenotebook>`__
-  `edit\_mode.Notebook <#edit_modenotebook>`__
-  `list\_checkpoints\_failed.Notebook <#list_checkpoints_failednotebook>`__
-  `notebook\_load\_failed.Notebook <#notebook_load_failednotebook>`__
-  `notebook\_loaded.Notebook <#notebook_loadednotebook>`__
-  `notebook\_loading.Notebook <#notebook_loadingnotebook>`__
-  `notebook\_rename\_failed.Notebook <#notebook_rename_failednotebook>`__
-  `notebook\_renamed.Notebook <#notebook_renamednotebook>`__
-  `notebook\_restoring.Notebook <#notebook_restoringnotebook>`__
-  `notebook\_save\_failed.Notebook <#notebook_save_failednotebook>`__
-  `notebook\_saved.Notebook <#notebook_savednotebook>`__
-  `notebook\_saving.Notebook <#notebook_savingnotebook>`__
-  `rename\_notebook.Notebook <#rename_notebooknotebook>`__
-  `selected\_cell\_type\_changed.Notebook <#selected_cell_type_changednotebook>`__
-  `set\_dirty.Notebook <#set_dirtynotebook>`__
-  `set\_next\_input.Notebook <#set_next_inputnotebook>`__
-  `trust\_changed.Notebook <#trust_changednotebook>`__

Other
-----

-  `open\_with\_text.Pager <#open_with_textpager>`__
-  `rebuild.QuickHelp <#rebuildquickhelp>`__
