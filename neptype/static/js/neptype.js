function strcompare(str1, str2){
    error = false;
    if(str1.length>str2.length){
        error = true;
    } else{
        for(i=0;i<str1.length;i++){
            if(str1[i] != str2[i]){
                error = true;
                break;
            }
        }
    }
    return error;
}
$(document).ready(function(){
    var index = 0;
    var mistake;
    var sometext; // = "this is pramod maharjan."
    var textarray;// = sometext.split(" ");
<<<<<<< HEAD
    var writestatus = false;
    var start_time;

    $(window).load(function(){
        $("#demo").html("Wonder how fast can you type?<br>Find out now !!!<br>Click on start");
    });

=======
    var start_time;
    var user_speed;

    //Load the text from database
>>>>>>> 37c339a605e48c23a3f69e3a9b297d9507e67a2b
    $("#start").click(function(){
        $.ajax({
            type: "GET",
            url: "/neptype/ajax/load_text/",
            success: function(data){
<<<<<<< HEAD
                sometext = data;
=======
                user_speed = data[0];
                sometext = data[1];
>>>>>>> 37c339a605e48c23a3f69e3a9b297d9507e67a2b
                textarray = sometext.split(" "); 
                $("#demo").text(sometext);
                index = 0;
                $("#textbox").prop('disabled', true);
                $("#speed").text("5");
<<<<<<< HEAD
=======
                $("#result").text("");
                $("#record").text("");
>>>>>>> 37c339a605e48c23a3f69e3a9b297d9507e67a2b
                setTimeout(function(){ $("#speed").text("4"); }, 1000);
                setTimeout(function(){ $("#speed").text("3"); }, 2000);
                setTimeout(function(){ $("#speed").text("2"); }, 3000);
                setTimeout(function(){ $("#speed").text("1"); }, 4000);
                setTimeout(function(){ 
<<<<<<< HEAD
                    writestatus = true;
=======
>>>>>>> 37c339a605e48c23a3f69e3a9b297d9507e67a2b
                    $("#textbox").prop('disabled', false);
                    $("#textbox").focus();
                    $("#speed").text("Go!");
                    start_time = new Date();
                }, 5000);


            }
        });

    });
<<<<<<< HEAD
    $("#textbox").keydown(function(e){
        document.write('press' + e.keyCode);
        var numwords = textarray.length;
        var x = document.getElementById("textbox");
        var z = x.value.substr(-1,1);
        var key = z.charCodeAt(0);
        if(writestatus == false){
            x.value ="";
        }
        else if(key == 32){
            var temp = x.value.slice(0,-1);
=======

    //Check the text input 
    $("#textbox").on('input', function(){
        var numwords = textarray.length;
        var x = document.getElementById("textbox");
        var txt = $(this).val();
        var z = txt.substr(-1,1);
        var key = z.charCodeAt(0);
        if(key == 32){
            var temp = txt.slice(0,-1);
>>>>>>> 37c339a605e48c23a3f69e3a9b297d9507e67a2b
            mistake = strcompare(temp, textarray[index]);
            if(!mistake && temp.length == textarray[index].length){
                x.value = "";
                index++;
                var right_now = new Date();
                var speed = parseInt(index*1000*60/(right_now - start_time));
                $("#speed").text(speed);

                index = index % numwords;
            }
            else{ mistake = true;
            }
        }
        else if(index == numwords -1){
<<<<<<< HEAD
            if(!mistake && x.value.length == textarray[index].length){
=======
            mistake = strcompare(txt, textarray[index]);
            if(!mistake && txt.length == textarray[index].length){
>>>>>>> 37c339a605e48c23a3f69e3a9b297d9507e67a2b
                x.value = "";
                $("#textbox").prop('disabled', true);
                var right_now = new Date();
                var speed = parseInt(numwords*1000*60/(right_now - start_time));
                $("#speed").text(speed);
<<<<<<< HEAD
                $("#result").text("Your speed is "+speed+" W/m");
                $("#start").text("Race Again");
            }
        }
        else{
            mistake  = strcompare(x.value, textarray[index])
        }

=======
                $("#result").text("Your speed is "+speed+" Wpm");
                $("#start").text("Race Again");
                if(speed > user_speed){
                    //ajax function to update max speed
                    $.ajax({
                        type: "POST",
                        url: "/neptype/ajax/update_speed/",
                        data: {'new_speed' : speed},
                        dataType: "json",
                        success: function(data){
                            $("#max_speed").text("Your max. speed : "+speed+" Wpm");
                            $("#record").text("You've beaten your own highest score");

                        }
                    });
                }

            }
        }
        else{
            mistake  = strcompare(txt, textarray[index]);
        }
        //bold the current word
>>>>>>> 37c339a605e48c23a3f69e3a9b297d9507e67a2b
        $("#demo").text(" ");
        for(i=0;i< numwords;i++){
            if(i == index){
                $("#demo").append("<strong>" + textarray[i] + "</strong> ");
            } else{
                $("#demo").append(textarray[i]+ " ");
            }

        }
<<<<<<< HEAD
=======


        //display red color in mistyping
>>>>>>> 37c339a605e48c23a3f69e3a9b297d9507e67a2b
        if(mistake == true){
            $("#textbox").attr("style","color:#ff0000");
        }
        else{
            $("#textbox").attr("style","color:#000000");
        }
    });
<<<<<<< HEAD
=======
    // CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    }); 


>>>>>>> 37c339a605e48c23a3f69e3a9b297d9507e67a2b

});

