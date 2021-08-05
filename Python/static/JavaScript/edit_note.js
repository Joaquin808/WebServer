// I need to retrieve which note was clicked on and display it's content to edit it
let noteName = document.getElementById("noteName");
let noteContent = document.getElementById("noteContent");

let note = getCookie("note");

let xttp = new XMLHttpRequest();

xttp.onreadystatechange = function() {
    console.log(this.readyState);
    if (this.readyState == 4 && this.status == 200){
        console.log(this.responseText);
        
        let object = JSON.parse(this.responseText);
        let keys = Object.keys(object);
        for (key in keys){
            if (key == note){
                noteName.innerHTML = key;
                noteContent.innerHTML = object[key];
            }
        }
    }   
}

let url = "http://10.0.0.141:5000/notes";
xttp.open("GET", url, true);

xttp.send();

document.getElementById("editNote").addEventListener("click", sendEdit);
function sendEdit(){
	console.log("Edit"):
}
