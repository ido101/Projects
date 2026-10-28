let color = 'aqua';
function ChangeCol(){
    let form = document.forms[0];
    let i;
    for(i = 0;i<form.length;i++){
        if(form[i].checked){
            color = form[i].id;
        }
    }
    document.getElementById("body").style.backgroundColor = color;
}
