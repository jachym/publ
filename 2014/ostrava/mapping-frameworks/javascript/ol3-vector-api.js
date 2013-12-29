goog.require('ol.Map');
goog.require('ol.layer.Vector');
goog.require('ol.source.GeoJSON');

var map;
map = new ol.Map({
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM()
        })
    ],
    renderers: ol.RendererHints.createFromQueryData(),
    target: 'map',
    view: new ol.View2D({
        center: [1612500, 6312500],
        zoom: 10
    })
});

var style = new ol.style.Style({
  symbolizers: [
    new ol.style.Icon({
      url: 'http://dev.openlayers.org/releases/OpenLayers-2.13.1/img/marker.png',
      yOffset: -22
    })
  ]
});

var image = new ol.style.Circle({
  radius: 5,
  fill: null,
  stroke: new ol.style.Stroke({color: 'red', width: 1})
});
var styles = {
  //'Point': [new ol.style.Style({
  //  image: image
  //})],
  'Point': [
    new ol.style.Style({
      image: new ol.style.Icon({
        src: 'http://dev.openlayers.org/releases/OpenLayers-2.13.1/img/marker.png'
      })
    })
  ],
  'LineString': [new ol.style.Style({
    stroke: new ol.style.Stroke({
      color: 'green',
      width: 1
    })
  })],
  'MultiLineString': [new ol.style.Style({
    stroke: new ol.style.Stroke({
      color: 'green',
      width: 1
    })
  })],
  'MultiPoint': [new ol.style.Style({
    image: image
  })],
  'MultiPolygon': [new ol.style.Style({
    stroke: new ol.style.Stroke({
      color: 'yellow',
      width: 1
    }),
    fill: new ol.style.Fill({
      color: 'rgba(255, 255, 0, 0.1)'
    })
  })],
  'Polygon': [new ol.style.Style({
    stroke: new ol.style.Stroke({
      color: 'blue',
      lineDash: [4],
      width: 3
    }),
    fill: new ol.style.Fill({
      color: 'rgba(0, 0, 255, 0.1)'
    })
  })],
  'GeometryCollection': [new ol.style.Style({
    stroke: new ol.style.Stroke({
      color: 'magenta',
      width: 2
    }),
    fill: new ol.style.Fill({
      color: 'magenta'
    }),
    image: new ol.style.Circle({
      radius: 10,
      fill: null,
      stroke: new ol.style.Stroke({
        color: 'magenta'
      })
    })
  })]
};
var styleFunction = function(feature, resolution) {
  return styles[feature.getGeometry().getType()];
};
var vlayer = new ol.layer.Vector({
  style: style,
  source: new ol.source.GeoJSON(
  {object: geojson}),
  styleFunction: styleFunction
});

var add_geojson = function() {
  map.addLayer(vlayer);
};

//add_geojson();

var bbox = [1600000, 6300000, 1625000, 6325000];
// 1600000 6300000 1650000 6350000

var pan = function() {
  map.getView().getView2D().setCenter([bbox[2], bbox[1]]);
};


goog.exportSymbol('add_geojson', add_geojson);
goog.exportSymbol('pan', pan);
