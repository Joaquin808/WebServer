let xttp = new XMLHttpRequest();

xttp.onreadystatechange = function() {
	console.log(this.readyState);
	if (this.readyState == 4 && this.status == 200){
		console.log(this.responseText);
		let notes = JSON.parse(this.responseText);
		let noteView = document.getElementById("noteView");
		for (note in notes){
			noteView.innerHTML += 
			` 
			<button viewNote(${note.note_name})> ${note.note_name} </button>
			`;
		}
	}
};

let url = "http://10.0.0.141:5000/notes";
xttp.open("GET", url, true);

xttp.send();

document.getElementById("createButton").addEventListener("click", NewNote);
function NewNote(){
	window.location.href = "http://10.0.0.141:5000/newNote";
}
