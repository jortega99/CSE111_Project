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

<h2>Chose Edit Option</h2>

<form class="form-horizontal" action="updateCPU.php">
<fieldset>
<!-- Form Name -->
<legend>Edit CPU</legend>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="username">Username</label>  
  <div class="col-md-4">
  <input id="username" name="username" type="text" placeholder="username" class="form-control input-md" required="">
    
  </div>
</div>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="password">Password</label>  
  <div class="col-md-4">
  <input id="password" name="password" type="text" placeholder="password" class="form-control input-md" required="">
  <span class="help-block">sign in to update</span>  
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="b_code">Build Code</label>  
  <div class="col-md-4">
  <input id="b_code" name="b_code" type="text" placeholder="" class="form-control input-md" required="">
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="cpu_ID">New CPU ID</label>  
  <div class="col-md-4">
  <input id="cpu_ID" name="cpu_ID" type="text" placeholder="" class="form-control input-md" required="">  
  </div>
</div>

<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="search"></label>
  <div class="col-md-4">
    <button id="search" name="" class="btn btn-success">Edit Build</button>
  </div>
</div>
</fieldset>
</form>

<form class="form-horizontal" action="updateGPU.php">
<fieldset>
<!-- Form Name -->
<legend>Edit GPU</legend>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="username">Username</label>  
  <div class="col-md-4">
  <input id="username" name="username" type="text" placeholder="username" class="form-control input-md" required="">
  </div>
</div>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="password">Password</label>  
  <div class="col-md-4">
  <input id="password" name="password" type="text" placeholder="password" class="form-control input-md" required="">
  <span class="help-block">sign in to update</span>  
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="b_code">Build Code</label>  
  <div class="col-md-4">
  <input id="b_code" name="b_code" type="text" placeholder="" class="form-control input-md" required="">
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="cpu_ID">New GPU ID</label>  
  <div class="col-md-4">
  <input id="gpu_ID" name="gpu_ID" type="text" placeholder="" class="form-control input-md" required="">  
  </div>
</div>
<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="search"></label>
  <div class="col-md-4">
    <button id="search" name="" class="btn btn-success">Edit Build</button>
  </div>
</div>
</fieldset>
</form>

<form class="form-horizontal" action="updateMB.php">
<fieldset>
<!-- Form Name -->
<legend>Edit Motherboard</legend>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="username">Username</label>  
  <div class="col-md-4">
  <input id="username" name="username" type="text" placeholder="username" class="form-control input-md" required="">
  </div>
</div>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="password">Password</label>  
  <div class="col-md-4">
  <input id="password" name="password" type="text" placeholder="password" class="form-control input-md" required="">
  <span class="help-block">sign in to update</span>  
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="b_code">Build Code</label>  
  <div class="col-md-4">
  <input id="b_code" name="b_code" type="text" placeholder="" class="form-control input-md" required="">    
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="cpu_ID">New MB ID</label>  
  <div class="col-md-4">
  <input id="m_ID" name="m_ID" type="text" placeholder="" class="form-control input-md" required="">  
  </div>
</div>
<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="search"></label>
  <div class="col-md-4">
    <button id="search" name="" class="btn btn-success">Edit Build</button>
  </div>
</div>
</fieldset>
</form>
<!-- Form Name -->
<form class="form-horizontal" action="updateRAM.php">
<fieldset>
<!-- Form Name -->
<legend>Edit Memory</legend>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="username">Username</label>  
  <div class="col-md-4">
  <input id="username" name="username" type="text" placeholder="username" class="form-control input-md" required=""> 
  </div>
</div>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="password">Password</label>  
  <div class="col-md-4">
  <input id="password" name="password" type="text" placeholder="password" class="form-control input-md" required="">
  <span class="help-block">sign in to update</span>  
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="b_code">Build Code</label>  
  <div class="col-md-4">
  <input id="b_code" name="b_code" type="text" placeholder="" class="form-control input-md" required="">
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="ram_ID">New RAM ID</label>  
  <div class="col-md-4">
  <input id="ram_ID" name="ram_ID" type="text" placeholder="" class="form-control input-md" required="">  
  </div>
