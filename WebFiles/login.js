document.getElementById("login").addEventListener("click", login);
function login(){
	let xttp = new XMLHttpRequest();

	xttp.onreadystatechange = function() {
		console.log(this.readyState);
		if (this.status == 200 && this.readyState == 4){
			window.location.href = "/home/pi/Desktop/WebServer/WebFiles/MainPage.html";
		}
	}
	
	let url = "localhost:5000/login";
	xttp.open("GET", url, true);
	xttp.setRequestHeader("Content-Type", "application/json");
	
	let username = document.getElementById('username').innerHTML;
	let password = document.getElementById('password').innerHTML;
	let loginObject = {"username": username, 'password': password};
	xttp.send(loginObject);
}
