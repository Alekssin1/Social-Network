var id = JSON.parse(document.getElementById('json-posts').textContent);


const socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + id
    + '/'
);

socket.onopen = function (e) {
    console.log("CONNECTION ESTABLISHED");
}

socket.onclose = function (e) {
    console.log("CONNECTION LOST");
}

socket.onerror = function (e) {
    console.log("ERROR OCCURED");
}


socket.onmessage = function (e) {
    var currentdate = new Date();
    var datetime =
        + ((currentdate.getHours()) < 10 ? "0" + currentdate.getHours() : currentdate.getHours()) + ":"
        + ((currentdate.getMinutes()) < 10 ? "0" + currentdate.getMinutes() : currentdate.getMinutes());
    const data = JSON.parse(e.data);
    console.log(data);
        if (data.message != "") {
            if (data.username == message_username) {
                document.querySelector('#chat').innerHTML += `<div class="chat_message right">
            <span class="chat_message-text">${data.message}</span>
            <span class="time_message">${datetime}</span>
        </div>`
            } else {
                document.querySelector('#chat').innerHTML += `<div class="chat_message">
            <img class="title_chat_avatar" src="{% static 'assets/dp.png' %}" alt="avatar">
            <span class="chat_message-text">${data.message}</span>
            <span class="time_message">${datetime}</span>
        </div>`
            }
        }

}

// document.querySelector('#chat-message-submit').onclick = function (e) {
//     const message_input = document.querySelector('#message_input');
//     const message = message_input.value;

//     socket.send(JSON.stringify({
//         'message': message,
//         'username': message_username,
//         'base64': "0"
//     }));

//     message_input.value = '';
// }