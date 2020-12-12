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
	<li><a href="searchPSU.php">Power Supplies</a></li>
	<li><a href="searchTower.php">Towers</a></li>
	<li><a href="createBuilds.php">Create a Build</a></li>
	<li class="active"><a href="searchBuilds.php">Build Look-Up</a></li>
	<li><a href="accountcreation.php">Create Account</a></li>
    </ul>
  </div>
</nav>

<?php
include "connection.php";
$bcode = $_GET["bcode"];

echo "<h3>Price Updated</h3>";
$sql = "update build
                set b_price = (select sum(x.price) as total
                from (select CPU_price as price
                    from cpu
                    where CPU_name like '%b_cpu%'
                    union all
                    select GPU_price
                    from gpu
                    where GPU_name like '%b_gpu%'
                    union all
                    select MB_price
                    from motherboard
                    where MB_name like '%b_motherboard%'
                    union all
                    select RAM_price
                    from ram
                    where RAM_name like '%b_ram%'
                    union all
                    select Storage_price
                    from storage
                    where Storage_name like '%b_storage%'
                    union all
                    select PSU_price
                    from psu
                    where PSU_name like '%b_psu%'
					union all
                    select Case_price
                    from tower
                    where Case_name like '%b_tower%'
                ) x) 
                where b_code = '$bcode'";

$result = $mysqli->query($sql);
$mysqli->close();
?>

</html>

