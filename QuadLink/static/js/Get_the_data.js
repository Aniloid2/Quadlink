
function get_the_data() {

	var video = document.getElementById('video_stream');

	var audio = document.getElementById('audio_stream');

	function update_video_ip(ip) {
		video.src = 'http://' + ip + '/video'
		console.log(video.src)
	}

	function update_audio_ip() {
		audio.src = 'http://' + ip +'/audio.wav'
		console.log(audio.src)
	}


	console.log('hi');

	var quad = document.getElementById("quad_username").value;

	var databaseURL = "https://quadlink-c80dc.firebaseio.com"

	var folder = quad.concat(databaseURL)
	console.log(folder)


	console.log(quad)

	var config = {
	apiKey: "AIzaSyA1He_lYsMphHl41rpQSEUfTeYIj976Oz4",
	authDomain: "quadlink-c80dc.firebaseapp.com",
	databaseURL: folder,
	storageBucket: "quadlink-c80dc.appspot.com",
	};


	firebase.initializeApp(config);

	const dbRefObject = firebase.database().ref().child(quad);


	const axis = firebase.database().ref().child(quad).child("axis")

	const pitch = firebase.database().ref().child(quad).child("axis").child("pitch")

	const roll = firebase.database().ref().child(quad).child("axis").child("roll")

	const yaw = firebase.database().ref().child(quad).child("axis").child("yaw")

	const ip_address = firebase.database().ref().child(quad).child('ip_address')


	const acceleration = firebase.database().ref().child(quad).child('acceleration')

	const x_acc = firebase.database().ref().child(quad).child('acceleration').child('x_acc')

	const y_acc = firebase.database().ref().child(quad).child('acceleration').child('y_acc')

	const z_acc = firebase.database().ref().child(quad).child('acceleration').child('z_acc')

	const thrust = firebase.database().ref().child(quad).child('thrust')

	var LinkedObj = new links(axis,pitch, roll, yaw, ip_address,acceleration, x_acc,y_acc,z_acc, thrust)
	console.log('Parts of lissener object',LinkedObj.pitch,LinkedObj.roll,LinkedObj.yaw )
	console.log(thrust)
	LinkedObj.ip_address.on('value', function(snapshot) {
		
		ip = snapshot.val()
		console.log(ip)
		update_video_ip(ip)
		update_audio_ip(ip)

	})

	return LinkedObj;

	}