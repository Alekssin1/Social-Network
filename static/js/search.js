$(document).ready(function(){   
    searchHide()
});

function searchShow(){

    if (document.getElementById("search-button-inp").style.display != "none") {
        $("#search-button-inp").hide();
    }
    else {
        $("#search-button-inp").show();
    }
    
}

function searchHide(){
    $("#search-button-inp").hide();
}