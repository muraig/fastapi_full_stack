// создаем WebSocket подключение
//const socket = new WebSocket("ws://localhost:8080");
const socket = new WebSocket("ws://192.168.1.97:8765/events");


// устанавливаем обработчик событий, вызываемый при открытии соединения
socket.onopen = function(event) {
    socket.send("соединение с сервером установлено");
    // отправляем определенные данные в формате JSON
    var data = {"message": "test"}
    socket.send(JSON.stringify(data));
};
// устанавливаем обработчик событий, вызываемый при получении сообщения от сервера
socket.onmessage = function(event) {
    console.log("сообщение от сервера получено", event.data);
}
// устанавливаем обработчик событий, вызываемый при ошибке
socket.onerror = function(event) {
  console.error("Ошибка WebSocket");
  socket.close(); // закрываем подключение к серверу
}
// устанавливаем обработчик событий, вызываемый при закрытии соединения
socket.onclose = function(event) {
  socket.send("соединение с сервером завершено");
}
/////////////////////////////////////////////////
/////////////////////////////////////////////////
var ws = new WebSocket("ws://echo.websocket.org");
//Используйте протокол «ws://», если нужно не шифрованное соединение или протокол «wss://» для шифрованного соединения.
//Этап. Создание обработчиков событий.
//После того как мы создали объект WebSocket необходимо повесить функции-обработчики на события.

ws.onopen = function()
{
	console.log("Соединение установлено.");
};

ws.onclose = function(event)
{
	console.log("Соединение закрыто. Код «" + event.code + "». Причина «" + event.reason + "».");
};

ws.onmessage = function(event)
{
	console.log("Пришло сообщение «" + event.data + "».");
};

ws.onerror = function(error) 
{
	console.log("Произошла ошибка: «" + error.message + "».");
};
/////////////////////////////////////////////////////////////
// Если нужно повесить несколько функций на событие используем методы «addEventListener» и «removeEventListener». Пример:

ws.addEventListener("message", function(event)
{
	console.log("Пришло сообщение «" + event.data + "».");
});

ws.addEventListener("message", function(event)
{
	console.log("Обрабатываем сообщение «" + event.data + "».");
});

ws.addEventListener("open", function(){});
ws.addEventListener("close", function(event){});
ws.addEventListener("message", function(event){});
ws.addEventListener("error", function(error){});
