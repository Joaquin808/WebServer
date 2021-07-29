document.getElementById("sendNote").addEventListener("click", sendNote);

// This will send the note to the storage device in the raspberry pi when the user
// is done writing their note
function sendNote(){	
	let noteName = document.getElementById("noteName").value;
	let noteContent = document.getElementById("noteContent").value;

	let xttp = new XMLHttpRequest();

	xttp.onreadystatechange = function() {
		console.log(this.readyState);
		if (this.readyState == 4 && this.status == 200){
			console.log(this.responseText);
		}
	}

	let url = "http://10.0.0.141:5000/note";
	xttp.open("POST", url, true);
	xttp.setRequestHeader("Content-Type", "application/json");

	let noteObject = {"url": "", "noteName": noteName, "noteContent": noteContent};
	console.log(noteObject);
	xttp.send(JSON.stringify(noteObject));
}
