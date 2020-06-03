function checkFields() {
    if(document.getElementbyId('#emailInput').value == '')
    {
        alert('email is empty!')
        return false;
    }
    return true;
}