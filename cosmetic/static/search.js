function enterSearch() {
    if(event.keyCode == 13){
        myFunction();  // 실행할 이벤트
    }
}
function myFunction() {
    var x = document.getElementById("text").value;
    window.location.href = "http://cybertramp.net/search/"+x;
}