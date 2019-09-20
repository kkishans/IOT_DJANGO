( function ( $ ) {

	var charts = {
		init: function () {
			// -- Set new default font family and font color to mimic Bootstrap's default styling
			Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
			Chart.defaults.global.defaultFontColor = '#292b2c';

			this.createCompletedJobsChart();

		},

		// ajaxGetPostMonthlyData: function () {
		// 	var urlPath =  'http://' + window.location.hostname + '/get-post-chart-data';
		// 	var request = $.ajax( {
		// 		method: 'GET',
		// 		url: urlPath
		// } );

		// 	request.done( function ( response ) {
		// 		console.log( response );
		// 		charts.createCompletedJobsChart( response );
		// 	});
		// },

		/**
		 * Created the Completed Jobs Chart
		 */
		createCompletedJobsChart: function () {

			var ctx = document.getElementById("mychart");
			var myLineChart = new Chart(ctx, {
				type: 'line',
				data: {
					labels: ["10:00", "10:30", "11:00","11:30	"], // The response got from the ajax request containing all month names in the database
					datasets: [{
						label: "Temperature",
						lineTension: 0.3,
						backgroundColor: "rgba(2,117,216,0.2)",
						borderColor: "rgba(2,117,216,1)",
						pointRadius: 5,
						pointBackgroundColor: "rgba(2,117,216,1)",
						pointBorderColor: "rgba(255,255,255,0.8)",
						pointHoverRadius: 5,
						pointHoverBackgroundColor: "rgba(2,117,216,1)",
						pointHitRadius: 20,
						pointBorderWidth: 2,
						data: [26,29,30,30] // The response got from the ajax request containing data for the completed jobs in the corresponding months
					},
					{ label: "Humidity",
						lineTension: 0.3,
						backgroundColor: "rgba(255,77,77,0.2)",
						borderColor: "rgba(253, 44, 0,1)",
						pointRadius: 5,
						pointBackgroundColor: "rgba(255,0,5,1)",
						pointBorderColor: "rgba(255,255,255,0.8)",
						pointHoverRadius: 5,
						pointHoverBackgroundColor: "rgba(255, 102, 102,1)",
						pointHitRadius: 20,
						pointBorderWidth: 2,
						data: [10,15,20,60]
				}
				],
				},
				options: {
					scales: {
						xAxes: [{
							time: {
								unit: 'date'
							},
							gridLines: {
								display: false
							},
							ticks: {
								maxTicksLimit: 7
							}
						}],
						yAxes: [{
							ticks: {
								min: 0,
								max: 100, // The response got from the ajax request containing max limit for y axis
								maxTicksLimit: 5
							},
							gridLines: {
								color: "rgba(0, 0, 0, .125)",
							}
						}],
					},
					legend: {
						display: false
					}
				}
			});
		}
	};

	charts.init();

} )( jQuery );