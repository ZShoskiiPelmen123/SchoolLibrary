let initEvents = function() {
    menuitem_list = document.getElementsByClassName('menuitem');
    for (const el of menuitem_list) {
        el.addEventListener("click", (e) => {
           for (const el of document.getElementsByClassName('main'))
               el.style.display = el.dataset.id === e.target.dataset.id ? "flex" : "none";
            for (const el of document.getElementsByClassName('menuitem'))
                el.style.backgroundColor = "white"
            e.target.style.backgroundColor = "rgb(143, 154, 163)";
        });
    }
}

function getKlass() {
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
                        $('.innerTable:last tbody').append("<tr><td>" + res[i].books[j].author + "</td><td>" +
                            res[i].books[j].title + "</td></tr>")
                    }
                }
            }
        }
    });
}

function bookBooking(book_id) {
    $.ajax({
        url: '/bb',
        data: JSON.stringify({book_id: book_id}),
        datatype: JSON,
        contentType: 'application/json;charset=UTF-8',
        method: 'post',
        success: function (res) {
            $('#book'+book_id).attr("disabled", true);
        },
        error: function (res) {
            alert("Книга недоступна")
        }
    });
}

function logout() {
    window.location.href = '/Kvass53'
}

function disableBooked() {
    for (const el of document.getElementsByClassName('bbb'))
        if (el.dataset.userid !== "None")
            el.setAttribute('disabled', 'disabled')
}

initEvents();
disableBooked();