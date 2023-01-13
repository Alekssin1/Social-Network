setInterval(function () {
    $("#another_users").load(location.href + " #another_users>*", "");

    if (document.getElementById("#title_chat")) {
        $("#title_chat").load(location.href + " #title_chat>*", "");
    }
}, 5000);

