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

function replaceClassList(ids, remove, add){
    for (var i = 0; i < ids.length; i++){
        replaceClassObject(ids[i], remove, add);
    }    
}

function replaceClassObject(id, remove, add){
    try {
        try {
            if(remove.length>0){
                document.getElementById(id).classList.remove(remove);
            }
        }catch (error) {}
        try {
            if(add.length>0){
                document.getElementById(id).classList.add(add);
            }
        }catch (error) {}        
    } catch (error) {}
}
root = document.documentElement;

function setLightmode(){
    replaceClassList(["darkButton", "filtersButton", "loginButton"], "btn-secondary", "btn-primary");
    replaceClassList(["indexContent", "mainTable", "footer"], "bg-dark", "bg-light");
    replaceClassList(["modalLoginContent", "modalProfileContent"], "bg-dark", "") 

    document.getElementById("darkButtonText").textContent="Dark mode 🌙";
    replaceClassObject("dataTable", "table-dark", "");
    replaceClassObject("mainTable", "text-light", "text-dark"); 
    replaceClassObject("superiorNav", "bg-dark", "bg-dark-md");
    replaceClassObject("main", "", "bg-light");
    delete root.dataset.theme;
}

function setDarkmode(){
    replaceClassList(["darkButton", "filtersButton", "loginButton"], "btn-primary", "btn-secondary");
    replaceClassList(["indexContent", "mainTable", "footer"], "bg-light", "bg-dark")
    replaceClassList(["modalLoginContent", "modalProfileContent"], "", "bg-dark")

    document.getElementById("darkButtonText").textContent="Light mode ☀️";
    replaceClassObject("dataTable", "", "table-dark");
    replaceClassObject("mainTable", "text-dark", "text-light");
    replaceClassObject("superiorNav", "bg-dark-md", "bg-dark");
    replaceClassObject("main", "bg-light", "");
    
    root.dataset.theme = 'dark';
}