//const wss = new WebSocket.Server({server:app});
const ws = new WebSocket.Server("ws://192.168.1.97:8765/events");
let userOn={};
function time(){
    return parseInt(new Date().getTime())
}
wss.on('connection', function(ws,req) {
    const user=getUser(req.url);
    let user_id=user['viewer_id'];
    if(MD5(user['api_id']+"_"+user['viewer_id']+"_"+appkey)!==user['auth_key'] || !user['auth_key']){
        console.info('Conn End');
        ws.close()
    }else{
        ws.onclient=user['viewer_id'];

        ws.userFind="";

        ws.timeconnect=time();
        userOn={[parseInt(user_id)]:time()};

        ///Функция отключения
        ws.funcDouble=function(){
            ws.send(JSON.stringify({doubleClient:"запущено в другой вкладке"}));
            ws.close();
        };
        //Поиск пользователя с таким-же id
        ws.typeDouble=function () {
            const clientOn=wss;
            let i=0;
            let findDouble = new Promise((resolve, reject) => {
                clientOn.clients.forEach((exit) => {
                    if (exit.userFind === ws.onclient){
                        exit.funcDouble()
                    }
                    i++;
                    if (i === parseInt(clientOn.options.server._connections)) resolve();
                });
            });
            findDouble.then(() => {
                ws.userFind=ws.onclient;
            });
        };

    }
    ws.on('close', function (data) {
        if(data !==1005){
            delete userOn[user_id]
        }
        console.info('exit',data)

    });
    ws.on('message', function (data) {
        console.info(data)
        try{
            const userSend=JSON.parse(data);

            if(userSend===data.doubleClient){
                console.info('double')
            }

            //console.info(userSend)

        }catch (e) {
            console.info('Не JSON')
            return false
        }

    })
}
)
