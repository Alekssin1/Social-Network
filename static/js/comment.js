var id = JSON.parse(document.getElementById('json-posts').textContent);
const comment_username = JSON.parse(document.getElementById('json-comment-username').textContent);

const socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + 'comment/'
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
        document.querySelector('#comment_for_post').innerHTML += `<div class="user_post">
            <img
              class="avatar online"
              src="{% static 'assets/dp.png' %}"
              alt="avatar"
            />
              <div class="about_user">
                <span class="nickname_post">${data.username}</span>
                <span class="comment_text post_subtitle">${data.comment}</span>
              </div>               
          </div>`
    }

}

document.querySelector('#post-comment-submit').onclick = function (e) {
    const comment_input = document.querySelector('#comment_input');
    const comment = comment_input.value;

    socket.send(JSON.stringify({
        'comment': comment,
        'username': comment_username,
    }));

    comment_input.value = '';
}