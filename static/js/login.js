function validate() {
    var email = document.forms["loginForm"]["email"].value;
    var pw = document.forms["loginForm"]["password"].value;

    if(email.length == 0 || pw.length == 0)
    {
        alert("One or more fields are empty!");
        return false;
    }

    return true;
}

