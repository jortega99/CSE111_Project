<html>
<head>
 <!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script> 

<title>Storage List</title>
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
	<li class="active"><a href="searchSt.php">Storage</a></li>
	<li><a href="searchPSU.php">Power Supplies</a></li>
	<li><a href="searchTower.php">Towers</a></li>
	<li><a href="createBuilds.php">Create a Build</a></li>
	<li><a href="searchBuilds.php">Build Look-Up</a></li>
	<li><a href="accountcreation.php">Create Account</a></li>
    </ul>
  </div>
</nav>

<h2>Storage List</h2>

<?php
include "connection.php";

if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}
//echo $mysqli->host_info . "<br>";

$sql = "SELECT Storage_id, Storage_name, Storage_price, Storage_manufactuer, Storage_capacity, Storage_type from Storage";
$result = $mysqli->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "ID: " . $row["Storage_id"]." - Name: " . $row["Storage_name"]. " - Price: " . $row["Storage_price"]. " - Manufacturer: " . $row["Storage_manufactuer"]
	.	" - Capacity: " . $row["Storage_capacity"]. " - Type: " . $row["Storage_type"]. "<br>";
  }
} else {
  echo "0 results";
}
?>

</html>
