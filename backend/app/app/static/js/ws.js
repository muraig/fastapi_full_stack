    // var ws = new WebSocket("ws://" + location.host + "/ws");
    //var ws = new WebSocket("ws://" + location.hostname + ":5050/events");
    var ws = new WebSocket("ws://" + location.host + "/events");
    //var messages = document.getElementById('messages');
    //var messages = document.querySelector("div#messages ul.event")
    //var message = document.removeChild('ul');
    //var oldChild = element.removeChild(child);
    //element.removeChild(child);
    let ul = document.querySelectorAll('#messages ul');
    function deleteUl() {
        for (var i = 0, len = ul.length; i < len; i++) {
          ul[i].onclick = function() {
            //console.log('parentNode', this.parentNode);
            //console.log('element => this', this);
            this.parentNode.removeChild(this);
          }
        }
    }

    var messages = document.getElementById('messages');
    var message = document.createElement('ul');
    message.className= "event";
    //console.log('message:', message);
    if (message.length > 0) {
        messages.appendChild(message);
    }


    ws.onmessage = function(event) {
        var messages = document.querySelector("div#messages ul.event")
        //console.log('messages:', messages);

        var messag = document.createElement('li')
        messag.className= "lsname";

        var content = document.createTextNode(event.data)
        messag.appendChild(content)
        //console.log('messag:', messag);

        //console.log('content:', content);

        messages.appendChild(messag)
    };

    function sendMessage(event) {
        var input = document.getElementById("messageText")
        ws.send(input.value)
        input.value = ''
        event.preventDefault()
    }
