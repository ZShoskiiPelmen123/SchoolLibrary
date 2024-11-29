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

function getMyBooks() {
    $.ajax({
        url: '/getMyBooks',
        method: 'get',
        success: function (res) {
            for (let i = 0; i < res.length; i++) {
                $('#tableMyBooks').append('<tr>\n' +
                    '                        <td>' + res[i].title + '</td>\n' +
                    '                        <td>' + res[i].author + '</td>\n' +
                    '                        <td>' + res[i].info + '</td>\n' +
                    '                    </tr>');
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
            $('#book'+book_id)[0].innerText = "Отменить";
            $('#book'+book_id)[0].removeAttribute('onClick');
            $('#book'+book_id).off('click');
            $('#book'+book_id).on('click', function() {cancelBookBooking(book_id)});
        },
        error: function (res) {
            alert("Книга недоступна")
        }
    });
}

function cancelBookBooking(book_id) {
    $.ajax({
        url: '/cb',
        data: JSON.stringify({book_id: book_id}),
        datatype: JSON,
        contentType: 'application/json;charset=UTF-8',
        method: 'post',
        success: function (res) {
            $('#book'+book_id)[0].innerText = "Забронировать";
            $('#book'+book_id)[0].removeAttribute('onClick');
            $('#book'+book_id).off('click');
            $('#book'+book_id).on('click', function() {bookBooking(book_id)});
        }
    });
}

function giveBook(book_id) {
    $.ajax({
        url: '/gb',
        data: JSON.stringify({book_id: book_id}),
        datatype: JSON,
        contentType: 'application/json;charset=UTF-8',
        method: 'post',
        success: function (res) {
            // $('#book'+book_id).attr("disabled", true);
            $('#book'+book_id)[0].innerText = "Вернуть";
            $('#book'+book_id)[0].removeAttribute('onClick');
            $('#book'+book_id).off('click');
            $('#book'+book_id).on('click', function() {takeBook(book_id)});
        }
    });
}

function takeBook(book_id) {
    $.ajax({
        url: '/tb',
        data: JSON.stringify({book_id: book_id}),
        datatype: JSON,
        contentType: 'application/json;charset=UTF-8',
        method: 'post',
        success: function (res) {
            $('#book'+book_id).attr("disabled", true);
            $('#book'+book_id)[0].innerText = "Доступна";
            $('#book'+book_id)[0].removeAttribute('onClick');
        }
    });
}

function logout() {
    window.location.href = '/Kvass53'
}

function disableBooked() {
    let userid = null
    $.ajax({
        url: '/getCurrentUserId',
        method: 'get',
        success: function (res) {
            for (const el of document.getElementsByClassName('bbb')) {
                if (el.dataset.userid !== "None" && res.userTypeId === 1) {
                    if (Number(el.dataset.userid) === res.userId) { // моя книга
                        if (Number(el.dataset.bookstatusid) === 2)
                            el.innerText = 'Отменить'
                    } else { // чужая книга
                        el.setAttribute('disabled', 'disabled')
                        if (Number(el.dataset.bookstatusid) === 2)
                            el.innerText = 'Забронирована'
                    }
                }
            }
        }
    });
}


initEvents();
disableBooked();