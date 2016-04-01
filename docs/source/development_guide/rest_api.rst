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

+--------+--------+-------+
| HTTP   | URL    | Actio |
| verb   |        | n     |
+========+========+=======+
| ``GET` | /.\*/  |
| `      | \|     |
|        | Strips |
|        | traili |
|        | ng     |
|        | slashe |
|        | s.     |
|        | \| \|  |
|        | ``GET` |
|        | `      |
|        | \|     |
|        | /api   |
|        | \|     |
|        | Return |
|        | s      |
|        | api    |
|        | versio |
|        | n      |
|        | inform |
|        | ation. |
|        | \| \|  |
|        | ``*``  |
|        | \|     |
|        | /api/n |
|        | oteboo |
|        | ks     |
|        | \|     |
|        | Deprec |
|        | ated:  |
|        | redire |
|        | ct     |
|        | to     |
|        | /api/c |
|        | ontent |
|        | s      |
|        | \| \|  |
|        | ``GET` |
|        | `      |
|        | \|     |
|        | /api/n |
|        | bconve |
|        | rt     |
|        | \| \|  |
+--------+--------+-------+

Notebook contents API.

+--------+--------+-------+
| HTTP   | URL    | Actio |
| verb   |        | n     |
+========+========+=======+
| ``GET` | /api/c | Retur |
| `      | ontent | n     |
|        | s      | a     |
|        |        | model |
|        |        | for   |
|        |        | the   |
|        |        | base  |
|        |        | direc |
|        |        | tory. |
|        |        | See   |
|        |        | /api/ |
|        |        | conte |
|        |        | nts/< |
|        |        | path> |
|        |        | /<fil |
|        |        | e>.   |
+--------+--------+-------+
| ``GET` | /api/c | Retur |
| `      | ontent | n     |
|        | s/<fil | a     |
|        | e>     | model |
|        |        | for   |
|        |        | the   |
|        |        | given |
|        |        | file  |
|        |        | in    |
|        |        | the   |
|        |        | base  |
|        |        | direc |
|        |        | tory. |
|        |        | See   |
|        |        | /api/ |
|        |        | conte |
|        |        | nts/< |
|        |        | path> |
|        |        | /<fil |
|        |        | e>.   |
+--------+--------+-------+
| ``GET` | /api/c | Retur |
| `      | ontent | n     |
|        | s/<pat | a     |
|        | h>/<fi | model |
|        | le>    | for a |
|        |        | file  |
|        |        | or    |
|        |        | direc |
|        |        | tory. |
|        |        | A     |
|        |        | direc |
|        |        | tory  |
|        |        | model |
|        |        | conta |
|        |        | ins   |
|        |        | a     |
|        |        | list  |
|        |        | of    |
|        |        | model |
|        |        | s     |
|        |        | (with |
|        |        | out   |
|        |        | conte |
|        |        | nt)   |
|        |        | of    |
|        |        | the   |
|        |        | files |
|        |        | and   |
|        |        | direc |
|        |        | torie |
|        |        | s     |
|        |        | it    |
|        |        | conta |
|        |        | ins.  |
+--------+--------+-------+
| ``PUT` | /api/c | Saves |
| `      | ontent | the   |
|        | s/<pat | file  |
|        | h>/<fi | in    |
|        | le>    | the   |
|        |        | locat |
|        |        | ion   |
|        |        | speci |
|        |        | fied  |
|        |        | by    |
|        |        | name  |
|        |        | and   |
|        |        | path. |
|        |        | PUT   |
|        |        | is    |
|        |        | very  |
|        |        | simil |
|        |        | ar    |
|        |        | to    |
|        |        | POST, |
|        |        | but   |
|        |        | the   |
|        |        | reque |
|        |        | ster  |
|        |        | speci |
|        |        | fies  |
|        |        | the   |
|        |        | name, |
|        |        | where |
|        |        | as    |
|        |        | with  |
|        |        | POST, |
|        |        | the   |
|        |        | serve |
|        |        | r     |
|        |        | picks |
|        |        | the   |
|        |        | name. |
|        |        | PUT   |
|        |        | /api/ |
|        |        | conte |
|        |        | nts/p |
|        |        | ath/N |
|        |        | ame.i |
|        |        | pynb  |
|        |        | Save  |
|        |        | noteb |
|        |        | ook   |
|        |        | at    |
|        |        | ``pat |
|        |        | h/Nam |
|        |        | e.ipy |
|        |        | nb``. |
|        |        | Noteb |
|        |        | ook   |
|        |        | struc |
|        |        | ture  |
|        |        | is    |
|        |        | speci |
|        |        | fied  |
|        |        | in    |
|        |        | ``con |
|        |        | tent` |
|        |        | `     |
|        |        | key   |
|        |        | of    |
|        |        | JSON  |
|        |        | reque |
|        |        | st    |
|        |        | body. |
|        |        | If    |
|        |        | conte |
|        |        | nt    |
|        |        | is    |
|        |        | not   |
|        |        | speci |
|        |        | fied, |
|        |        | creat |
|        |        | e     |
|        |        | a new |
|        |        | empty |
|        |        | noteb |
|        |        | ook.  |
|        |        | PUT   |
|        |        | /api/ |
|        |        | conte |
|        |        | nts/p |
|        |        | ath/N |
|        |        | ame.i |
|        |        | pynb  |
|        |        | with  |
|        |        | JSON  |
|        |        | body: |
|        |        | :{    |
|        |        | "copy |
|        |        | \_fro |
|        |        | m"    |
|        |        | :     |
|        |        | "[pat |
|        |        | h/to/ |
|        |        | ]Othe |
|        |        | rNote |
|        |        | book. |
|        |        | ipynb |
|        |        | "     |
|        |        | }     |
|        |        | Copy  |
|        |        | Other |
|        |        | Noteb |
|        |        | ook   |
|        |        | to    |
|        |        | Name  |
+--------+--------+-------+
| ``PATC | /api/c | PATCH |
| H``    | ontent | renam |
|        | s/<pat | es    |
|        | h>/<fi | a     |
|        | le>    | noteb |
|        |        | ook   |
|        |        | witho |
|        |        | ut    |
|        |        | re-up |
|        |        | loadi |
|        |        | ng    |
|        |        | conte |
|        |        | nt.   |
+--------+--------+-------+
| ``POST | /api/c | Creat |
| ``     | ontent | e     |
|        | s/<pat | a new |
|        | h>/<fi | file  |
|        | le>    | or    |
|        |        | direc |
|        |        | tory  |
|        |        | in    |
|        |        | the   |
|        |        | speci |
|        |        | fied  |
|        |        | path. |
|        |        | POST  |
|        |        | creat |
|        |        | es    |
|        |        | new   |
|        |        | files |
|        |        | or    |
|        |        | direc |
|        |        | torie |
|        |        | s.    |
|        |        | The   |
|        |        | serve |
|        |        | r     |
|        |        | alway |
|        |        | s     |
|        |        | decid |
|        |        | es    |
|        |        | on    |
|        |        | the   |
|        |        | name. |
|        |        | POST  |
|        |        | /api/ |
|        |        | conte |
|        |        | nts/p |
|        |        | ath   |
|        |        | New   |
|        |        | untit |
|        |        | led   |
|        |        | noteb |
|        |        | ook   |
|        |        | in    |
|        |        | path. |
|        |        | If    |
|        |        | conte |
|        |        | nt    |
|        |        | speci |
|        |        | fied, |
|        |        | uploa |
|        |        | d     |
|        |        | a     |
|        |        | noteb |
|        |        | ook,  |
|        |        | other |
|        |        | wise  |
|        |        | start |
|        |        | empty |
|        |        | .     |
|        |        | POST  |
|        |        | /api/ |
|        |        | conte |
|        |        | nts/p |
|        |        | ath   |
|        |        | with  |
|        |        | body  |
|        |        | {"cop |
|        |        | y\_fr |
|        |        | om"   |
|        |        | :     |
|        |        | "Othe |
|        |        | rNote |
|        |        | book. |
|        |        | ipynb |
|        |        | "}    |
|        |        | New   |
|        |        | copy  |
|        |        | of    |
|        |        | Other |
|        |        | Noteb |
|        |        | ook   |
|        |        | in    |
|        |        | path  |
+--------+--------+-------+
| ``DELE | /api/c | delet |
| TE``   | ontent | e     |
|        | s/<pat | a     |
|        | h>/<fi | file  |
|        | le>    | in    |
|        |        | the   |
|        |        | given |
|        |        | path  |
+--------+--------+-------+
| ``GET` | /api/c | get   |
| `      | ontent | lists |
|        | s/<pat | check |
|        | h>/<fi | point |
|        | le>/ch | s     |
|        | eckpoi | for a |
|        | nts    | file. |
+--------+--------+-------+
| ``POST | /api/c | post  |
| ``     | ontent | creat |
|        | s/<pat | es    |
|        | h>/<fi | a new |
|        | le>/ch | check |
|        | eckpoi | point |
|        | nts    | .     |
+--------+--------+-------+
| ``POST | /api/c | post  |
| ``     | ontent | resto |
|        | s/<pat | res   |
|        | h>/<fi | a     |
|        | le>/ch | file  |
|        | eckpoi | from  |
|        | nts/<c | a     |
|        | heckpo | check |
|        | int\_i | point |
|        | d>     | .     |
+--------+--------+-------+
| ``DELE | /api/c | delet |
| TE``   | ontent | e     |
|        | s/<pat | clear |
|        | h>/<fi | s     |
|        | le>/ch | a     |
|        | eckpoi | check |
|        | nts/<c | point |
|        | heckpo | for a |
|        | int\_i | given |
|        | d>     | file. |
+--------+--------+-------+

Kernel API

+--------+--------+-------+
| HTTP   | URI    | Actio |
| verb   |        | n     |
+========+========+=======+
| ``GET` | /api/k | Retur |
| `      | ernels | n     |
|        |        | a     |
|        |        | model |
|        |        | of    |
|        |        | all   |
|        |        | kerne |
|        |        | ls.   |
+--------+--------+-------+
| ``GET` | /api/k | Retur |
| `      | ernels | n     |
|        | /<kern | a     |
|        | el\_id | model |
|        | >      | of    |
|        |        | kerne |
|        |        | l     |
|        |        | with  |
|        |        | given |
|        |        | kerne |
|        |        | l     |
|        |        | id.   |
+--------+--------+-------+
| ``POST | /api/k | Start |
| ``     | ernels | a new |
|        |        | kerne |
|        |        | l     |
|        |        | with  |
|        |        | defau |
|        |        | lt    |
|        |        | or    |
|        |        | given |
|        |        | name. |
+--------+--------+-------+
| ``DELE | /api/k | Shutd |
| TE``   | ernels | own   |
|        | /<kern | the   |
|        | el\_id | given |
|        | >      | kerne |
|        |        | l.    |
+--------+--------+-------+
| ``POST | /api/k | Perfo |
| ``     | ernels | rm    |
|        | /<kern | actio |
|        | el\_id | n     |
|        | >/<act | on    |
|        | ion>   | kerne |
|        |        | l     |
|        |        | with  |
|        |        | given |
|        |        | kerne |
|        |        | l     |
|        |        | id.   |
|        |        | Actio |
|        |        | ns    |
|        |        | can   |
|        |        | be    |
|        |        | "inte |
|        |        | rrupt |
|        |        | "     |
|        |        | or    |
|        |        | "rest |
|        |        | art". |
+--------+--------+-------+
| ``WS`` | /api/k | Webso |
|        | ernels | cket  |
|        | /<kern | strea |
|        | el\_id | m     |
|        | >/chan |       |
|        | nels   |       |
+--------+--------+-------+
| ``GET` | /api/k | Retur |
| `      | ernels | n     |
|        | pecs   | a     |
|        |        | spec  |
|        |        | model |
|        |        | of    |
|        |        | all   |
|        |        | avail |
|        |        | able  |
|        |        | kerne |
|        |        | ls.   |
+--------+--------+-------+
| ``GET` | /api/k | Retur |
| `      | ernels | n     |
|        | pecs/< | a     |
|        | kernel | spec  |
|        | \_name | model |
|        | >      | of    |
|        |        | avail |
|        |        | able  |
|        |        | kerne |
|        |        | ls    |
|        |        | with  |
|        |        | given |
|        |        | kerne |
|        |        | l     |
|        |        | name. |
+--------+--------+-------+

Sessions API

+--------+--------+-------+
| HTTP   | URL    | Actio |
| verb   |        | n     |
+========+========+=======+
| ``GET` | /api/s | Retur |
| `      | ession | n     |
|        | s      | model |
|        |        | of    |
|        |        | activ |
|        |        | e     |
|        |        | sessi |
|        |        | ons.  |
+--------+--------+-------+
| ``POST | /api/s | If    |
| ``     | ession | sessi |
|        | s      | on    |
|        |        | does  |
|        |        | not   |
|        |        | alrea |
|        |        | dy    |
|        |        | exist |
|        |        | ,     |
|        |        | creat |
|        |        | e     |
|        |        | a new |
|        |        | sessi |
|        |        | on    |
|        |        | with  |
|        |        | given |
|        |        | noteb |
|        |        | ook   |
|        |        | name  |
|        |        | and   |
|        |        | path  |
|        |        | and   |
|        |        | given |
|        |        | kerne |
|        |        | l     |
|        |        | name. |
|        |        | Retur |
|        |        | n     |
|        |        | activ |
|        |        | e     |
|        |        | sessi |
|        |        | on.   |
+--------+--------+-------+
| ``GET` | /api/s | Retur |
| `      | ession | n     |
|        | s/<ses | model |
|        | sion\_ | of    |
|        | id>    | activ |
|        |        | e     |
|        |        | sessi |
|        |        | on    |
|        |        | with  |
|        |        | given |
|        |        | sessi |
|        |        | on    |
|        |        | id.   |
+--------+--------+-------+
| ``PATC | /api/s | Chang |
| H``    | ession | e     |
|        | s/<ses | noteb |
|        | sion\_ | ook   |
|        | id>    | name  |
|        |        | or    |
|        |        | path  |
|        |        | of    |
|        |        | sessi |
|        |        | on    |
|        |        | with  |
|        |        | given |
|        |        | sessi |
|        |        | on    |
|        |        | id.   |
+--------+--------+-------+
| ``DELE | /api/s | Delet |
| TE``   | ession | e     |
|        | s/<ses | activ |
|        | sion\_ | e     |
|        | id>    | sessi |
|        |        | on    |
|        |        | with  |
|        |        | given |
|        |        | sessi |
|        |        | on    |
|        |        | id.   |
+--------+--------+-------+

Clusters API

+--------+--------+-------+
| HTTP   | URL    | Actio |
| verb   |        | n     |
+========+========+=======+
| ``GET` | /api/c | Retur |
| `      | luster | n     |
|        | s      | model |
|        |        | of    |
|        |        | clust |
|        |        | ers.  |
+--------+--------+-------+
| ``GET` | /api/c | Retur |
| `      | luster | n     |
|        | s/<clu | model |
|        | ster\_ | of    |
|        | id>    | given |
|        |        | clust |
|        |        | er.   |
+--------+--------+-------+
| ``POST | /api/c | Perfo |
| ``     | luster | rm    |
|        | s/<clu | actio |
|        | ster\_ | n     |
|        | id>/<a | with  |
|        | ction> | given |
|        |        | clust |
|        |        | ers.  |
|        |        | Valid |
|        |        | actio |
|        |        | ns    |
|        |        | are   |
|        |        | "star |
|        |        | t"    |
|        |        | or    |
|        |        | "stop |
|        |        | "     |
+--------+--------+-------+

Old Architecture
----------------

This chart shows the web-services in the single directory IPython
notebook.

+--------+--------+-------+
| HTTP   | URL    | Actio |
| verb   |        | n     |
+========+========+=======+
| ``GET` | /noteb | retur |
| `      | ooks   | ns    |
|        |        | list  |
|        |        | of    |
|        |        | dicts |
|        |        | with  |
|        |        | each  |
|        |        | noteb |
|        |        | ook's |
|        |        | info  |
+--------+--------+-------+
| ``POST | /noteb | if    |
| ``     | ooks   | sendi |
|        |        | ng    |
|        |        | a     |
|        |        | body, |
|        |        | savin |
|        |        | g     |
|        |        | that  |
|        |        | body  |
|        |        | as a  |
|        |        | new   |
|        |        | noteb |
|        |        | ook;  |
|        |        | if no |
|        |        | body, |
|        |        | creat |
|        |        | e     |
|        |        | a new |
|        |        | noteb |
|        |        | ooks  |
+--------+--------+-------+
| ``GET` | /noteb | get   |
| `      | ooks/< | JSON  |
|        | notebo | data  |
|        | ok\_id | for   |
|        | >      | noteb |
|        |        | ook   |
+--------+--------+-------+
| ``PUT` | /noteb | saves |
| `      | ooks/< | an    |
|        | notebo | exist |
|        | ok\_id | ing   |
|        | >      | noteb |
|        |        | ook   |
|        |        | with  |
|        |        | body  |
|        |        | data  |
+--------+--------+-------+
| ``DELE | /noteb | delet |
| TE``   | ooks/< | es    |
|        | notebo | the   |
|        | ok\_id | noteb |
|        | >      | ook   |
|        |        | with  |
|        |        | the   |
|        |        | given |
|        |        | ID    |
+--------+--------+-------+

This chart shows the architecture for the IPython notebook website.

+--------+--------+-------+
| HTTP   | URI    | Actio |
| verb   |        | n     |
+========+========+=======+
| ``GET` | /      | navig |
| `      |        | ates  |
|        |        | user  |
|        |        | to    |
|        |        | dashb |
|        |        | oard  |
|        |        | of    |
|        |        | noteb |
|        |        | ooks  |
|        |        | and   |
|        |        | clust |
|        |        | ers   |
+--------+--------+-------+
| ``GET` | /<note | go to |
| `      | book\_ | webpa |
|        | id>    | ge    |
|        |        | for   |
|        |        | that  |
|        |        | noteb |
|        |        | ook   |
+--------+--------+-------+
| ``GET` | /new   | creat |
| `      |        | es    |
|        |        | a new |
|        |        | noteb |
|        |        | ook   |
|        |        | with  |
|        |        | profi |
|        |        | le    |
|        |        | (or   |
|        |        | defau |
|        |        | lt,   |
|        |        | if no |
|        |        | profi |
|        |        | le    |
|        |        | exist |
|        |        | s)    |
|        |        | setti |
|        |        | ngs   |
+--------+--------+-------+
| ``GET` | /<note | opens |
| `      | book\_ | a     |
|        | id>/co | dupli |
|        | py     | cate  |
|        |        | copy  |
|        |        | of    |
|        |        | the   |
|        |        | noteb |
|        |        | ook   |
|        |        | with  |
|        |        | the   |
|        |        | given |
|        |        | ID in |
|        |        | a new |
|        |        | tab   |
+--------+--------+-------+
| ``GET` | /<note | print |
| `      | book\_ | s     |
|        | id>/pr | the   |
|        | int    | noteb |
|        |        | ook   |
|        |        | with  |
|        |        | the   |
|        |        | given |
|        |        | ID;   |
|        |        | if    |
|        |        | noteb |
|        |        | ook   |
|        |        | ID    |
|        |        | doesn |
|        |        | 't    |
|        |        | exist |
|        |        | ,     |
|        |        | displ |
|        |        | ays   |
|        |        | error |
|        |        | messa |
|        |        | ge    |
+--------+--------+-------+
| ``GET` | /login | navig |
| `      |        | ates  |
|        |        | to    |
|        |        | login |
|        |        | page; |
|        |        | if no |
|        |        | user  |
|        |        | profi |
|        |        | le    |
|        |        | is    |
|        |        | defin |
|        |        | ed,   |
|        |        | it    |
|        |        | navig |
|        |        | ates  |
|        |        | user  |
|        |        | to    |
|        |        | dashb |
|        |        | oard  |
+--------+--------+-------+
| ``GET` | /logou | logs  |
| `      | t      | out   |
|        |        | of    |
|        |        | curre |
|        |        | nt    |
|        |        | profi |
|        |        | le,   |
|        |        | and   |
|        |        | navig |
|        |        | ates  |
|        |        | user  |
|        |        | to    |
|        |        | login |
|        |        | page  |
+--------+--------+-------+

This chart shows the Web services that act on the kernels and clusters.

+--------+--------+-------+
| HTTP   | URL    | Actio |
| verb   |        | n     |
+========+========+=======+
| ``GET` | /kerne | retur |
| `      | ls     | n     |
|        |        | the   |
|        |        | list  |
|        |        | of    |
|        |        | kerne |
|        |        | l     |
|        |        | ID's  |
|        |        | curre |
|        |        | ntly  |
|        |        | runni |
|        |        | ng    |
+--------+--------+-------+
| ``GET` | /kerne | ---   |
| `      | ls/<ke |       |
|        | rnel\_ |       |
|        | id>    |       |
+--------+--------+-------+
| ``GET` | /kerne | perfo |
| `      | ls/<ke | rms   |
|        | rnel\_ | actio |
|        | id>/<k | n     |
|        | ernel\ | (rest |
|        | _actio | art/k |
|        | n>     | ill)  |
|        |        | kerne |
|        |        | l     |
|        |        | with  |
|        |        | given |
|        |        | ID    |
+--------+--------+-------+
| ``GET` | /kerne | ---   |
| `      | ls/<ke |       |
|        | rnel\_ |       |
|        | id>/io |       |
|        | pub    |       |
+--------+--------+-------+
| ``GET` | /kerne | ---   |
| `      | ls/<ke |       |
|        | rnel\_ |       |
|        | id>/sh |       |
|        | ell    |       |
+--------+--------+-------+
| ``GET` | /rstse | ---   |
| `      | rvice/ |       |
|        | render |       |
+--------+--------+-------+
| ``GET` | /files |
| `      | /(.\*) |
|        | \| --- |
|        | \| \|  |
|        | ``GET` |
|        | `      |
|        | \|     |
|        | /clust |
|        | ers    |
|        | \|     |
|        | return |
|        | s      |
|        | a list |
|        | of     |
|        | dicts  |
|        | with   |
|        | each   |
|        | cluste |
|        | r's    |
|        | inform |
|        | ation  |
|        | \| \|  |
|        | ``POST |
|        | ``     |
|        | \|     |
|        | /clust |
|        | ers/<p |
|        | rofile |
|        | \_id>/ |
|        | <clust |
|        | er\_ac |
|        | tion>  |
|        | \|     |
|        | perfor |
|        | ms     |
|        | action |
|        | (start |
|        | /stop) |
|        | on     |
|        | cluste |
|        | r      |
|        | with   |
|        | given  |
|        | profil |
|        | e      |
|        | ID \|  |
|        | \|     |
|        | ``GET` |
|        | `      |
|        | \|     |
|        | /clust |
|        | ers/<p |
|        | rofile |
|        | \_id>  |
|        | \|     |
|        | return |
|        | s      |
|        | the    |
|        | JSON   |
|        | data   |
|        | for    |
|        | cluste |
|        | r      |
|        | with   |
|        | given  |
|        | profil |
|        | e      |
|        | ID \|  |
+--------+--------+-------+
