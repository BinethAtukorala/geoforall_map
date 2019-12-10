window.onload = function () {
    var basemap = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
	});

    $.getJSON("../data/data.geojson", function(data) {

    var geojson = L.geoJson(data, {
      onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.Organisation + '<p><b>Application recieved/announced: ' + feature.properties.Application) +'</b></p?';
      }
    });


    var map = L.map('Geo-for-All-members')
    .setView([45, 14], 5);

    basemap.addTo(map);
    geojson.addTo(map);
  });

};