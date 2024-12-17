<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$errorMessage = "";

if ($_SERVER['REQUEST_METHOD']=='POST'){   
    $username = $_POST['username'];
    $password = $_POST['userpwd'];
    require_once('dbConnect.php');
    $sql= "SELECT * FROM tbl_user WHERE username = '{$username}' AND password = '{$password}'; ";
    $result = mysqli_query($conn,$sql);
    $check = mysqli_fetch_array($result);
    if(isset($check)){
        $errorMessage = 'success!';
    }else{
        $errorMessage = 'User name and password not found. Please try again.';
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="w8.css">

    <style>
        .errorMessage{
            color: red;
            padding: 20px;
        }
    </style>
</head>
<body>


    <?php include 'header.php';?>
    <form name="userForm" onsubmit="return validateform();" method="post" action="login.php">
    
    <div id="divMessage" class="errorMessage">
        <?php echo $errorMessage; ?>
    </div>
    
    <!-- Userid -->  
        <label for="username" id="lblusername">Username:</label> 
        <input type="text" name="username" id="username"> <!--  required title="Please enter your username" -->
        <br>
        <br>
        <!-- Password -->
        <label for="userpwd" id="lblpassword">Password:</label>
        <input type="text" name="userpwd" id="userpwd">
        <br>
        <br>
        <!-- Submit Button -->
        <button type="submit">Submit</button>
    </form>
    <script src="validate.js"></script>
    <?php include 'footer.php';?>

</body>
</html>