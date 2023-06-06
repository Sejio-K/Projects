
window.onload = function() {
    let button = document.getElementById("myButton");
    let countSpan = document.getElementById("count");
    let count = 0;

    button.addEventListener("click", function() {
        count++;
        countSpan.innerText = count.toString();
    });
};