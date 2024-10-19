function plane1(){
    let f = document.body;
    let MI = document.getElementById("mewing");
    let E = document.getElementsByClassName("authForm");
    document.getElementById("FedorTiLoh").style.visibility = "hidden";
    let enterBtn = document.getElementsByClassName("Enter")[0];
    //let registerBtn = document.getElementsByClassName("Register")[0];
    let btnList = $('.authForm').find('button');
    let inputList = $('input');
    let themeBtn = document.getElementsByTagName("button")[0];

    if (f.style.backgroundColor === 'rgb(127, 127, 127)') { // светлая тема
        f.style.backgroundColor = "white";
        f.style.color = "black";
        MI.src = "static/Безымянный.png";
        E[0].style.backgroundColor = 'rgb(223, 223, 223)';
        for (const item of btnList) {
            item.style.backgroundColor = 'rgb(211, 211, 211)'
        }
        for (const item of inputList) {
            item.style.backgroundColor = 'white';
        }
        if ($('select').length > 0)
            $('select').css('backgroundColor', 'white');
    } else { // тёмная тема
        f.style.backgroundColor = "rgb(127, 127, 127)"
        f.style.color = "lightgray";
        MI.src = "static/Тёмный безымянный.png"
        E[0].style.backgroundColor = 'rgb(100, 100, 100)'
        for (const item of btnList) {
            item.style.backgroundColor = 'grey';
        }
        for (const item of inputList) {
            item.style.backgroundColor = 'darkgray';
        }
        if ($('select').length > 0)
            $('select').css('backgroundColor', 'darkgray');
}   }

