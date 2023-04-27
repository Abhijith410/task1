function RegValidate(){
    var fname_error = document.getElementById('fnamerror');
    var fname = document.getElementById('FName').value;
    var lname_error = document.getElementById('lnamerror');
    var lname = document.getElementById('LName').value;
    var contact_error = document.getElementById('addresserror_');
    var contact = document.getElementById('address').value;
    var email_error = document.getElementById('emailerror_');
    var email = document.getElementById('email').value;
    var username_error = document.getElementById('usererror_');
    var username = document.getElementById('user_name').value;
    var pass_error = document.getElementById('passerror_');
    var pass = document.getElementById('pass_word').value;
    var confpass_error = document.getElementById('conferror');
    var confpass = document.getElementById('r_password').value;
    reg1 = 1;
    reg2 = 1;
    reg3 = 1;
    reg4 = 1;
    reg5 = 1;
    reg6 = 1;
    reg7 = 1;

    if(fname == ""){
        document.getElementById('FName').style.borderColor = "red";
        fname_error.innerHTML = "Please enter first name";
        reg1 = 0;
    }
    else{
        reg1 = 1;
    }  

    if(lname == ""){
        document.getElementById('LName').style.borderColor = "red";
        lname_error.innerHTML = "Please enter last name";
        reg2 = 0;
    }
    else{
        reg2 = 1;
    } 

    if(contact == ""){
        document.getElementById('address').style.borderColor = "red";
        contact_error.innerHTML = "Please enter address";
        reg3 = 0;
    }
    else{
        reg3 = 1;
    }

    if(email == ""){
        document.getElementById('email').style.borderColor = "red";
        email_error.innerHTML = "Please enter email";
        reg4 = 0;
    }
    else{
        reg4 = 1;
    }

    if(username == ""){
        document.getElementById('user_name').style.borderColor = "red";
        username_error.innerHTML = "Please enter username";
        reg5 = 0;
    }
    else{
        reg5 = 1;
    }

    if(pass == ""){
        document.getElementById('pass_word').style.borderColor = "red";
        pass_error.innerHTML = "Please enter a password";
        reg6 = 0;
    }
    else{
        var regex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
        if(regex.test(pass) === false) {
            document.getElementById('pass_word').style.borderColor = "red";
            pass_error.innerHTML = "Please enter proper password";
            reg6 = 0;
        } 
        else {
            reg6 = 1;
        }
    }
    
    if(confpass == ""){
        document.getElementById('r_password').style.borderColor = "red";
        confpass_error.innerHTML = "Please re-enter password";
        reg7 = 0;
    }
    else{
        if(confpass != pass) {
            document.getElementById('r_password').style.borderColor = "red";
            confpass_error.innerHTML = "Passwords do not match";
            reg7 = 0;
        } 
        else {
            confpass_error.innerHTML = "Passwords matching";
            document.getElementById('conferror').style.color = "green";
            reg7 = 1;
        }
    }

    if(reg1 === 1 && reg2 ===1 && reg3 === 1 && reg4 === 1 && reg5 === 1 && reg6 === 1 && reg7 == 1){
        return true;  
    }
    else{
        return false;
    }

}

var check = function() {
    if (document.getElementById('pass_word').value ==
      document.getElementById('r_password').value) {
      document.getElementById('message').style.color = 'green';
      document.getElementById('message').innerHTML = 'Passwords are matching';
    } else {
      document.getElementById('message').style.color = 'red';
      document.getElementById('message').innerHTML = 'Passwords do not match';
    }
  }