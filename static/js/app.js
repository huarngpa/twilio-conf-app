
/***************************************************************
VARIABLES
***************************************************************/

service_addr = '/service'

/***************************************************************
EVENT LISTENERS
***************************************************************/

// Bind action to form button
document.addEventListener('DOMContentLoaded', function() {
	document.getElementById('service_submit').addEventListener(
		'click', function(event) {
			event.preventDefault();
			serviceSubmit();
		});
});

/***************************************************************
APPLICATION CODE
***************************************************************/

// Main function for sending payload to database
function serviceSubmit() {
	// Makes a payload
	payload = {}
	to_number = document.getElementById('to_number').value;
	conf_num = document.getElementById('conf_num').value;
	passcode_1 = document.getElementById('passcode_1').value;
	passcode_2 = document.getElementById('passcode_2').value;
	payload['to_number'] = to_number;
	payload['conf_num'] = conf_num;
	payload['passcode_1'] = passcode_1;
	payload['passcode_2'] = passcode_2;
	// console.log(payload);
	if(typeof(to_number) == 'undefined' || to_number == '') {
		alert("Enter a valid phone number to send SMS to.");
	} else if(typeof(conf_num) == 'undefined' || conf_num == '') {
		alert("Enter a valid conference number!");
	} else {
		var req = new XMLHttpRequest();
		var res = {};
		req.open('POST', service_addr, true);
		req.setRequestHeader('Content-Type', 'application/json');
		req.addEventListener('load', function() {
			if(req.status >= 200 && req.status < 400) {
				alert('This is not classy, but... SMS successfully sent!');
			} else {
				console.log("Error in network request: " +
					req.statusText);
			}
		});
		req.send(JSON.stringify(payload))
	}
}
