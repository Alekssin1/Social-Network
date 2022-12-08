$('.likebutton').click(my_ajax);
$('.likebutton_none').click(my_ajax);

function my_ajax() {
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

                if (data.like == true) {
                    // when we don`t have data in BD
                    var nonActiveLike = document.getElementsByClassName("likebutton" + id)[0];
                    nonActiveLike.classList.remove('d-b');
                    nonActiveLike.classList.add('d-n');
                    var ActiveLike = document.getElementsByClassName("likebutton_none" + id)[0];
                    ActiveLike.classList.remove('d-n');
                    ActiveLike.classList.add('d-b');
                    var num_likes = document.getElementsByClassName("like_number" + id)[0];
                    var num = Number(num_likes.textContent)
                    num_likes.innerHTML = num+1
                }
                else {
                    var ActiveLike = document.getElementsByClassName("likebutton_none" + id)[0];
                    ActiveLike.classList.remove('d-b');
                    ActiveLike.classList.add('d-n');
                    var nonActiveLike = document.getElementsByClassName("likebutton" + id)[0];
                    nonActiveLike.classList.remove('d-n');
                    nonActiveLike.classList.add('d-b');
                    var num_likes = document.getElementsByClassName("like_number" + id)[0];
                    var num = Number(num_likes.textContent)
                    num_likes.innerHTML = num-1
                }
            }
        })
}