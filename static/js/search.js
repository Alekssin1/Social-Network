$(document).ready(function(){   
    searchHide()
});

function searchShow(){ 
    var inp = document.getElementById("search-button-inp");
    if (document.getElementById("search-button-inp").style.visibility != "hidden") {
        inp.style.top = '-100%';
        // document.getElementById("search-button-inp").style.transition = "top .5s cubic-bezier(0, 0, 1, 1), visibility 1s 1s"
        document.getElementById("search-button-inp").style.visibility = "hidden";
    }
    else {
        inp.style.top = '0';
        // document.getElementById("search-button-inp").style.transition = "top .5s cubic-bezier(0, 0, 1, 1), visibility 1s 1s"
        document.getElementById("search-button-inp").style.visibility = "inherit";
    }
}

function searchHide(){
    var inp = document.getElementById("search-button-inp");
    inp.style.top = '-100%';
    // document.getElementById("search-button-inp").style.transition = "top .5s cubic-bezier(0, 0, 1, 1), visibility 1s 1s"
    document.getElementById("search-button-inp").style.visibility = "hidden";
}


