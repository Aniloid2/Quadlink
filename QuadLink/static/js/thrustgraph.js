
function callable_thrust(LinkObj) {

		console.log('Acceleration on X',LinkObj.x_acc)

		var dps = []; // dataPoints

		var chart = new CanvasJS.Chart("chartContainerthrust",{
			title :{
				text: "Live Thrust as percentage"
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
			chart.render();		

		};



		// updateChart(dataLength)
		// update chart after specified time. 
		//setInterval(function(){updateChart()}, updateInterval); 
		console.log('link object, update thrust',LinkObj.acceleration)
		LinkObj.thrust.on('value', function(snapshot) {
		// console.log('accel', snapshot.child('x_acc'))// snap value will be in json format eith values
			thrust = snapshot.val()
			thrust_as_perc = (thrust - 1000)/10
			console.log('thrust value', thrust, thrust_as_perc)



			updateChart(undefined, thrust_as_perc)
		});
		

	}
