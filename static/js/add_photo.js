function add_photo(input_element, id_photo) {
    $(input_element).on('change', function () {
        var input = $(this)
        if (input[0].files && input[0].files[0]) {
            let f = input[0].files[0];
            console.log(f);
            img = document.getElementById(id_photo);
            console.log(img);
            if (f) {
                img.src = URL.createObjectURL(f);
                localStorage.setItem('myImage', img.src);
            }
            img.classList.add(id_photo);
        }
    })
}

add_photo('input[id="id_avatar"]', 'id_avatar_show-photo');
add_photo('input[id="id_background"]', 'id_background_show-photo');