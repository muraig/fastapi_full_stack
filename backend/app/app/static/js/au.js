/*
 const el = document.getElementById('chart');
 const dataPoints = [];
 const chart = new TimeChart(el, {
     series: [{ data: dataPoints, name: 'Real-time measurement streaming', color: 'darkblue' }],
     realTime: true,
     xRange: { min: 0, max: 500 },
 });
 */
 //const ws = new WebSocket("ws://localhost:8000/ws");
 //const ws = new WebSocket("ws://" + location.hostname + ":8008/ws");
 const ws = new WebSocket("ws://" + location.host + "/ws");

 let x = 0;
 ws.onmessage = function(event) {
     const measurement = event.data;
     x += 1
     dataPoints.push({x, y: measurement.value});
     chart.update();
 };
