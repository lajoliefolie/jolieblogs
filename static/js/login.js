// Function which handles the logging in of users
$(function() {
    //$('a#signin').bind('click', function() {
    $('form#urllogin').submit(function(event){
        var vals = $( this ).serializeArray();
        event.preventDefault(); //Won't move forward with default false action. Not good for this. Return True/False from this JS!
    
        function findElement(vals, propName, propValue){
            for (var i=0; i < vals.length; i++)
                if (vals[i][propName] == propValue)
                    return vals[i];
            }
            var email = findElement(vals, "name", "returnEmail")["value"];
            var password = findElement(vals, "name", "returnPassword")["value"];
            
            console.log(email);
            console.log(password);
            
            $.getJSON("completed_js", {
            returnEmail: email,
            returnPassword: password
            }, function (data) {
                // console.log(data);
                if(data == "valid_login"){
                    // console.log("Valid! Woo!");
                    window.location = main_view
                }
                else if(data == "invalid_login"){
                    // console.log("Invalid! Nooooo!");
                    inputPassword.value = '';
                    document.getElementById("login_message").innerHTML = "Invalid email/password combination."
                    // $("login_message").load("Invalid email/password combination."); 
                }
            });
    })
});