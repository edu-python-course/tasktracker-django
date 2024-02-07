const getCookie = (name) => {
    let value = null
    if (!document.cookie && document.cookie === "") return
    let cookies = document.cookie.split(";")
    for (const element of cookies) {
        let cookie = element.trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
            value = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
    }

    return value
}
