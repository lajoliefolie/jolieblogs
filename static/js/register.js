// Handles registration form
$(function() {
    //$('a#signin').bind('click', function() {
    $('form#register').submit(function(event){
        var vals = $( this ).serializeArray();
        event.preventDefault(); //Won't move forward with default false action. Not good for this. Return True/False from this JS!
    
        function findElement(vals, propName, propValue){
            for (var i=0; i < vals.length; i++)
                if (vals[i][propName] == propValue)
                    return vals[i];
            }
            var email = findElement(vals, "name", "returnEmail")["value"];
            var password1 = findElement(vals, "name", "returnPassword")["value"];
            var password2 = findElement(vals, "name", "confirmPassword")["value"];
            
            console.log(email + " " + password1 + " " + password2)
            
            $.getJSON("check", { //.get
            returnEmail: email,
            returnPassword: password1,
            confirmPassword: password2
            }, function (data) {
                console.log(data);
                if(data == "email_registered"){
                    console.log("Email registered error.");
                    inputPassword.value = '';
                    confPassword.value = '';
                    document.getElementById("register_message").innerHTML = "Email already registered.";
                }
                else if(data == "pw_match"){
                    console.log("Passwords don't match error.");
                    inputPassword.value = '';
                    confPassword.value = '';
                    document.getElementById("register_message").innerHTML = "Passwords do not match.";
                }
                else if(data == "valid_register"){
                    window.location = main_view;
                }
            });
    })
});