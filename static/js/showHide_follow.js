$(document).ready(function(){   
    FollowingHide();
    FollowedHide();
    EditHide();
});

function FollowingShow(){
    $("#user_form-back").show();
    $("#user_form").show();
    $("body").css("overflow","hidden"); 
}

function FollowingHide(){
    $("#user_form-back").hide();
    $("#user_form").hide();
    $("body").css("overflow","auto");
}

function FollowedShow(){
    $("#userFollower_form-back").show();
    $("#userFollower_form").show();
    $("body").css("overflow","hidden"); 
}

function FollowedHide(){
    $("#userFollower_form-back").hide();
    $("#userFollower_form").hide();
    $("body").css("overflow","auto");
}

function EditShow(){
    $("#user_form_edit-back").show();
    $("#user_form_edit").show();
    $("body").css("overflow","hidden"); 
}

function EditHide(){
    $("#user_form_edit-back").hide();
    $("#user_form_edit").hide();
    $("body").css("overflow","auto");
}