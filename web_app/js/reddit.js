let backend_server_address = "http://127.0.0.1:5000/"

window.onload = function(){
    update_for_search_type()
};

function update_for_search_type(){
    // changes needed on change of the Subreddit search and username search options
    let current_selection = document.getElementById("search_select").value
    switch (current_selection){
        case "subreddit":
            document.getElementById("name_input").placeholder = "enter subreddit name..."
            document.getElementById("name_input").title = "i.e enter 'ukpolitics' for r/ukpolitics"
            document.getElementById("sort_select_html").hidden = false
            document.getElementById("num_posts_html").hidden = false
            document.getElementById("all_replies_html").hidden = false
            document.getElementById("num_posts_from_user_html").hidden = true
            document.getElementById("username_encrypt_html").hidden = true
            break
        case "username":
            document.getElementById("name_input").placeholder = "enter a reddit username..."
            document.getElementById("name_input").title = "i.e your reddit username"
            document.getElementById("sort_select_html").hidden = true
            document.getElementById("num_posts_html").hidden = true
            document.getElementById("all_replies_html").hidden = true
            document.getElementById("num_posts_from_user_html").hidden = false
            document.getElementById("username_encrypt_html").hidden = false
            break
        default:
            document.getElementById("name_input").placeholder = "enter name ..."
            break
    }
}

function check_input_for_errors(){
    // checks all the input fields for errors
    let errors = false;
    let reddit_name = document.getElementById("name_input").value;
    if (reddit_name == null || reddit_name === "") {
        alert("Please enter a value in the Search field");
        errors = true
    }
    let current_selection = document.getElementById("search_select").value;
    if (current_selection === "subreddit") {
        let num_posts = document.getElementById("no_of_posts").value;
            if (num_posts == null || num_posts === "") {
                alert("Please enter a number in the Number of Posts field");
                errors = true
            } else if (num_posts < 1 || num_posts > 100) {
                alert("Please enter a number between 1-100 in the Number of Posts field");
                errors = true
            }
    } else if (current_selection === "username") {
        let num_posts = document.getElementById("no_of_posts_from_user").value;
            if (num_posts == null || num_posts === "") {
                alert("Please enter a number in the Number of Comments field");
                errors = true
            } else if (num_posts < 0 || num_posts > 10000) {
                alert("Please enter a number between 1-10000 in the Number of Comments field");
                errors = true
            }
    }
    return errors
}

function get_all_data_fields(){
    // return a json string for all the data inputted on the form
    let name = document.getElementById("name_input").value
    let num_posts = document.getElementById("no_of_posts").value
    let sort_order = document.getElementById("sort_select").value
    let get_all_replies = document.getElementById("nested_replies_checkbox").checked
    let num_comments = document.getElementById("no_of_posts_from_user").value
    let encrypted_username = document.getElementById("username_encrypted_checkbox").checked

    return JSON.stringify({
        "name": name,
        "sort_order": sort_order,
        "num_posts": num_posts,
        "all_replies_option": get_all_replies,
        "num_comments" : num_comments,
        "encrypted_username" : encrypted_username
    })
}

function get_posts(){
    // the function for the get posts button, sends the get request to the backend api with the specified parameters
    if (!check_input_for_errors()) {
        let search_type = document.getElementById("search_select").value
        let request_url = backend_server_address + "get_comments_by_" + search_type

        $.ajax({
            type: "POST",
            url: request_url,
            contentType: "application/json",
            async: false,
            data: get_all_data_fields(),

            success: function (success_data, _textStatus, _jqXHR_obj) {
                show_success_status_msg("Comments retrieved successfully and has been saved")
                console.log(success_data)
            },
            error: function (jqXHR_obj, textStatus, errorThrown) {
                show_danger_status_msg("Error Encountered when fetching comments!! Please check the console logs in the backend server for more information")
                console.log("Error!!!")
                console.log(jqXHR_obj)
                console.log(textStatus)
                console.log(errorThrown)
            },
        });
    }
}

