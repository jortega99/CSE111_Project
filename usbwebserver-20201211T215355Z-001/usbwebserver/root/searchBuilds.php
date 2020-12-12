<html>
<head>
 <!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script> 

<title>Build Search</title>
<link href="css.css" rel="stylesheet" type="text/css">
</head>

<div id = "title">
</div>

<nav class="topnav navbar-inverse">
  <div class="container-fluid">
    <ul class="nav navbar-nav">
    <li class="active"><a href="index.php">Home</a></li>
    <li><a href="searchCPU.php">Computer Processors</a></li>
	<li><a href="searchGPU.php">Graphics Cards</a></li>
	<li><a href="searchMB.php">Motherboards</a></li>
	<li><a href="searchRam.php">Memory</a></li>
	<li><a href="searchSt.php">Storage</a></li>
	<li><a href="searchPSU.php">Power Supplies</a></li>
	<li><a href="searchTower.php">Towers</a></li>
	<li><a href="createBuilds.php">Create a Build</a></li>
	<li><a href="searchBuilds.php">Build Look-Up</a></li>
	<li><a href="accountcreation.php">Create Account</a></li>
    </ul>
  </div>
</nav>


<h2>Build Search</h2>

<form class="form-horizontal" action="buildListing.php">
<fieldset>

<!-- Form Name -->

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="b_code">Enter Build Code</label>  
  <div class="col-md-4">
  <input id="b_code" name="b_code" type="text" placeholder="" class="form-control input-md" required="">
    
  </div>
</div>

<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="search"></label>
  <div class="col-md-4">
    <button id="search" name="search" class="btn btn-success">Search</button>
  </div>
</div>

</fieldset>
</form>

<form class="form-horizontal" action="buildEdit.php">
<fieldset>

<!-- Form Name -->
<legend>Build Owner Options</legend>
<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="search"></label>
  <div class="col-md-4">
    <button id="search" name="" class="btn btn-success">Edit Build</button>
  </div>
</div>

</fieldset>
</form>

</html>
