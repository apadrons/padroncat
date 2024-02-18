document.addEventListener('DOMContentLoaded', function () {
    var menuBtn = document.getElementById('menuBtn');
    var menuContainer =document.getElementById('menuContainer');
    menuBtn.onclick = function(){

            menuContainer.classList.remove('invisible');
            menuBtn.classList.add('invisible');

    };
});