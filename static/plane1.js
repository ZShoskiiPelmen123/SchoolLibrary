function plane1(){

    let f = document.body;
    let MI = document.getElementById("mewing")
    let E = document.getElementsByClassName("Войти")
    document.getElementById("FedorTiLoh").style.visibility = "hidden"
    let enterBtn = document.getElementsByClassName("Enter")[0];
    let registerBtn = document.getElementsByClassName("Register")[0];
    let themeBtn = document.getElementsByTagName("button")[0];
    if (f.style.backgroundColor === 'rgb(127, 127, 127)') {
        f.style.backgroundColor = "white";
        f.style.color = enterBtn.style.color = registerBtn.style.color = "black";
        MI.src = "static/Безымянный.png";
        E[0].style.backgroundColor = 'rgb(223, 223, 223)';
        enterBtn.style.backgroundColor = registerBtn.style.backgroundColor = 'rgb(211, 211, 211)';
    } else {
        f.style.backgroundColor = "rgb(127, 127, 127)"
        f.style.color = enterBtn.style.color = registerBtn.style.color = "lightgray";
        MI.src = "static/Тёмный безымянный.png"
        E[0].style.backgroundColor = 'rgb(100, 100, 100)'
        enterBtn.style.backgroundColor = registerBtn.style.backgroundColor = 'grey';
}   }

