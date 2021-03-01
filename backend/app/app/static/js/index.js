// создать подключение
//, ["json"]
//var ws = new WebSocket("ws://192.168.7.249:8088/
// ari/events?api_key=pbxuser:e07026d612c56a4ec8f62273ed366e48&app=channel-playback", ["json"]);
// < {"type":"ApplicationReplaced","timestamp":"2021-01-13T20:29:22.872+0800","application":"channel-playback","asterisk_id":"00:0c:29:03:ad:44"}

//var key = 'c1da6a19a11e9b9e2c74f4635bde3055'
//var socket = new WebSocket("ws://192.168.1.68:8088/ari/events?api_key=fastuser:" + key + "&app=channel-playback");
//var socket = new WebSocket("ws://" + location.hostname + ":5050/events");
var socket = new WebSocket("ws://" + location.host + "/fiz_liz");

// var ws = new WebSocket("ws://127.0.0.1:5050/events");
// var socket = new WebSocket("ws://localhost:5050/events")

// отправить сообщение из формы publish
/*
document.forms.publish.onsubmit = function() {
  var outgoingMessage = this.message.value;

  socket.send(outgoingMessage);
  return false;
};
*/

// обработчик входящих сообщений
/*
socket.onmessage = function(event) {
  var incomingMessage = event.data;
  showMessage(incomingMessage);
  console.log('event.data:', event.data);
};
*/
socket.onmessage = function(e){
   var incomingMessage = e.data;
   showMessage(incomingMessage);
   console.log(incomingMessage);
}

// показать сообщение в div#subscribe
function showMessage(message) {
  var messageElem = document.createElement('div');
  messageElem.appendChild(document.createTextNode(message));
  document.getElementById('subscribe').appendChild(messageElem);
}
