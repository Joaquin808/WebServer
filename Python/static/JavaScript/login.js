document.getElementById("login").addEventListener("click", login);
function login(){
	let xttp = new XMLHttpRequest();

	xttp.onreadystatechange = function() {
		console.log(this.readyState);
		if (this.status == 200 && this.readyState == 4){
			window.location.href = "/main.html";
		}
	}
	
	let url = "http://10.0.0.141:5000/login";
	xttp.open("GET", url, true);
	xttp.setRequestHeader("Content-Type", "application/json");
	
	let username = document.getElementById('username').value;
	let password = document.getElementById('password').value;
	let loginObject = {"username": username, 'password': password};
	console.log(loginObject);
	xttp.send(JSON.stringify(loginObject));
}
