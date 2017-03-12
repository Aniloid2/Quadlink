

function callable(LinkObj) {

		console.log('Acceleration on X',LinkObj.x_acc)

		var dps = []; // dataPoints

		var chart = new CanvasJS.Chart("chartContainer",{
			title :{
				text: "Live Acceleration"
			},			
			data: [{
				type: "line",
				dataPoints: dps 
			}]
		});

		var xVal = 0;
		var yVal = 0;	
		var updateInterval = 100;
		var dataLength = 250; // number of dataPoints visible at any point
		var updateChart = function (count, y_value) {
			console.log(y_value)
			count = count || 1;
			// count is number of times loop runs to generate random dataPoints.
			console.log(count)

			if (y_value != undefined) {
				offset = y_value;
			}
			else {
				offset = 0;
			}
			for (var j = 0; j < count; j++) {	
				yVal = offset;
				console.log('im filling graph')
				dps.push({
					x: xVal,
					y: yVal
				});
				xVal++;
				console.log(xVal);
			};
			if (dps.length > dataLength)
			{
				dps.shift();				
			}
			console.log('not working')
			chart.render();		

		};



		// updateChart(dataLength)
		// update chart after specified time. 
		//setInterval(function(){updateChart()}, updateInterval); 
		console.log('link object, update acceleration',LinkObj.acceleration)
		LinkObj.acceleration.on('value', function(snapshot) {
		// console.log('accel', snapshot.child('x_acc'))// snap value will be in json format eith values
			console.log('value', snapshot.child('x_acc').val(), snapshot.val())
			// find magnitude. and call function
			x_acc = snapshot.child('x_acc').val()
			y_acc = snapshot.child('y_acc').val()
			z_acc = snapshot.child('z_acc').val()
			modulus = Math.pow(x_acc, 2) + Math.pow(y_acc,2) + Math.pow(z_acc,2)
			acc = Math.sqrt(modulus)
	


			updateChart(undefined, acc)
		});
		

	}

