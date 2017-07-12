
// Function to get all users for admin panel controls
// Should be done using Jinja2, like posts are, but this was done earlier
// To be refactored
$(document).ready(function(){
    $("button#get_users").on('click', 
    function(){
        $.getJSON("/admin/load_user_data", function(result){
            // console.log("Returned");
            
            $('table#user_data').empty();
            $('table#user_data').append("<tr class='table_header'> <th>User ID</th> <th>Home</th> <th>Signup Data</th> <th>Permissions</th> <th>Update Admin</th> <th>Delete User</th> </tr>");
            
            for(var i = 0; i<result.length; i++){
                
                var add_or_rem_admin = "Add Admin";
                var is_admin = "notadmin";
                // console.log(result[i][3]);
                // console.log(result[i][3].indexOf("admin"));
                if(result[i][3].indexOf("admin")!=-1){
                    //console.log(result[i][3]);
                    add_or_rem_admin = "Remove Admin";
                    is_admin = "admin";
                }
                
                $('table#user_data').append("<tr>" +
                                        "<td class='text_row'>" + result[i][0] + "</td>" +
                                        "<td class='text_row'>" + result[i][1] + "</td>" +
                                        "<td class='text_row'>" + result[i][2] + "</td>" +
                                        "<td class='text_row'>" + result[i][3] + "</td>" +
                                        "<td class='button_row'> <button class = 'btn admin_button' data-userid=" + result[i][0] + 
                                        " data-isadmin=" + is_admin + 
                                        " name='ltrContainer'>" + add_or_rem_admin + 
                                        "<td class='button_row'> <button class = 'btn delete_button' data-userid=" + result[i][0] + 
                                        " name='ltrContainer'>Delete User</button></td></tr>");
            }
        });
    }
    );
    // Inner button function call for updating admin permissions
    $('body').on('click', '.admin_button', function() {
        var user_id = $(this).attr('data-userid');
        var is_admin = $(this).attr('data-isadmin');
        // console.log(user_id);
        // console.log(is_admin);
        
        $.getJSON("/admin/update_admin", { //.get
            userid: user_id,
            isadmin: is_admin
            }, function(result){
                document.getElementById("get_users").click();
        });
        
    });
    
    // Inner button function call for deleting users
    $('body').on('click', '.delete_button', function() {
        var user_id = $(this).attr('data-userid');
        
        $.getJSON("/admin/delete_user", { //.get
            userid: user_id,
            }, function(result){
                if(result == "deleted_logout")
                     window.location="/login/logout"
                document.getElementById("get_users").click();
        });
        
    });
});

// $(document).ready(function()
// {   
//     $('.buttons').each(function(){
//         $(this).click(function(){
//             console.log("GOT ONE!");
//         });
        
//     // document.getElementById('textContainer').value += this.innerHTML;
//     // alert(this.innerHTML);
//     });
// });