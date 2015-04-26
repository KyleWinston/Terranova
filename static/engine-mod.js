$('button').click(function(event) {
    event.preventDefault();
if($('input[name="act"]').val().slice(0,2)=="::"){
            $.ajax({
            url: '/chat/',
            datatype: "application/json; charset=utf-8",
            data: {value:$('input[name="act"]').val(), user:"moderator"},
            type: 'GET',
            success: function(response) {
                $('input[name="act"]').val('');
            },
            error: function(error) {
                console.log(error);
            }
        });
    } else if($('input[name="act"]').val()==""){
            $('#question').html("loading world");
            $.ajax({
            url: '/mod/',
            datatype: "application/json; charset=utf-8",
            data: {value:"go"},
            type: 'GET',
            success: function(response) {
                $('input[name="act"]').val('');
                console.log(response.result);
            },
            error: function(error) {
                console.log(error);
            }
        });
    } else if ($('input[name="act"]').val()=="finish"){
        $.ajax({
            url: '/finish/',
            datatype: "application/json; charset=utf-8",
            data: {value:"done"},
            type: 'GET',
            success: function(response) {
                $('input[name="act"]').val('');
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
        setInterval(function(){
        $.ajax({
            url: '/player/',
            datatype: "application/json; charset=utf-8",
            data: {value:"players"},
            type: 'GET',
            success: function(response) {
                $('#players').html(response.result)
                console.log("success");
                console.log(response.result);
            },
            error: function(error) {
                console.log(error);
            }
        });
},3000);