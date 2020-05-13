function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}
function eraseCookie(name) {   
    document.cookie = name+'=; Max-Age=-99999999;';  
}

function darkButtonClick() {
    if(getDarkmodeCookie()){
        setCookie("darkmode", "false", 30);
        setLightmode();
    }else{
        setCookie("darkmode", "true", 30);
        setDarkmode();
    }
}

function getDarkmodeCookie(){
    if(getCookie("darkmode")==null){
        setCookie("darkmode", "false", 30);
    }
    return getCookie("darkmode")=="true";
}

$(document).ready(function() {
    if(getDarkmodeCookie()){
        setDarkmode();
    }else{        
        setLightmode();
    }
}); 

function setDarkmode(){
    button = document.getElementById("darkButton");
    button.classList.remove("btn-primary");
    button.classList.add("btn-secondary");
    darktext = document.getElementById("darkButtonText").textContent="Light mode ☀️";
}

function setLightmode(){
    button = document.getElementById("darkButton");
    button.classList.remove("btn-secondary");
    button.classList.add("btn-primary");
    darktext = document.getElementById("darkButtonText").textContent="Dark mode 🌙";
    
    
}