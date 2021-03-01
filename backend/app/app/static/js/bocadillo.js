//const ws = new WebSocket("ws://" + location.hostname + ":8765/echo");
const ws = new WebSocket("ws://192.168.1.97:8765/events");


ws.onopen = event => console.log("Connected:", event);
ws.onclose = event => console.log("Connection lost:", event);
ws.onmessage = event => console.log("Received:", JSON.parse(event.data));

setInterval(() => {
  const message = { text: Math.random() > 0.5 ? "ping" : "pong" };
  ws.send(JSON.stringify(message));
  console.log("Sent: ", message);
}, 1000);