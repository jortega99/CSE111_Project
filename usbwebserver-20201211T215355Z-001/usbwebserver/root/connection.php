<?php
//variables to connect to database
$host = "localhost";
$username = "root";
$user_pass = "usbw";
$database_in_use = "pcbuilder";

//create connection instance mysqli is same as conn 
$mysqli = new mysqli($host, $username, $user_pass, $database_in_use);
?>