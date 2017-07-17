// Handles creating of posts; once a post is created, update the post viewing field
$(function() {
    //$('a#signin').bind('click', function() {
    $('form#make_post').submit(function(event){
        var vals = $( this ).serializeArray();
        event.preventDefault(); //Won't move forward with default false action. Not good for this. Return True/False from this JS!
        
        function findElement(vals, propName, propValue){
            for (var i=0; i < vals.length; i++){
                if (vals[i][propName] == propValue)
                    return vals[i];
            }
        }
        
       
        var title1 = findElement(vals, "name", "title")["value"];
        var text1 = findElement(vals,  "name", "text")["value"];
            
            $.getJSON("/posts/post_post", { //.get
            title: title1,
            text: text1 
            }, function (data) {
                if(data == "valid_post"){
                    title.value = '';
                    text.value = '';
                    if(location.href.includes("admin") || location.href.includes("profile")) {
                        var url_string = location.href;
                        var url = new URL(url_string);
                        var uid = url.searchParams.get("uid");
                        $.get( "/posts/get_user_posts?uid="+uid, function( data ) {
                            $( "#get_posts" ).html( data );
                        });
                    }
                    else{
                        $.get( "/posts/get_all_posts", function( data ) {
                            $( "#get_posts" ).html( data );
                        });
                    }
                }
            });
    })
});