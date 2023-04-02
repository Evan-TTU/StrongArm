
var sendButton =function(buttonId){
    var xhttp = new XMLHttpRequest();

var button = document.getElementById(buttonId);
var urlCommand = window.location.href + "send/" + buttonId;

button.disabled = false;

xhttp.open("GET", urlCommand, true);
xhttp.send();
}
var stopButton =function(buttonId){
    var xhttp = new XMLHttpRequest();

var button = document.getElementById(buttonId);
var urlCommand = window.location.href + "stop/" + buttonId;

button.disabled = false;

xhttp.open("GET", urlCommand, true);
xhttp.send();
}

function mouseDown() {
    document.getElementById("btn").innerHTML;
    console.log("down")
}

function mouseUp() {
    document.getElementById("btn").innerHTML;
    console.log("up")

}

