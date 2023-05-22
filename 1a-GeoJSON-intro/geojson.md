#### GeoJSON

#### TL;DR

- GeoJSON uses dictionaries and lists as in json
- counties and states are either Vector or Multi-Vector types
- even a vector may have multiple "rings"
- hence all vectors are surrounded by *double* brackets
- some GeoJSON (Puerto Rico) has non-UTF-8 encoding
- drawing properly requires projection

wikipedia has a nice [discussion](https://en.wikipedia.org/wiki/GeoJSON).

I obtained GeoJSON data for the US from 

- plotly ([here](https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json)), 
- and from this [page](https://eric.clst.org/tech/usgeojson/) on the web


#### Intro

GeoJSON is a JSON-type formatting for geographical data.  The geojson.org [page](https://geojson.org) has this example:

```
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [125.6, 10.1]
  },
  "properties": {
    "name": "Dinagat Islands"
  }
}
```

A <i>feature</i> is a dictionary with keys:

- type
- geometry
- properties

And geometry is a dictionary with keys:

- type
- coordinates

where coordinates is an array or list (that may be nested, as we'll see).

The types of geometry are

- Point
- LineString
- Polygon
- MultiPoint
- MultiLineString
- MultiPolygon

Polygons and multi-polygons consist of points in some arrangement.  These points are tuples of longitude, latitude.

The [spec](https://datatracker.ietf.org/doc/html/rfc7946#page-9) says that a polygon consists of a "linear ring", which "is a closed LineString with four or more positions."  The positions are to be specified in order, with the first and last being exact duplicates.

A linear ring is "the boundary of a surface or the boundary of a hole in a surface".  Its component positions should follow the right-hand rule (counter-clockwise), but this is not enforced, for backward compatibility.

####  brackets

The coordinates that define a polygon are given as an
array of tuples

```
[longitude, latitude]
```

so that'd would be something like

```
[[long,lat],[long,lat] ... [long,lat]]
```

However, the definition of a polygon actually has an extra set of brackets.  

```
[
 [[long,lat],[long,lat] ... [long,lat]]
]
```

Apparently, this is because polygons are allowed to have holes.  I don't know of examples yet in the state and county data.

#### multi-polygons

For a multi-polygon, the first polygon is the exterior ring of positions, and the ones that follow are interior.  However, the wiki article (below) has a different take on this.  I'll have to read the spec more carefully to be sure.

Because of the right-hand rule, interior polygons go clockwise.

#### U.S. states

In the GeoJSON data that I've seen, most U.S. states are represented as polygons, though a few are multi-polygons.

Alaska, California, .. are given as multi-polygons.  These include interior polygons which I believe are lakes.  At the scale of the data, the lakes in most states don't show up.

A multipolygon is

```
[
 [
  [[long,lat],[long,lat] ... [long,lat]]
 ]
]
```

which is consistent.

The [wikipedia](https://en.wikipedia.org/wiki/GeoJSON#Geometries) entry explains a bit.  In particular, the components of multi-polygons do not have to be inside a single boundary.

So it seems that a lake should be a second linear ring in a polygon feature.