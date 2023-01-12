$(document).ready(function(){   
    PopUpHide();
});

function PopUpShow(){
    $("#user_form-back").show();
    $("#user_form").show();
    $("body").css("overflow","hidden"); 
}

function PopUpHide(){
    $("#user_form-back").hide();
    $("#user_form").hide();
    $("body").css("overflow","auto");
}
