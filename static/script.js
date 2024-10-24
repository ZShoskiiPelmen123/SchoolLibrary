document.getElementById("a").addEventListener("click", () => {
    $('.main').hide()
    $('#main1').show()
    console.log($(this)[0])
    document.getElementById("a").style.backgroundColor = "rgb(143, 154, 163)";
    document.getElementById("b").style.backgroundColor = "white";
    document.getElementById("c").style.backgroundColor = "white";
    document.getElementById("d").style.backgroundColor = "white";
    document.getElementById("e").style.backgroundColor = "white";
    document.getElementById("f").style.backgroundColor = "white";
    document.getElementById("z").style.backgroundColor = "white";
});

document.getElementById("b").addEventListener("click", () => {
    $('.main').hide()
    $('#main2').show()
    document.getElementById("a").style.backgroundColor = "white";
    document.getElementById("b").style.backgroundColor = "rgb(143, 154, 163)";
    document.getElementById("c").style.backgroundColor = "white";
    document.getElementById("d").style.backgroundColor = "white";
    document.getElementById("e").style.backgroundColor = "white";
    document.getElementById("f").style.backgroundColor = "white";
    document.getElementById("z").style.backgroundColor = "white";
});

document.getElementById("c").addEventListener("click", () => {
    $('.main').hide()
    $('#main3').show()
    document.getElementById("a").style.backgroundColor = "white";
    document.getElementById("b").style.backgroundColor = "white";
    document.getElementById("c").style.backgroundColor = "rgb(143, 154, 163)";
    document.getElementById("d").style.backgroundColor = "white";
    document.getElementById("e").style.backgroundColor = "white";
    document.getElementById("f").style.backgroundColor = "white";
    document.getElementById("z").style.backgroundColor = "white";
});

document.getElementById("d").addEventListener("click", () => {
    $('.main').hide()
    $('#main4').show()
    document.getElementById("a").style.backgroundColor = "white";
    document.getElementById("b").style.backgroundColor = "white";
    document.getElementById("c").style.backgroundColor = "white";
    document.getElementById("d").style.backgroundColor = "rgb(143, 154, 163)";
    document.getElementById("e").style.backgroundColor = "white";
    document.getElementById("f").style.backgroundColor = "white";
    document.getElementById("z").style.backgroundColor = "white";
});

document.getElementById("e").addEventListener("click", () => {
    $('.main').hide()
    $('#main5').show()
    document.getElementById("a").style.backgroundColor = "white";
    document.getElementById("b").style.backgroundColor = "white";
    document.getElementById("c").style.backgroundColor = "white";
    document.getElementById("d").style.backgroundColor = "white";
    document.getElementById("e").style.backgroundColor = "rgb(143, 154, 163)";
    document.getElementById("f").style.backgroundColor = "white";
    document.getElementById("z").style.backgroundColor = "white";
});

document.getElementById("f").addEventListener("click", () => {
    $('.main').hide()
    $('#main6').show()
    document.getElementById("a").style.backgroundColor = "white";
    document.getElementById("b").style.backgroundColor = "white";
    document.getElementById("c").style.backgroundColor = "white";
    document.getElementById("d").style.backgroundColor = "white";
    document.getElementById("e").style.backgroundColor = "white";
    document.getElementById("f").style.backgroundColor = "rgb(143, 154, 163)";
    document.getElementById("z").style.backgroundColor = "white";
});

document.getElementById("z").addEventListener("click", () => {
    $('.main').hide()
    $('#main7').show()
    document.getElementById("a").style.backgroundColor = "white";
    document.getElementById("b").style.backgroundColor = "white";
    document.getElementById("c").style.backgroundColor = "white";
    document.getElementById("d").style.backgroundColor = "white";
    document.getElementById("e").style.backgroundColor = "white";
    document.getElementById("f").style.backgroundColor = "white";
    document.getElementById("z").style.backgroundColor = "rgb(143, 154, 163)";
});

function getKlass(tn) {
    $.ajax({
        url: '/getKlass',
        data: {teacher_name: tn},
        method: 'get',
        success: function (res) {
            $('#tbodyStud tr').remove();
            for (let i = 0; i < res.length; i++) {
                $('#tbodyStud').append("<tr><td>" + res[i].name + "</td><td>" + res[i].last_name + "</td><td>" +
                    res[i].books_count + "</td><td></td></tr>");
                if (res[i].books_count > 0) {
                    $('#tbodyStud td:last').append("<table class='innerTable' border-color='black' border='1'>" +
                        "<tbody></tbody></table>")
                    for (let j = 0; j < res[i].books.length; j++) {
                        console.log(res[i].books[j]);
                        $('.innerTable:last tbody').append("<tr><td>" + res[i].books[j].author + "</td><td>" +
                            res[i].books[j].title + "</td></tr>")
                    }
                }
            }
        }
    });
}
