<?php

/*$sname= "sql211.infinityfree.com";
$uname= "if0_37062813";
$password = "e885NPpocXaL";
$db_name = "if0_37062813_class";
*/

$sname= "localhost:3307";
$uname= "root";
$password = "";
$db_name = "csc356_test";

$conn = mysqli_connect($sname, $uname, $password, $db_name);

if (!$conn) {
    echo "Connection failed!";
}
?>