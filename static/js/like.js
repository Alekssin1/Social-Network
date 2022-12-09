// перевіряємо дві кнопки з лайком на натискання
$('.likebutton').click(my_ajax);
$('.likebutton_none').click(my_ajax);

function my_ajax() {
    // значення айді посту
    var id = this.classList[1];
    $.ajax(
        {
            type: "GET",
            url: "ajax",
            data: {
                "result": id,
            },
            dataType: "json",
            success: function (data) {
                // якщо лайк не поставлений
                if (data.like == true) {
                    // змінюємо лайк на актисний
                    var nonActiveLike = document.getElementsByClassName("likebutton" + id)[0];
                    nonActiveLike.classList.remove('d-b');
                    nonActiveLike.classList.add('d-n');
                    var ActiveLike = document.getElementsByClassName("likebutton_none" + id)[0];
                    ActiveLike.classList.remove('d-n');
                    ActiveLike.classList.add('d-b');
                    var num_likes = document.getElementsByClassName("like_number" + id)[0];
                    // змінюємо кількість лайків на +1
                    var num = Number(num_likes.textContent)
                    num_likes.innerHTML = num+1
                }
                // якщо лайк поставлений
                else {
                    // змінюємо лайк на неактивний
                    var ActiveLike = document.getElementsByClassName("likebutton_none" + id)[0];
                    ActiveLike.classList.remove('d-b');
                    ActiveLike.classList.add('d-n');
                    var nonActiveLike = document.getElementsByClassName("likebutton" + id)[0];
                    nonActiveLike.classList.remove('d-n');
                    nonActiveLike.classList.add('d-b');
                    var num_likes = document.getElementsByClassName("like_number" + id)[0];
                    // змінюємо кількість лайків на -1
                    var num = Number(num_likes.textContent)
                    num_likes.innerHTML = num-1
                }
            }
        })
}