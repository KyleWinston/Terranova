 isName=false;
    name="newUser";
    var ready=false;
 $('button').click(function(event) {
        event.preventDefault();
        if($('input[name="act"]').val().slice(0,2)=="::"){
            $.ajax({
                url: '/chat/',
                datatype: "application/json; charset=utf-8",
                data: {value:$('input[name="act"]').val(), user:name},
                type: 'GET',
                success: function(response) {
                    $('input[name="act"]').val('');

                },
                error: function(error) {
                    console.log(error);
                }
            });
        }else if($('input[name="act"]').val().slice(0,2)!= "" && ready==false) {
            if(!isName){
            name = $('input[name="act"]').val();
            isName=true;
            }
            $.ajax({
                url: '/load/',
                datatype: "application/json; charset=utf-8",
                data: {value:$('input[name="act"]').val(), ID:name},
                type: 'GET',
                success: function(response) {
                    $('input[name="act"]').val('');
                    $('#question').html(response.result);
                    console.log("success");
                    console.log(response.result);
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }else if ($('#question').text()=="Ready! Press >> to begin." || ready==true){
            if($('#question').text()=="Ready! Press >> to begin."){
                val = "start";
            }else{
                val = $('input[name="act"]').val();
            }
         $.ajax({
                url: '/move/',
                datatype: "application/json; charset=utf-8",
                data: {value:val, ID:name},
                type: 'GET',
                success: function(response) {
                    $('input[name="act"]').val('');
                    $('#question').html(response.result);
                    clearInterval(interval);
                    ready=true;
                    console.log("success");
                    console.log(response.result);
                },
                error: function(error) {
                    console.log(error);
            }
        });
    }
});
setInterval(function(){
    $.ajax({
            url: '/chat/',
            datatype: "application/json; charset=utf-8",
            data: {value:"getChat", user:name},
            type: 'GET',
            success: function(response) {
                total = "";
                for(var i=0; i<response.result.length; i++){
                    total = total + response.result[i] + "<br>";
                }

                $('#chat').html(total);
                console.log(total);
            },
            error: function(error) {
                console.log(error);
        }
    });
}, 2000);


var interval = setInterval(function(){

        $.ajax({
            url: '/check/',
            datatype: "application/json; charset=utf-8",
            data: {value:"checking if ready", user:name},
            type: 'GET',
            success: function(response) {
            if(response.header=="ok"){
                $('#question').html(response.result);
                }else{
                }
            },
            error: function(error) {
                console.log(error);
        }
    });
},5000);


setInterval(function(){

        $.ajax({
            url: '/event/',
            datatype: "application/json; charset=utf-8",
            data: {ID:name},
            type: 'GET',
            success: function(response) {
                $('#event').html(response.result);
                console.log(response.header);
            },
            error: function(error) {
                console.log(error);
        }
    });
},300);



