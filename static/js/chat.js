const id = JSON.parse(document.getElementById('json-username').textContent);
const message_username = JSON.parse(document.getElementById('json-message-username').textContent);

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
    if (data.base64 === "1") {

        if (data.username == message_username) {
            document.querySelector('#chat').innerHTML += `<div class="right for_audio">
            <audio controls="controls" autobuffer="autobuffer" class="my_audio">
              <source src="data:audio/wav;base64, ${data.message}" />
            </audio> 
            <span class="time_message">${datetime}</span>
          </div>`

        } else {
            document.querySelector('#chat').innerHTML += `<div class="left ">
            <audio controls="controls" autobuffer="autobuffer" class="my_audio">
              <source src="data:audio/wav;base64, ${data.message}" />
            </audio> 
            <span class="time_message">${datetime}</span>
          </div>`
        }
    }
    else {
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

}

document.querySelector('#chat-message-submit').onclick = function (e) {
    const message_input = document.querySelector('#message_input');
    const message = message_input.value;

    socket.send(JSON.stringify({
        'message': message,
        'username': message_username,
        'base64': "0"
    }));

    message_input.value = '';
}

jQuery(document).ready(function () {
    var $ = jQuery;
    var myRecorder = {
        objects: {
            context: null,
            stream: null,
            recorder: null
        },
        init: function () {
            if (null === myRecorder.objects.context) {
                myRecorder.objects.context = new (
                    window.AudioContext || window.webkitAudioContext
                );
            }
        },
        start: function () {
            var options = { audio: true, video: false };
            navigator.mediaDevices.getUserMedia(options).then(function (stream) {
                myRecorder.objects.stream = stream;
                myRecorder.objects.recorder = new Recorder(
                    myRecorder.objects.context.createMediaStreamSource(stream),
                    { numChannels: 1 }
                );
                myRecorder.objects.recorder.record();
            }).catch(function (err) { });
        },
        stop: function (listObject) {
            if (null !== myRecorder.objects.stream) {
                myRecorder.objects.stream.getAudioTracks()[0].stop();
            }
            if (null !== myRecorder.objects.recorder) {
                myRecorder.objects.recorder.stop();


                // Validate object
                if (null !== listObject
                    && 'object' === typeof listObject
                    && listObject.length > 0) {


                    // Export the WAV file
                    myRecorder.objects.recorder.exportWAV(function (blob) {
                        // var url = (window.URL || window.webkitURL)
                        //     .createObjectURL(blob);


                        // var audioObject = $('<audio class="audio" controls></audio>')
                        //     .attr('src', url);


                        var reader = new window.FileReader();
                        reader.readAsDataURL(blob);
                        reader.onloadend = function () {
                            base64 = reader.result;
                            base64 = base64.split(',')[1];


                            socket.send(JSON.stringify({
                                'message': base64,
                                'username': message_username,
                                'base64': "1",
                            }));

                        }

                        // // Wrap everything in a row
                        // var holderObject = $('<div class="row"></div>')
                        //     .append(audioObject);

                        // // Append to the list
                        // listObject.append(holderObject);
                    });
                }
            }
        }
    };

    // Prepare the recordings list
    var listObject = $('[data-role="recordings"]');

    // Prepare the record button
    $('[data-role="controls"] > button').click(function () {
        // Initialize the recorder
        myRecorder.init();

        // Get the button state 
        var buttonState = !!$(this).attr('data-recording');

        // Toggle
        if (!buttonState) {
            $(this).attr('data-recording', 'true');
            myRecorder.start();
        } else {
            $(this).attr('data-recording', '');
            myRecorder.stop(listObject);
        }
    });
});