<html>
<head>
 <!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script> 

<title>Build Creation</title>
<link href="css.css" rel="stylesheet" type="text/css">
</head>

<div id = "title">
</div>
	
<nav class="topnav navbar-inverse">
  <div class="container-fluid">
    <ul class="nav navbar-nav">
    <li><a href="index.php">Home</a></li>
    <li><a href="searchCPU.php">Computer Processors</a></li>
	<li><a href="searchGPU.php">Graphics Cards</a></li>
	<li><a href="searchMB.php">Motherboards</a></li>
	<li><a href="searchRam.php">Memory</a></li>
	<li><a href="searchSt.php">Storage</a></li>
	<li   class="active"><a href="searchPSU.php">Power Supplies</a></li>
	<li><a href="searchTower.php">Towers</a></li>
	<li><a href="createBuilds.php">Create a Build</a></li>
	<li><a href="searchBuilds.php">Build Look-Up</a></li>
	<li><a href="accountcreation.php">Create Account</a></li>
    </ul>
  </div>
</nav>


<?php
include "connection.php";
$buser = $_GET["username"];
$bpword = $_GET["password"];
$bcode = $_GET["b_code"];
$psu_ID = $_GET["psu_ID"];

echo "<h3>New PSU saved to build</h3>";
$sql = "UPDATE build SET b_cpu = (select PSU_name from psu where PSU_id = '$psu_ID') where b_code = '$bcode'";
$result = $mysqli->query($sql);

//echo "<h3>Price calculated</h3>";
$result = $mysqli->query($sql);
$mysqli->close();
?>

</html>

