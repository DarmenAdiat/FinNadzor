<template>
  <div id="chartContainer" style="width: 100%;height: 360px;" ref="chartContainer"></div>
</template>
<script>	
if (process.client) {
	var CanvasJS = require('../assets/canvasjs.min.js');
	var chart = new CanvasJS.Chart("chartContainer", {
	  title:{
		text: "Column Chart in Nuxt.js"
	  },
	  data: [{				
		dataPoints: [
		  { x: 10, y: 71 },
		  { x: 20, y: 55},
		  { x: 30, y: 50 },
		  { x: 40, y: 65 },
		  { x: 50, y: 95 },
		  { x: 60, y: 68 },
		  { x: 70, y: 28 },
		  { x: 80, y: 34 },
		  { x: 90, y: 14}
		]
	  }]
	});
	chart.render();
}
</script>

<style>

</style>
