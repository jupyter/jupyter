.. _rest_api:

Architecture of IPython notebook's Dashboard
============================================

.. attention::
    This is copied verbatim from the old IPython wiki and is currently under development. Much of the information in this part of the development guide is out of date.

The tables below show the current RESTful web service architecture
implemented in IPython notebook. The listed URL's use the HTTP verbs to
return representations of the desired resource.

We are in the process of creating a new dashboard architecture for the
IPython notebook, which will allow the user to navigate through multiple
directory files to find desired notebooks.

Current Architecture
--------------------

Miscellaneous

+------------+-----------------+----------------------------------------+
| HTTP       | URL             | Action                                 |
| verb       |                 |                                        |
+============+=================+========================================+
| ``GET``    | /.\*/\          |  Strips trailing slashes.              |
+------------+-----------------+----------------------------------------+
| ``GET``    | \/api\          |  Returns api version information.      |
+------------+-----------------+----------------------------------------+
| ``*``      | \/api/notebooks |  Deprecated: redirect to /api/contents |
+------------+-----------------+----------------------------------------+
| ``GET``    | \/api/nbconvert |                                        |
+------------+-----------------+----------------------------------------+

Notebook contents API.

+------------+-----------------+----------------------------------------+
| HTTP       | URL             | Action                                 |
| verb       |                 |                                        |
+============+=================+========================================+
| ``GET``    | /api/contents   | Return a model for the base directory. |
|            |                 | See /api/contents/<path>/<file>.       |
+------------+-----------------+----------------------------------------+
| ``GET``    | /api/contents/  | Return a model for the given file in   |
|            | <file>          | the base directory. See                |
|            |                 | /api/contents/<path>/<file>.           |
+------------+-----------------+----------------------------------------+
| ``GET``    | /api/contents/  | Return a model for a file or           |
|            | <path>/<file>   | directory. A directory model contains  |
|            |                 | a list of models (without content) of  |
|            |                 | the files and directories it contains. |
+------------+-----------------+----------------------------------------+
| ``PUT``    | /api/contents/  | Saves the file in the location         |
|            | <path>/<file>   | specified by name and path. PUT is     |
|            |                 | very similar to POST, but the          |
|            |                 | requester specifies the name, where as |
|            |                 | with POST, the server picks the name.  |
|            |                 | PUT /api/contents/path/Name.ipynb Save |
|            |                 | notebook at ``path/Name.ipynb``.       |
|            |                 | Notebook structure is specified in     |
|            |                 | ``content`` key of JSON request body.  |
|            |                 | If content is not specified, create a  |
|            |                 | new empty notebook.                    |
|            |                 | PUT /api/contents/path/Name.ipynb with |
|            |                 | JSON body                              |
|            |                 | {"copy\_from" : "[path/to/]            |
|            |                 | OtherNotebook.ipynb"} Copy             |
|            |                 | OtherNotebook to Name                  |
+------------+-----------------+----------------------------------------+
| ``PATCH``  | /api/contents/  | Renames a notebook without             |
|            | <path>/<file>   | re-uploading content.                  |
+------------+-----------------+----------------------------------------+
| ``POST``   | /api/contents/  | Creates a new file or directory in the |
|            | <path>/<file>   | specified path. POST creates new files |
|            |                 | or directories. The server always      |
|            |                 | decides on the name.                   |
|            |                 | POST /api/contents/path New untitled   |
|            |                 | notebook in path. If content           |
|            |                 | specified, upload a notebook,          |
|            |                 | otherwise start empty.                 |
|            |                 | POST /api/contents/path with body      |
|            |                 | {"copy\_from":"OtherNotebook.ipynb"}   |
|            |                 | New copy of OtherNotebook in path      |
+------------+-----------------+----------------------------------------+
| ``DELETE`` | /api/contents/  | delete a file in the given path.       |
|            | <path>/<file>   |                                        |
+------------+-----------------+----------------------------------------+
| ``GET``    | /api/contents/  | get lists checkpoint for a file.       |
|            | <path>/<file>   |                                        |
|            | /checkpoints    |                                        |
+------------+-----------------+----------------------------------------+
| ``POST``   | /api/contents/  | post creates a new checkpoint.         |
|            | <path>/<file>   |                                        |
|            | /checkpoints    |                                        |
+------------+-----------------+----------------------------------------+
| ``POST``   | /api/contents/  | post restores a file from a            |
|            | <path>/<file>   | checkpoint.                            |
|            | /checkpoints/   |                                        |
|            | <checkpoint\_   |                                        |
|            | id>             |                                        |
+------------+-----------------+----------------------------------------+
| ``DELETE`` | /api/contents/  | delete clears a checkpoint for a       |
|            | <path>/<file>   | given file.                            |
|            | /checkpoints/   |                                        |
|            | <checkpoint\_   |                                        |
|            | id>             |                                        |
+------------+-----------------+----------------------------------------+

Kernel API

+------------+-----------------+----------------------------------------+
| HTTP       | URI             | Action                                 |
| verb       |                 |                                        |
+============+=================+========================================+
| ``GET``    | /api/kernels    | Return a model of all kernels.         |
+------------+-----------------+----------------------------------------+
| ``GET``    | /api/kernels    | Return a model of kernel with given    |
|            | /<kernel\_id>   | kernel id.                             |
+------------+-----------------+----------------------------------------+
| ``POST``   | /api/kernels    | Start a new kernel with default or     |
|            |                 | given name.                            |
+------------+-----------------+----------------------------------------+
| ``DELETE`` | /api/kernels    | Shutdown the given kernel.             |
|            | /<kernel\_id>   |                                        |
+------------+-----------------+----------------------------------------+
| ``POST``   | /api/kernels    | Perform action on kernel with given    |
|            | /<kernel\_id>   | kernel id. Actions can be              |
|            | /<action>       | "interrupt" or "restart".              |
+------------+-----------------+----------------------------------------+
| ``WS``     | /api/kernels    | Websocket stream                       |
|            | /<kernel\_id>   |                                        |
|            | /channels       |                                        |
+------------+-----------------+----------------------------------------+
| ``GET``    | /api/kernel     | Return a spec model of all available   |
|            | specs           | kernels.                               |
+------------+-----------------+----------------------------------------+
| ``GET``    | /api/kernel     | Return a spec model of all available   |
|            | specs/          | kernels with a given kernel name.      |
|            | <kernel\_name>  |                                        |
+------------+-----------------+----------------------------------------+

Sessions API

+------------+-----------------+----------------------------------------+
| HTTP       | URL             | Action                                 |
| verb       |                 |                                        |
+============+=================+========================================+
| ``GET``    | /api/sesions    | Return model of active sessions.       |
+------------+-----------------+----------------------------------------+
| ``POST``   | /api/sessions   | If session does not already exist,     |
|            |                 | create a new session with given        |
|            |                 | notebook name and path and given       |
|            |                 | kernel name. Return active sesssion.   |
+------------+-----------------+----------------------------------------+
| ``GET``    | /api/sessions   | Return model of active session with    |
|            | /<session\_id>  | given session id.                      |
+------------+-----------------+----------------------------------------+
| ``PATCH``  | /api/sessions   | Return model of active session with    |
|            | /<session\_id>  | notebook name or path of session with  |
|            |                 | given session id.                      |
+------------+-----------------+----------------------------------------+
| ``DELETE`` | /api/sessions   | Delete model of active session with    |
|            | /<session\_id>  | given session id.                      |
+------------+-----------------+----------------------------------------+

Clusters API

+------------+-----------------+----------------------------------------+
| HTTP       | URL             | Action                                 |
| verb       |                 |                                        |
+============+=================+========================================+
| ``GET``    | /api/clusters   | Return model of clusters.              |
+------------+-----------------+----------------------------------------+
| ``GET``    | /api/clusters   | Return model of given cluster.         |
|            | <cluster\_id>   |                                        |
+------------+-----------------+----------------------------------------+
| ``POST``   | /api/clusters   | Perform action with given clusters.    |
|            | <cluster\_id>   | Valid actions are "start" and "stop"   |
|            | <action>        |                                        |
+------------+-----------------+----------------------------------------+

Old Architecture
----------------

This chart shows the web-services in the single directory IPython
notebook.

+------------+-----------------+----------------------------------------+
| HTTP       | URL             | Action                                 |
| verb       |                 |                                        |
+============+=================+========================================+
| ``GET``    | /notebooks      | return list of dicts with each         |
|            |                 | notebook's info                        |
+------------+-----------------+----------------------------------------+
| ``POST``   | /notebooks      | if sending a body, saving that body as |
|            |                 | a new notebook; if no body, create a   |
|            |                 | a new notebook.                        |
+------------+-----------------+----------------------------------------+
| ``GET``    | /notebooks      | get JSON data for notebook             |
|            | /<notebook\_id> |                                        |
+------------+-----------------+----------------------------------------+
| ``PUT``    | /notebooks      | saves an existing notebook with body   |
|            | /<notebook\_id> | data                                   |
+------------+-----------------+----------------------------------------+
| ``DELETE`` | /notebooks      | deletes the notebook with the given ID |
|            | /<notebook\_id> |                                        |
+------------+-----------------+----------------------------------------+

This chart shows the architecture for the IPython notebook website.

+------------+-----------------+----------------------------------------+
| HTTP       | URL             | Action                                 |
| verb       |                 |                                        |
+============+=================+========================================+
| ``GET``    | /               | navigates user to dashboard of         |
|            |                 | notebooks and clusters.                |
+------------+-----------------+----------------------------------------+
| ``GET``    | /<notebook\_id> | go to wepage for that notebook         |
+------------+-----------------+----------------------------------------+
| ``GET``    | /new            | creates a new notebook with profile    |
|            |                 | (or default, if no profile exists)     |
|            |                 | setings                                |
+------------+-----------------+----------------------------------------+
| ``GET``    | /<notebook\_id> | opens a duplicate copy or the notebook |
|            | /copy           | with the given ID in a a new tab       |
+------------+-----------------+----------------------------------------+
| ``GET``    | /<notebook\_id> | prints the notebook with the given ID; |
|            | /print          | if notebook doesn't exist, displays    |
|            |                 | error message                          |
+------------+-----------------+----------------------------------------+
| ``GET``    | /login          | navigates to login page; if no user    |
|            |                 | profile is defined, it navigates user  |
|            |                 | to dashboard                           |
+------------+-----------------+----------------------------------------+
| ``GET``    | /logout         | logs out of current profile, and       |
|            |                 | navigates user to login page           |
+------------+-----------------+----------------------------------------+

This chart shows the Web services that act on the kernels and clusters.

+------------+-----------------+----------------------------------------+
| HTTP       | URL             | Action                                 |
| verb       |                 |                                        |
+============+=================+========================================+
| ``GET``    | /kernels        | return the list of kernel IDs          |
|            |                 | currently running                      |
+------------+-----------------+----------------------------------------+
| ``GET``    | /kernels        | ---                                    |
|            | /<kernel\_id>   |                                        |
+------------+-----------------+----------------------------------------+
| ``GET``    | /kernels        | performs action (restart/kill) kernel  |
|            | /<kernel\_id>   | with given ID                          |
|            | <action>        |                                        |
+------------+-----------------+----------------------------------------+
| ``GET``    | /kernels        | ---                                    |
|            | /<kernel\_id>   |                                        |
|            | /iopub          |                                        |
+------------+-----------------+----------------------------------------+
| ``GET``    | /kernels        | ---                                    |
|            | /<kernel\_id>   |                                        |
|            | /shell          |                                        |
+------------+-----------------+----------------------------------------+
| ``GET``    | /rstservice/    | ---                                    |
|            | render          |                                        |
+------------+-----------------+----------------------------------------+
| ``GET``    | /files/(.\*)    | ---                                    |
+------------+-----------------+----------------------------------------+
| ``GET``    | /clusters       | returns a list of dicts with each      |
|            |                 | cluster's information                  |
+------------+-----------------+----------------------------------------+
| ``POST``   | /clusters       | performs action (start/stop) on        |
|            | /<profile\_id>  | cluster with given profile ID          |
|            | /<cluster\_     |                                        |
|            | action>         |                                        |
+------------+-----------------+----------------------------------------+
| ``GET``    | /clusters       | returns the JSON data for cluster with |
|            | /<profile\_id>  | given profile ID                       |
+------------+-----------------+----------------------------------------+
