function Greeting(id) {
    let koha = new Date;
    let stuff = "";
    if (koha.getHours() < 10)
        stuff = "Mirmengjesi Client i dashur";
    else if (koha.getHours() < 18 && koha.getHours() > 10)
        stuff = "Mirdita Client i dashur";
    else if (koha.getHours() > 18 || koha.getHours() < 5)
        stuff = "Mirmbrema Client i dashur";
    for (let i = 0; i < id.length; i++)
        id[i].innerHTML = stuff;
}
Greeting(document.getElementsByClassName("greeting"))