</div>
<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="search"></label>
  <div class="col-md-4">
    <button id="search" name="" class="btn btn-success">Edit Build</button>
  </div>
</div>
</fieldset>
</form>

<form class="form-horizontal" action="updateSt.php">
<fieldset>
<!-- Form Name -->
<legend>Edit Storage</legend>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="username">Username</label>  
  <div class="col-md-4">
  <input id="username" name="username" type="text" placeholder="username" class="form-control input-md" required="">
  </div>
</div>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="password">Password</label>  
  <div class="col-md-4">
  <input id="password" name="password" type="text" placeholder="password" class="form-control input-md" required="">
  <span class="help-block">sign in to update</span>  
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="b_code">Build Code</label>  
  <div class="col-md-4">
  <input id="b_code" name="b_code" type="text" placeholder="" class="form-control input-md" required="">
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="st_ID">New Storage ID</label>  
  <div class="col-md-4">
  <input id="st_ID" name="st_ID" type="text" placeholder="" class="form-control input-md" required="">  
  </div>
</div>
<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="search"></label>
  <div class="col-md-4">
    <button id="search" name="" class="btn btn-success">Edit Build</button>
  </div>
</div>
</fieldset>
</form>

<form class="form-horizontal" action="updatePSU.php">
<fieldset>
<!-- Form Name -->
<legend>Edit Power Supply</legend>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="username">Username</label>  
  <div class="col-md-4">
  <input id="username" name="username" type="text" placeholder="username" class="form-control input-md" required="">  
  </div>
</div>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="password">Password</label>  
  <div class="col-md-4">
  <input id="password" name="password" type="text" placeholder="password" class="form-control input-md" required="">
  <span class="help-block">sign in to update</span>  
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="b_code">Build Code</label>  
  <div class="col-md-4">
  <input id="b_code" name="b_code" type="text" placeholder="" class="form-control input-md" required=""> 
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="psu_ID">New PSU ID</label>  
  <div class="col-md-4">
  <input id="psu_ID" name="psu_ID" type="text" placeholder="" class="form-control input-md" required="">  
  </div>
</div>
<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="search"></label>
  <div class="col-md-4">
    <button id="search" name="" class="btn btn-success">Edit Build</button>
  </div>
</div>
</fieldset>
</form>

<form class="form-horizontal" action="updateCase.php">
<fieldset>
<!-- Form Name -->
<legend>Edit Case<legend>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="username">Username</label>  
  <div class="col-md-4">
  <input id="username" name="username" type="text" placeholder="username" class="form-control input-md" required="">
    
  </div>
</div>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="password">Password</label>  
  <div class="col-md-4">
  <input id="password" name="password" type="text" placeholder="password" class="form-control input-md" required="">
  <span class="help-block">sign in to update</span>  
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="b_code">Build Code</label>  
  <div class="col-md-4">
  <input id="b_code" name="b_code" type="text" placeholder="" class="form-control input-md" required=""> 
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="case_ID">New Case ID</label>  
  <div class="col-md-4">
  <input id="case_ID" name="case_ID" type="text" placeholder="" class="form-control input-md" required="">  
  </div>
</div>
<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="search"></label>
  <div class="col-md-4">
    <button id="search" name="" class="btn btn-success">Edit Build</button>
  </div>
</div>
</fieldset>
</form>

<form class="form-horizontal" action="deleteBuild.php">
<fieldset>
<!-- Form Name -->
<legend>Delete Build<legend>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="username">Username</label>  
  <div class="col-md-4">
  <input id="username" name="username" type="text" placeholder="username" class="form-control input-md" required="">
</div>
</div>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="password">Password</label>  
  <div class="col-md-4">
  <input id="password" name="password" type="text" placeholder="password" class="form-control input-md" required="">
  <span class="help-block">sign in to update</span>  
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="b_code">Build Code</label>  
  <div class="col-md-4">
  <input id="b_code" name="b_code" type="text" placeholder="" class="form-control input-md" required=""> 
  </div>
</div>
<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="search"></label>
  <div class="col-md-4">
    <button id="search" name="" class="btn btn-danger">Delete</button>
  </div>
</div>
</fieldset>
</form>
</html>

