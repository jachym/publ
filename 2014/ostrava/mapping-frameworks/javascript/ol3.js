goog.require('ol.Map');
goog.require('ol.layer.Vector');
goog.require('ol.parser.GeoJSON');

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

var parser = new ol.parser.GeoJSON();
var features = parser.myread(/** @type {GeoJSONObject} */ (window['geojson']));
var style = new ol.style.Style({
  symbolizers: [
    new ol.style.Icon({
      url: 'http://dev.openlayers.org/releases/OpenLayers-2.13.1/img/marker.png',
      yOffset: -22
    })
  ]
});
var vlayer = new ol.layer.Vector({
    //style: style,
    source: new ol.source.Vector()
});
vlayer.getSource().addFeatures(features);

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
