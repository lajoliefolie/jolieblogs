// Handles form for updating email
$(function() {
    //$('a#signin').bind('click', function() {
    $('form#update_email').submit(function(event){
        var vals = $( this ).serializeArray();
        event.preventDefault(); //Won't move forward with default false action. Not good for this. Return True/False from this JS!
    
        function findElement(vals, propName, propValue){
            for (var i=0; i < vals.length; i++)
                if (vals[i][propName] == propValue)
                    return vals[i];
            }
            var email = findElement(vals, "name", "returnEmail")["value"];
            var email2 = findElement(vals, "name", "returnConfEmail")["value"];
            var password = findElement(vals, "name", "returnPassword")["value"];
            
            $.getJSON("update_email_check", {
            returnEmail: email,
            returnConfEmail: email2,
            returnPassword: password
            }, function (data) {
                if(data == "password_fail"){
                    inputPassword.value = '';
                    document.getElementById("update_message").innerHTML = "Password is not correct.";
                }
                else if(data == "email_nomatch"){
                    inputPassword.value = '';
                    document.getElementById("update_message").innerHTML = "Emails do not match.";
                }
                else if(data == "email_used"){
                    inputPassword.value = '';
                    document.getElementById("update_message").innerHTML = "Email already in use.";
                }
                else if(data == "valid_update"){
                    inputPassword.value = '';
                    document.getElementById("update_message").innerHTML = "Email updated!";
                    window.location = "/";
                }
            });
    })
});

// Handles form for updating password
$(function() {
    $('form#update_password').submit(function(event){
        var vals = $( this ).serializeArray();
        event.preventDefault(); //Won't move forward with default false action. Not good for this. Return True/False from this JS!
    
        function findElement(vals, propName, propValue){
            for (var i=0; i < vals.length; i++)
                if (vals[i][propName] == propValue)
                    return vals[i];
            }
            var pw1T= findElement(vals, "name", "pw1")["value"];
            var pw2T = findElement(vals, "name", "pw2")["value"];
            var pwConfT = findElement(vals, "name", "returnPassword")["value"];
            
            console.log(pw1T);
            
            $.getJSON("update_password_check", {
            pw1: pw1T,
            pw2: pw2T,
            returnPassword: pwConfT
            }, function (data) {
                if(data == "password_fail"){
                    inputPassword.value = '';
                    document.getElementById("update_message").innerHTML = "Password is not correct.";
                }
                else if(data == "password_nomatch"){
                    inputPassword.value = '';
                    document.getElementById("update_message").innerHTML = "Emails do not match.";
                }
                else if(data == "valid_update"){
                    inputPassword.value = '';
                    document.getElementById("update_message").innerHTML = "Password updated!";
                    window.location = "/";
                }
            });
    })
});