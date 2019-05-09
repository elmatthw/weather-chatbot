var idCounter = 0;
function bot(){
    let form = document.forms["myform"];
        let user_query = form.elements["user_query"].value;
        let request = new XMLHttpRequest();
        request.open("POST", "/post", true);
        request.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
        request.addEventListener("load", function () {
             let received = JSON.parse(request.response);
             /*console.log(typeof $(".response").attr("id"));*/
             var userMessage = $("<div class='request'></div>").attr("id", idCounter).text(received.user_query);
             var botMessage = $("<div class='response'></div>").attr("id", idCounter+1).text(received.bot_response);;
             $("#"+idCounter+".response").after(userMessage, botMessage);
             $(".w3-input").val('');
             console.log(received.user_query, "-", received.bot_response);
            idCounter++;
        });
        request.send(JSON.stringify({query:user_query}));
}

$(document).keypress(function (event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        event.stopPropagation();
        bot();

    }
});