let backend_server_address = "http://127.0.0.1:5000/"

window.onload = function(){
    update_search_box_hint()
};

var status_fade_out = function(){
  $("#status_msg_div").fadeOut().empty();
}

function update_search_box_hint(){
    let current_selection = document.getElementById("search_select").value
    switch (current_selection){
        case "subreddit":
            document.getElementById("name_input").placeholder = "enter subreddit name..."
            document.getElementById("name_input").title = "i.e enter 'ukpolitics' for r/ukpolitics"
            break
        case "username":
            document.getElementById("name_input").placeholder = "enter a reddit username..."
            document.getElementById("name_input").title = "i.e your reddit username"
            break
        default:
            document.getElementById("name_input").placeholder = "enter name ..."
            break
    }
}

function check_input_for_errors(){
    let errors = false;
    let num_posts = document.getElementById("no_of_posts").value
    let reddit_name = document.getElementById("name_input").value
    if (reddit_name == null || reddit_name == ""){
        alert("Please enter a value in the Search field");
        errors = true
    }
    else if (num_posts == null || num_posts == ""){
        alert("Please enter a number in the Number of Posts field");
        errors = true
    }
    else if (num_posts<1 || num_posts>100){
        alert("Please enter a number between 1-100 in the Number of Posts field");
        errors = true
    }
    return errors
}

function get_posts(){
    if (!check_input_for_errors()) {
        let search_type = document.getElementById("search_select").value
        let name = document.getElementById("name_input").value
        let num_posts = document.getElementById("no_of_posts").value
        let sort_order = document.getElementById("sort_select").value
        let get_all_replies = document.getElementById("nested_replies_checkbox").checked

        let request_json = JSON.stringify({
            "name": name,
            "num_posts": num_posts,
            "sort_order": sort_order,
            "all_replies_option": get_all_replies
        })
         let request_url = backend_server_address + "get_comments_by_" + search_type

        $.ajax({
            type: "POST",
            url: request_url,
            contentType: "application/json",
            async: false,
            data: request_json,

            success: function (success_data, textStatus, jqXHR_obj) {
                console.log(success_data)
            },
            error: function (jqXHR_obj, textStatus, errorThrown) {
                console.log("Error!!!")
                console.log(jqXHR_obj)
                console.log(textStatus)
                console.log(errorThrown)
            },
        });
    }
}

function view_comments(){
    if (!check_input_for_errors()){
        let name = document.getElementById("name_input").value
        let num_posts = document.getElementById("no_of_posts").value
        let sort_order = document.getElementById("sort_select").value

        let request_json = JSON.stringify({
            "name": name,
            "num_posts": num_posts,
            "sort_order": sort_order
        })
        let request_url = backend_server_address + "view_comments"

        $.ajax({
            type: "POST",
            url: request_url,
            contentType: "application/json",
            async: false,
            data: request_json,

            success: function (success_data, textStatus, jqXHR_obj) {
                console.log(success_data)
                console.log(success_data.comments_list)
                console.log(success_data.comments_list[0][0])


                create_table(success_data.comments_list)
            },
            error: function (jqXHR_obj, textStatus, errorThrown) {
                console.log("Error!!!")
                console.log(jqXHR_obj)
                console.log(textStatus)
                console.log(errorThrown)
            },
        });
    }
}

function load_visualisations(){
    if (!check_input_for_errors()){

    }
}

function create_table(comments_list){
    div = document.getElementById("comments_table");
    var tmp_table_html = "";
    tmp_table_html += "<table><thead><tr><th scope=\"col\">ID</th><th scope=\"col\">Comment</th> </tr></thead>"
    tmp_table_html += "<tbody>"
    for (i = 0; i < comments_list.length; i++){
        tmp_table_html += "<tr><th scope=\"row\">"
        tmp_table_html += comments_list[i][1]
        tmp_table_html += "</th><td>"
        tmp_table_html += comments_list[i][0]
        tmp_table_html += "</td></tr>"
    }
    tmp_table_html += "</tbody></table>";
    div.innerHTML = tmp_table_html
}



