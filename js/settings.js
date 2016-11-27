document.addEventListener("DOMContentLoaded", function() {
	document.getElementById("changePass").addEventListener("submit", chkEqualPass);
	document.getElementById("btnDelete").addEventListener("click", deleteAccount)
});

window.addEventListener("beforeunload", beforeUnload);


function beforeUnload(event) {
	inputs = document.querySelectorAll("input[type='text'], input[type='email'], input[type='password']");
	for(i=0; i<inputs.length; i++){
		if (inputs[i].value !=""){
			event.returnValue = "warning!";
			return "Warning!";
		}
	}

}



function chkEqualPass(event) {
	var p1 = document.getElementById("password1").value;
	var p2 = document.getElementById("password2").value;
	
	if (!(p1.length>5 && p1.length<25) || !(p2.length>5 && p2.length<25)) {
		alert("The password you entered is too short or too long")
	}
	
	if (p1 != p2) {
		alert("Passwords don't match")
	}
	else {
		window.location.replace("profil.html");
	}
}

function deleteAccount(event) {
	var foo = confirm("are you shure you want to delete your account?");
	if (foo == true) {
		window.location.replace("index.html");
	}
}
	