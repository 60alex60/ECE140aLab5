// Add javascript here







var dataURL = "http://localhost:8000/drone_command/";
    
function sendCommand(command){
    var newDataURL = dataURL + command + "/";
    newDataURL += document.getElementById("inputField").value;
    fetchFunction(newDataURL);
}

function sendNoValCommand(command){
    var newDataURL = dataURL + command + "/";
    fetchFunction(newDataURL);
}


function showError(err) {
    console.log(err);
}


function fetchFunction(newDataURL) {
    fetch(newDataURL)
        .then(data => console.log(data))
        .catch(showError)
}

function displayFlightPlanBox(){
    if(document.getElementById("flightCheckBox").checked == true){
        document.getElementById("flightplanBox").style.display='block';
        document.getElementById("flightplanButton").style.display='block';}
    else{
        document.getElementById("flightplanBox").style.display='none';
        document.getElementById("flightplanButton").style.display='none';}
        
}




