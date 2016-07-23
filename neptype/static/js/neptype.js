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
    var start_time;

    $(window).load(function(){
        $("#demo").html("Wonder how fast can you type?<br>Find out now !!!<br>Click on start");
    });
    
    //Load the text from database
    $("#start").click(function(){
        $.ajax({
            type: "GET",
            url: "/neptype/ajax/load_text/",
            success: function(data){
                sometext = data;
                textarray = sometext.split(" "); 
                $("#demo").text(sometext);
                index = 0;
                $("#textbox").prop('disabled', true);
                $("#speed").text("5");
                setTimeout(function(){ $("#speed").text("4"); }, 1000);
                setTimeout(function(){ $("#speed").text("3"); }, 2000);
                setTimeout(function(){ $("#speed").text("2"); }, 3000);
                setTimeout(function(){ $("#speed").text("1"); }, 4000);
                setTimeout(function(){ 
                    $("#textbox").prop('disabled', false);
                    $("#textbox").focus();
                    $("#speed").text("Go!");
                    start_time = new Date();
                }, 5000);


            }
        });

    });
    //Check the text input 
    $("#textbox").on('input', function(){
        var numwords = textarray.length;
        var x = document.getElementById("textbox");
        var txt = $(this).val()
        var z = txt.substr(-1,1);
        var key = z.charCodeAt(0);
        if(key == 32){
            var temp = txt.slice(0,-1);
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
            mistake = strcompare(txt, textarray[index]);
            if(!mistake && txt.length == textarray[index].length){
                x.value = "";
                $("#textbox").prop('disabled', true);
                var right_now = new Date();
                var speed = parseInt(numwords*1000*60/(right_now - start_time));
                $("#speed").text(speed);
                $("#result").text("Your speed is "+speed+" W/m");
                $("#start").text("Race Again");
            }
        }
        else{
            mistake  = strcompare(txt, textarray[index]);
        }
        //bold the current word
        $("#demo").text(" ");
        for(i=0;i< numwords;i++){
            if(i == index){
                $("#demo").append("<strong>" + textarray[i] + "</strong> ");
            } else{
                $("#demo").append(textarray[i]+ " ");
            }

        }

        //display red color in mistyping
        if(mistake == true){
            $("#textbox").attr("style","color:#ff0000");
        }
        else{
            $("#textbox").attr("style","color:#000000");
        }
    });

});

