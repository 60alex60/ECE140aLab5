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

function sendFlightPlan(){
    commandList = document.getElementById("flightplanBox").value;
    commandList = commandList.replaceAll("\n",",")
    var dataURL = "http://localhost:8000/flight_plan";

   // const commands = {commandJson: commandList}
    console.log((commandList));

    fetch(dataURL, {
    method: 'POST', 
    body: commandList
    })
    .then(response => response.json())
    .then(data => {
    console.log('Success:', data);
    })
    .catch((error) => {
    console.error('Error:', error);
    });


}




