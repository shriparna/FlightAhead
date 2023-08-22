function getPrediction() {

console.log("Here");
let s = document.getElementById("originselect");

let origin = s.options[s.selectedIndex].value;

let d = document.getElementById("destselect");
let dest = d.options[d.selectedIndex].value;

let a = document.getElementById("airlineselect");
let airline = a.options[a.selectedIndex].value;

let t = document.getElementById("timeofdayselect");
let timeofday = t.options[t.selectedIndex].value;

let w = document.getElementById("weekdayselect");
let weekday = w.options[w.selectedIndex].value;

let se = document.getElementById("seasonselect");
let season = se.options[se.selectedIndex].value;

let p = document.getElementById("prediction");
let mapviz = document.getElementById("viz1692485047630");

queryURL = "/api/v1.0/flightPredict/"+timeofday+"/"+weekday+"/"+season+"/"+airline+"/"+origin+"/"+dest;


d3.json(queryURL).then(function (data) {
     console.log(data['flt_delay'],data['probability'])
     let pred = data['flt_delay']
     let prob = data['probability']
     if (pred == "on time") {
        p.innerHTML="<span class='color-blue'><b>There is a "+(prob*100).toFixed(2) +"% probability of your flight being " + pred + "</b></span>" ;
     }
     else {
     p.innerHTML="<span class='color-red'><b>There is a "+(prob*100).toFixed(2) +"% probability of your flight being " + pred + "</b>" ;
     }
 });

console.log("Done!");

}

