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
	<li class="active"><a href="createBuilds.php">Create a Build</a></li>
	<li><a href="searchBuilds.php">Build Look-Up</a></li>
	<li><a href="accountcreation.php">Create Account</a></li>
    </ul>
  </div>
</nav>

<?php
include "connection.php";
$buser = $_GET["username"];
$bpword = $_GET["password"];
$cpuID = $_GET["cpuID"];
$gpuID = $_GET["gpuID"];
$mID = $_GET["mID"];
$ramID = $_GET["ramID"];
$stID = $_GET["stID"];
$psuID = $_GET["psuID"];
$tID = $_GET["tID"];
//$bcode = rand();

echo "<h2>Congratulations on your new build $buser</h2>";

$sql = "INSERT INTO build(b_cpu,b_gpu,b_motherboard,b_psu,b_storage,b_tower,b_ram)
SELECT CPU_name, GPU_name, MB_name,PSU_name,RAM_name,Storage_name,Case_name 
FROM cpu,gpu,motherboard,psu,ram,storage,tower 
WHERE CPU_id = '$cpuID' AND GPU_id = '$gpuID' AND MB_id = '$mID' AND PSU_id = '$psuID' AND RAM_id = '$ramID' AND Storage_id = '$stID' AND Case_id = '$tID'";

$result = $mysqli->query($sql);
?>

<?php
include "connection.php";
$buser = $_GET["username"];
$cpuID = $_GET["cpuID"];
$gpuID = $_GET["gpuID"];
$mID = $_GET["mID"];
$ramID = $_GET["ramID"];
$stID = $_GET["stID"];
$psuID = $_GET["psuID"];
$tID = $_GET["tID"];
$bcode = rand(0, 1000);

echo "<h3>Please save your build code: $bcode</h3>";
$sql = "UPDATE build SET b_user = '$buser', b_code = '$bcode' WHERE b_user IS NULL AND b_code IS NULL;";
$result = $mysqli->query($sql);

//echo "<h3>Price calculated</h3>";
$sql = "update build
                set b_price = (select sum(x.price) as total
                from (select CPU_price as price
                    from cpu
                    where CPU_id = '$cpuID'
                    union all
                    select GPU_price
                    from gpu
                    where GPU_id = '$gpuID'
                    union all
                    select MB_price
                    from motherboard
                    where MB_id = '$mID'
                    union all
                    select RAM_price
                    from ram
                    where RAM_id = '$ramID'
                    union all
                    select Storage_price
                    from storage
                    where Storage_id = '$stID'
                    union all
                    select PSU_price
                    from psu
                    where PSU_id = '$psuID'
					union all
                    select Case_price
                    from tower
                    where Case_name = '$tID'
                ) x) 
                where b_code = '$bcode'";

$result = $mysqli->query($sql);
$mysqli->close();
?>

</html>

