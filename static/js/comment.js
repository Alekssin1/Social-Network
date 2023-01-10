var id = JSON.parse(document.getElementById('json-posts').textContent);
const comment_username = JSON.parse(document.getElementById('json-comment-username').textContent);

// створюємо новий об'єкт вебсокету
const socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + 'comment/'
    + id
    + '/'
);

// відкриває
socket.onopen = function (e) {
    console.log("CONNECTION ESTABLISHED");
}

// закриває
socket.onclose = function (e) {
    console.log("CONNECTION LOST");
}

// помилки
socket.onerror = function (e) {
    console.log("ERROR OCCURED");
}

// повідомлення
socket.onmessage = function (e) {
    // отримуємо дату
    var currentdate = new Date();
    // створюємо шаблон за яким дата буде виводитися в потрібному нам вигляді
    var datetime =
        + ((currentdate.getHours()) < 10 ? "0" + currentdate.getHours() : currentdate.getHours()) + ":"
        + ((currentdate.getMinutes()) < 10 ? "0" + currentdate.getMinutes() : currentdate.getMinutes());
    // отримуємо данні з chats.consumers.py    
    const data = JSON.parse(e.data);
    
    // перевірка на пустий рядок
    if (data.message != "") {
        // виводить коментарій
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
    window.scrollTo(0, document.body.scrollHeight);
}




// при натисканні на кнопку відправляємо json за допомогою сокетів в social_network.consumers.py 
document.querySelector('#post-comment-submit').onclick = function (e) {
     // отримання даних з поля вводу
    const comment_input = document.querySelector('#comment_input');
    const comment = comment_input.value;

    socket.send(JSON.stringify({
        'comment': comment,
        'username': comment_username,
    }));

    // заміняємо значення введеного тексту на пустий рядок
    comment_input.value = '';
}