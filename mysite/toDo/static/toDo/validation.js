
document.addEventListener("DOMContentLoaded", function() {
	document.getElementById("username").addEventListener("change", chkUsername);
	document.getElementById("password").addEventListener("change", chkPassword);
	document.getElementById("signIn").addEventListener("submit", redirect);
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


function chkPassword(event) {

  var pass = event.currentTarget.value;

  if (!(pass.length>5 && pass.length<25)) {
    alert("The password you entered is too short or too long\n");
	return false;
   }
   return true;
}

function redirect(event) {
	window.location.replace("profil.html");
}
