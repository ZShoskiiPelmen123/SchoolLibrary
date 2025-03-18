let initEvents = function() {
    let menuitem_list = document.getElementsByClassName('menuitem');
    for (const menuItem of menuitem_list) {
        menuItem.addEventListener("click", (e) => {
            // Дисплей главных элементов
            for (const mainItem of document.getElementsByClassName('main')) {
                mainItem.style.display = mainItem.dataset.id === e.target.dataset.id ? "flex" : "none";
            }

            // Сброс фона элементов меню
            for (const item of menuitem_list) {
                item.style.backgroundColor = "rgb(171,171,171)";
            }
            e.target.style.backgroundColor = "rgb(131, 134, 133)";
            let z = document.querySelector('#z');
            z.style.backgroundColor = "rgba(0,0,0,0)"
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
                    let $lastRow = $('#tbodyStud tr:last td:last');
                    $lastRow.append("<table class='innerTable' border='1'><tbody></tbody></table>");
                    for (let j = 0; j < res[i].books.length; j++) {
                        $('.innerTable:last tbody').append("<tr><td>" + res[i].books[j].author + "</td><td>" +
                            res[i].books[j].title + "</td></tr>");
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
            $('#tableMyBooks tr').remove(); // Очистка перед добавлением
            for (let i = 0; i < res.length; i++) {
                $('#tableMyBooks').append('<tr>\n' +
                    '    <td>' + res[i].title + '</td>\n' +
                    '    <td>' + res[i].author + '</td>\n' +
                    '    <td>' + res[i].info + '</td>\n' +
                    '</tr>');
            }
        }
    });
}

// Инициализация событий
initEvents();
function bookBooking(book_id) {
    $.ajax({
        url: '/bb',
        data: JSON.stringify({book_id: book_id}),
        datatype: JSON,
        contentType: 'application/json;charset=UTF-8',
        method: 'post',
        success: function (res) {
            let bid = $('#book'+book_id);
            bid[0].innerText = "Отменить";
            bid[0].removeAttribute('onClick');
            bid.off('click');
            bid.on('click', function() {cancelBookBooking(book_id)});
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
            let bid = $('#book'+book_id);
            bid[0].innerText = "Забронировать";
            bid[0].removeAttribute('onClick');
            bid.off('click');
            bid.on('click', function() {bookBooking(book_id)});
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
            let bid = $('#book'+book_id);
            bid[0].innerText = "Вернуть";
            bid[0].removeAttribute('onClick');
            bid.off('click');
            bid.on('click', function() {takeBook(book_id)});
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
            let bid = $('#book'+book_id);
            bid.attr("disabled", true);
            bid[0].innerText = "Доступна";
            bid[0].removeAttribute('onClick');
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


    let modal = document.getElementById("modal");
    let button = document.getElementById("menu");
    let closeBtn = document.getElementsByClassName("close1")[0];

    button.onclick = function () {
        modal.style.animation = "slideIn 0.5s forwards";
        modal.style.display = "block";


    }


    closeBtn.onclick = function() {
     modal.style.animation = "slideOut 0.5s forwards";

      setTimeout(function() {
        modal.style.animation = "";
        modal.style.display = "none";
     }, 500);
}


initEvents();
disableBooked();
