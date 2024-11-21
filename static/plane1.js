function plane1(newTheme) {
    let f = document.body;
    let MI = document.getElementById("mewing");
    let E = document.getElementsByClassName("authForm");
    let p = document.getElementById("Kvass1")
    document.getElementById("FedorTiLoh").style.visibility = "hidden";
    let enterBtn = document.getElementsByClassName("Enter")[0];
    //let registerBtn = document.getElementsByClassName("Register")[0];
    let btnList = $('.authForm').find('button');
    let inputList = $('input');
    let themeBtn = document.getElementsByTagName("button")[0];

    if (newTheme === 'white') { // светлая тема
        $('body').attr('data-theme', 'white');
        f.style.backgroundColor = "rgba(26,169,127,0.4)";
        f.style.color = "black";
        f.style.backgroundImage = 'url("static/DayBackroundBlur.jpg")';
        MI.src = "static/Безымянный.png";
        p.style.backgroundImage = 'url("static/DayBackround.jpg")';
        E[0].style.backgroundColor = 'rgb(223, 223, 223, 0)';
        for (const item of btnList) {
            item.style.backgroundColor = 'rgb(211, 211, 211)'
        }
        for (const item of inputList) {
            item.style.backgroundColor = 'rgba(37,92,202,0.5)';
        }
        if ($('select').length > 0)
            $('select').css('backgroundColor', 'white');
    } else if (newTheme === 'black') { // тёмная тема
        $('body').attr('data-theme', 'black');
        f.style.backgroundColor = "rgba(58, 58, 58, 0.4)";
        f.style.color = "black";
        f.style.backgroundImage = 'url("static/NightBackroundBlur.jpg")';
        f.style.color = "lightgray";
        MI.src = "static/Тёмный безымянный.png"
        p.style.backgroundImage = 'url("static/Night Backround.jpg")';
        E[0].style.backgroundColor = 'rgb(100, 100, 100, 0)'
        for (const item of btnList) {
            item.style.backgroundColor = 'grey';
        }
        for (const item of inputList) {
            item.style.backgroundColor = 'darkgray';
        }
        if ($('select').length > 0)
            $('select').css('backgroundColor', 'darkgray');
    }
}

function getTheme() {
    console.log('setThemeFunction in JS')
    $.ajax({
        url: '/getTheme',
        method: 'get',
        success: function (res) {
            plane1(res.newTheme);
            return res.newTheme;
        }
    });
}

function setTheme() {
    let newTheme = $('body').attr('data-theme') === 'black' ? 'white' : 'black';
    $.ajax({
        url: '/setTheme',
        data: JSON.stringify({'newTheme': newTheme}),
        dataType: 'json',
        contentType: 'application/json;charset=UTF-8',
        method: 'post',
        success: function (res) {
            plane1(newTheme)
        }
    })
}

getTheme();