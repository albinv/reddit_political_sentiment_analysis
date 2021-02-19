window.onload = function(){
    update_search_box_hint()
};

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
    console.log(num_posts)
    return errors
}

function get_post(){
    if (!check_input_for_errors()){

    }
}

function view_comments(){
    if (!check_input_for_errors()){

    }
}

function load_visualisations(){
    if (!check_input_for_errors()){

    }
}







