
$('body').on('click', '.chekker', function(){
	if ($(this).is(':checked')){
		$('#vvod').attr('type', 'text');
	} else {
		$('#vvod').attr('type', 'password');
	}
});

function plane1(newTheme) {
    let f = document.body;
    let MI = document.getElementById("Mewing");
    let E = document.getElementsByClassName("authForm");
    let p = document.getElementById("Kvass1");
    let Name = document.getElementById("Name")
    let Name1 = document.getElementById("Name1")
    let a = document.getElementById("Palka69");
    let b = document.getElementById("change_password");
    let c = document.getElementById("Text2");
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
        MI.style.backgroundImage = 'url("static/logo 1.png")';
        p.style.backgroundImage = 'url("static/DayBackround.png")';
        a.style.backgroundColor = 'rgb(190, 190, 190)';
        b.style.color = '#b9c1e9';
        c.style.color = '#0c2239';
        c.style.backgroundColor = 'rgba(256,256,256,20%)';
        Name.style.backgroundColor = "rgba(135, 177, 185, 0.4)";
        Name.style.color = "#0c2239";
        Name1.style.backgroundColor = "rgba(135, 177, 185, 0.4)";
        Name1.style.color = "#0c2239";

        E[0].style.backgroundColor = 'rgb(223, 223, 223, 0)';

        for (const item of btnList) {
            item.style.backgroundColor = 'white';
        }
        for (const item of inputList) {
            item.style.backgroundColor = 'white';
        }
        if ($('select').length > 0)
            $('select').css('backgroundColor', 'white');
    } else if (newTheme === 'black') { // тёмная тема
        $('body').attr('data-theme', 'black');
        f.style.backgroundColor = "rgba(58, 58, 58, 0.4)";
        f.style.color = "black";
        f.style.backgroundImage = 'url("static/NightBackroundBlur.jpg")';
        f.style.color = "lightgray";
        MI.style.backgroundImage = 'url("static/logo 2.png")';
        p.style.backgroundImage = 'url("static/NightBackround.png")';
        a.style.backgroundColor = 'rgb(66, 73, 86)';
        b.style.color = '#003aae';
        c.style.backgroundColor = "rgba(27, 26, 58, 0.6)";
        c.style.color = "rgb(145, 145 ,145)";
        E[0].style.backgroundColor = 'rgba(100, 100, 100, 0)'
        Name.style.backgroundColor = "rgba(27, 26, 58, 0.6)";
        Name.style.color = "rgb(145, 145 ,145)"
        Name1.style.backgroundColor = "rgba(27, 26, 58, 0.6)";
        Name1.style.color = "rgb(145, 145 ,145)"
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

