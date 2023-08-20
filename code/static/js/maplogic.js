let origin = document.getElementById("origin");
let dest = document.getElementById("dest");
let airline = document.getElementById("airline");
let timeofday = document.getElementById("timeofday");
let dayofweek = document.getElementById("weekday");
let season = document.getElementById("season");
queryURL = "localhost:5000/api/v1.0/flightPredict/"+timeoday+"/"+weekday+"/"+season+"/"+airline+"/"+origin+"/"+dest;
d3.json(queryUrl).then(function (data) {

});



