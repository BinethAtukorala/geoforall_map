window.onload = function () {
    var basemap = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
	});

    $.getJSON("../data/data.geojson", function(data) {

    var geojson = L.geoJson(data, {

        pointToLayer: function (feature, latlng) {
            var smallIcon = L.icon({
                               iconSize: [30, 30],
                               iconAnchor: [13, 27],
                               popupAnchor:  [1, -24],
                               iconUrl: '../data/logo.png'
                       });
     
              return L.marker(latlng, {icon: smallIcon});
             },

      onEachFeature: function (feature, layer) {
        layer.bindPopup('<a href="' + feature.properties.url + '"><b>' + feature.properties.Laboratory + '</b></a>');
      }
    });


    var map = L.map('my-map')
    .setView([-5, 30], 1);

    basemap.addTo(map);
    geojson.addTo(map);
  });

};