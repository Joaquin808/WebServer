let xttp = new XMLHttpRequest();

xttp.onreadystatechange = function() {
	console.log(this.readyState);
	if (this.readyState == 4 && this.status == 200){
		console.log(this.responseText);
	}
};

let url = "http://10.0.0.141:5000/notes";
xttp.open("GET", url, true);

xttp.send();
