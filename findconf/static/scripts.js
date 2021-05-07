//  Первая страница
function newCity() {
    const country = document.getElementById("country")
    for (let i of country) {
        if (i.selected === true) {
            const value = i.value
            updateCity(value);
        }
    }
}

function updateCity(value) {
    const xhr = new XMLHttpRequest()
    xhr.open('GET', '/get_city/?Id=' + value, false)
    xhr.send()
    const city = document.getElementById("city")
    if (xhr.responseText !== '') {
        const raise = JSON.parse(xhr.responseText)
        for (let i of city) {
            if (i.value === '') {
                i.hidden = true
                i.selected = true
            } else {
                const buf = Number.parseInt(i.value)
                i.hidden = raise.indexOf(buf) === -1;
            }
        }
    } else {
        for (let i of city) {
            if (i.value === '') {
                i.hidden = true
                i.selected = true
            } else {
                i.hidden = true;
            }
        }
    }
}
//    Вторая страница
function load_page() {
    const URL = document.URL
    const index = URL.indexOf('sear')
    const new_url = URL.slice(0, index) + 'search' + URL.slice(index + 4)
    const xhr = new XMLHttpRequest()
    xhr.open('GET', new_url, false)
    xhr.onreadystatechange = function () {
        const heas = document.getElementById('heas')
        heas.remove()
        console.log('yeee')
        document.write(xhr.responseText)
    }
    xhr.send()
    console.log(xhr.readyState)
}

//

