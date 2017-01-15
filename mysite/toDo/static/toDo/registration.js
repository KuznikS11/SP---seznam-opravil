document.addEventListener("DOMContentLoaded", function() {
	document.getElementById("username").addEventListener("change", chkUsername);
	document.getElementById("email").addEventListener("change", chkEmail);
	document.getElementById("formRegister").addEventListener("submit", chkEqualPass);
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

function chkUsername(event) {

// Get the target node of the event
  var name = event.currentTarget.value;

// Test the format of the input name 
//  Allow the spaces after the commas to be optional
//  Allow the period after the initial to be optional

  var pos = name.search(/^[A-Za-z0-9]+$/i);

  if (pos != 0 || (!(name.length>2 && name.length<25))){
    alert("The name you entered (" + name + 
          ") is not in the correct form (only letters and numbers are allowed)or it is too short or too long\n");
	return false;
   }
   return true;
}

function chkEmail(event) {
	
	var myEmail = event.currentTarget.value;
	
	var pos = myEmail.search(/^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
	if (pos != 0){
		alert("The email you entered (" + myEmail + 
          ") is not in the correct form\n");
		return false;
	}
	return true;
	
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
