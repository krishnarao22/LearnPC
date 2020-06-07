function validate() {
    var email = document.forms["signUpForm"]["email"].value;
    var username = document.forms["signUpForm"]["username"].value;
    var pw = document.forms["signUpForm"]["password"].value;
    var pwConfirm = document.forms["signUpForm"]["pwConfirm"].value;

    var numCount = 0;
    var letCount = 0;

    function isLetter(c) {
        return c.toLowerCase() != c.toUpperCase();
    }

    function isNum(c) {
        return c >= '0' && c <= '9'
    }

    var letExists = false;
    var numExists = false;

    function checkForLetAndNum() {
        
        if(pw.length < 2)
        {
            return false;
        }

        for(var i = 0; i < pw.length; i++)
        {
            if(isLetter(pw.charAt(i)))
                letExists = true;
            else if(isNum(pw.charAt(i)))
                numExists = true;
            
            if(letExists && numExists)
                break;
        }

        return letExists && numExists;
    }

    if(email == "" || username  == "" || pw == "" || pwConfirm == "")
    {
        alert("One or more fields are empty!")
        return false;
    }

    else if(pw != pwConfirm)
    {
        alert("Passwords do not match!");
        return false;
    }

    else if(pw.length < 8)
    {
        alert("Your password is too short!");
        return false;
    }

    else if(!checkForLetAndNum())
    {
        alert("Your password must contain letters and numbers!");
        return false;
    }

    return true;
} 