function view_comments(){
    // sends the 'view comments' request to the backend api and displays the results in a table
    if (!check_input_for_errors()){
        let search_type = document.getElementById("search_select").value
        let request_url = backend_server_address + "view_comments_" + search_type

        $.ajax({
            type: "POST",
            url: request_url,
            contentType: "application/json",
            async: false,
            data: get_all_data_fields(),

            success: function (success_data, _textStatus, _jqXHR_obj) {
                if (success_data.comments_list){
                    console.log(success_data)
                    create_comments_table(success_data.fields, success_data.comments_list)
                } else {
                    show_danger_status_msg("Error please generate the files for the comments using the 1st button")
                }
            },
            error: function (jqXHR_obj, textStatus, errorThrown) {
                show_danger_status_msg("Error Encountered!! Please check the console logs in the backend server for more information")
                console.log("Error!!!")
                console.log(jqXHR_obj)
                console.log(textStatus)
                console.log(errorThrown)
            },
        });
    }
}

function load_visualisations(){
    // when the analyse comments button is pressed, send the request to the backend api and load the results into a table
    if (!check_input_for_errors()){
        let search_type = document.getElementById("search_select").value
        let request_url = backend_server_address + "analyse_comments_" + search_type

        $.ajax({
            type: "POST",
            url: request_url,
            contentType: "application/json",
            async: false,
            data: get_all_data_fields(),

            success: function (success_data, _textStatus, _jqXHR_obj) {
                if (success_data.comments_list){
                    console.log(success_data)
                    create_results_table(success_data.fields, success_data.comments_list)
                } else{
                    show_danger_status_msg("Error please generate the files for the comments using the 1st button")
                }
            },
            error: function (jqXHR_obj, textStatus, errorThrown) {
                show_danger_status_msg("Error Encountered!! Please check the console logs in the backend server for more information")
                console.log("Error!!!")
                console.log(jqXHR_obj)
                console.log(textStatus)
                console.log(errorThrown)
            },
        });
    }
}

function show_success_status_msg(msg) {
    let div = document.getElementById("results_div");
    div.innerHTML = "<div class=\"alert alert-success\" role=\"alert\">\n" + msg + "</div>"
}

function show_danger_status_msg(msg) {
    let div = document.getElementById("results_div");
    div.innerHTML = "<div class=\"alert alert-danger\" role=\"alert\">" + msg + "</div>"
}

function create_comments_table(fields, comments_list){
    let div = document.getElementById("results_div");
    div.innerHTML = ""
    var tmp_table_html = "<div class=\"table-responsive\">";
    tmp_table_html += "<table class=\"table table-striped table-bordered table-hover table-condensed table-responsive\">"
    //add headings for columns
    tmp_table_html += "<thead class=\"table-dark\"><tr>"
    tmp_table_html += "<th scope=\"col\">" + fields[1] + "</th><th scope=\"col\">" + fields[0] + "</th>"
    tmp_table_html += "</tr></thead>"
    //add data rows to table
    tmp_table_html += "<tbody>"
    for (i = 0; i < comments_list.length; i++){
        tmp_table_html += "<tr><th scope=\"row\">"
        tmp_table_html += comments_list[i][1]
        tmp_table_html += "</th><th>"
        tmp_table_html += comments_list[i][0]
        tmp_table_html += "</th></tr>"
    }
    tmp_table_html += "</tbody></table></div>";
    div.innerHTML = tmp_table_html
}

function create_results_table(fields, comments_list){
    let div = document.getElementById("results_div");
    div.innerHTML = ""
    var tmp_table_html = "<div class=\"table-responsive\">";
    tmp_table_html += "<table class=\"table table-striped table-bordered table-hover table-condensed table-responsive\">"
    //add headings for columns
    tmp_table_html += "<thead class=\"table-dark\"><tr>"
    tmp_table_html += "<th scope=\"col\">" + fields[0] + "</th><th scope=\"col\">" + fields[1] + "</th><th scope=\"col\">" + fields[2] + "</th>"
    tmp_table_html += "</tr></thead>"
    //add data rows to table
    tmp_table_html += "<tbody>"
    for (i = 0; i < comments_list.length; i++){
        tmp_table_html += "<tr><th scope=\"row\">"
        tmp_table_html += comments_list[i][0]
        tmp_table_html += "</th><th>"
        tmp_table_html += comments_list[i][1]
        tmp_table_html += "</th><th>"
        tmp_table_html += comments_list[i][2]
        tmp_table_html += "</th></tr>"
    }
    tmp_table_html += "</tbody></table></div>";
    div.innerHTML = tmp_table_html
}
