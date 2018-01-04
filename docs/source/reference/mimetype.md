# Custom mimetypes (MIME types)


## What's a mimetype?

When an internet request and response occurs, a `Content-Type` header is
passed. A mimetype, also referred to as MIME type, identifies how the content
that is being returned should be handled or used, based on type, by the
application and browser. A MIME type is made up of a MIME *group* (i.e.
application, image, audio, etc.) and a MIME *subtype*. For example, a MIME
type is `image/png` where MIME *group* is `image` and *subtype* is `png`.

As types may contain vendor specific items, a
[custom vendor specific MIME type](https://en.wikipedia.org/wiki/Media_type#Vendor_tree),
`vnd`, can be used. A vendor specific MIME type will contain `vnd` such as
`application/vnd.jupyter.cells`.


## Custom mimetypes used in Jupyter and IPython projects

- `application/vnd.jupyter`
- `application/vnd.jupyter.cells`
- `application/vnd.jupyter.dragindex` used by nbdime
- `application/x-ipynb+json` for notebooks
- `text/html`
     * metadata:
         - `isolated: boolean` -- HTML should be rendered inside an `<iframe>`.

##  Listing of custom mimetypes used for display

* `application/vnd.geo+json` - [GeoJSON spec](http://geojson.org/geojson-spec.html)
  `application/vnd.geo+json` is now deprecated and replaced by
  `application/geo+json`
* `application/geo+json` - preferred [GeoJSON spec](http://geojson.org/geojson-spec.html)
* `application/vnd.plotly.v1+json` - [Plotly JSON Schema](http://help.plot.ly/json-chart-schema/)
* `application/vdom.v1+json` - [Virtual DOM spec](https://github.com/nteract/vdom/blob/master/docs/spec.md)
