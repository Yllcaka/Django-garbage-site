function animateValue(id, start, end, duration, cnt, item = "") {
    var range = end - start;
    var current = start;
    var increment = end > start ? cnt : -1;
    var stepTime = Math.abs(Math.floor(duration / range));
    var obj = document.getElementById(id);
    var timer = setInterval(function () {
        current += increment;
        obj.innerHTML = current;
        if (current >= end) {
            clearInterval(timer);
        }
        obj.innerHTML += item
    }, stepTime);
}
$("#carding").waypoint(function () {
    if ($("#count1").is(":empty")) {
        animateValue("count1", 0, 1299, 1, 3);
        animateValue("count2", 0, 120, 500, 1, "+")
        animateValue("count3", 0, 3, 800, 1);

    }

}, {
    offset: '100%'
});