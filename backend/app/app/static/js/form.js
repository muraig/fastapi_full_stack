    var ws = new WebSocket("ws://" + location.hostname + ":8765/events");
    var messages = document.getElementById('messages');
    var message = document.createElement('ul');
    message.className= "event";
    messages.appendChild(message);

    ws.onmessage = function(event) {
        var messages = document.querySelector("div#messages ul.event")
        var messag = document.createElement('li')
        messag.className= "message";

        var messa = document.createElement('span');
        messa.className= "symbol";
        messag.appendChild(messa)
        var mess = document.createElement('span');
        mess.className= "value";
        messag.appendChild(mess)

        //console.log('li:', messag);

        var content = document.createTextNode(event.data)
        //var content = document.createTextNode(event.data.split(','))
        console.log('content:', content);
        console.log('content[1]', content[1]);

     document.getElementsByClassName('value').textContent = content[1];
        console.log('span:', mess);

        messag.appendChild(content)
        messages.appendChild(messag)
    };

    function sendMessage(event) {
        var ul = document.querySelectorAll('#messages ul');
        console.log('ul:', ul);
        this.parentNode.removeChild(ul);

        var input = document.getElementById("messageText")
        ws.send(input.value)
        input.value = ''
        event.preventDefault()
    }
