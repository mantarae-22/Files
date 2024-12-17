function validateform(){  
    var username=document.userForm.username.value; //document.getElementById("username").value;  
    var password=document.userForm.userpwd.value; // document.getElementById("userpwd").value;  

    console.log("pw=" + password);
    console.log(password.length);

    document.getElementById("lblusername").style.backgroundColor = "";
    document.userForm.username.style.backgroundColor = "";
    document.userForm.userpwd.style.backgroundColor = "";

    if (username == ""){  
        document.getElementById("lblusername").style.backgroundColor = "yellow";
        document.getElementById("divMessage").textContent = "User name can't be blank.";
        document.userForm.username.style.backgroundColor = "yellow";
      return false;  
    }
    else if(password.length<6){     
      document.getElementById("lblpassword").style.backgroundColor = "yellow";   
      document.userForm.userpwd.style.backgroundColor = "yellow";
      document.getElementById("divMessage").textContent = "Password must be at least 6 characters.";
      return false;  
      }  

      return true;
      
    }  