let xttp = new XMLHttpRequest();

let allNotes = {};
xttp.onreadystatechange = function() {
	console.log(this.readyState);
	if (this.readyState == 4 && this.status == 200){
		console.log(this.responseText);
		allNotes = JSON.parse(this.responseText);
		let noteView = document.getElementById("noteView");
		let keys = Object.keys(allNotes);
		for (key in allNotes){
			console.log(key);
			console.log(allNotes[key]);
			noteView.innerHTML += 
			` 
			<button onclick='viewNote("${key}")'> ${key} </button>
			`;
		}
	}
};

let url = "http://10.0.0.141:5000/notes";
xttp.open("GET", url, true);

xttp.send();

// This function will display all of the contents within that specified note
function viewNote(noteName){
	console.log(noteName);
	document.getElementById("noteDisplay").innerHTML = allNotes[noteName];
	document.cookie = "note=" + noteName + "; expires=" + goodExpirationDate;
}

//document.getElementById("createButton").addEventListener("click", NewNote);
function NewNote(){
	window.location.href = "http://10.0.0.141:5000/newNote";
}
