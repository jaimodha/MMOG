<?php 
	session_start();
	if(isset($_SESSION['logged_in'])){

?>

<html>
<head>
    <title>Discussion Board</title>
    <link rel="stylesheet" href="../css/forumstyle.css">
    <meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<meta http-equiv="Content-Type" content="text/html; charset=US-ASCII">
	<link rel="stylesheet" href="../css/foundation.css" />
	<script src="../js/vendor/modernizr.js"></script>
</head>
<body>
    

        <div class="row" style="padding-top: 90px;">
        	<p style="text-align: justify;">Contested is developed using the open source game engine Panda 3D, which make use of python as the client side technology and java as the back end technology. This page will provide all the documents that the developer will need to know all about the game. Please stay tuned to this space for more updates and documents. This game is developed as a part od a course CS454-CS594 Massive Multiplayer Games Development at California State University, Los Angeles.</p>
      	</div>
      	<br/>
        <div class="row">
          
	          	<div class="medium-9 columns" >
	            <ul>
	              <li><a href='../devdoc/protocol.pdf'>Protocol</a></li>
	                <li><a href='../devdoc/ContestedDocTemplate.pdf'>Template</a></li>
	                <li><a href='../devdoc/Game Design Presentation.pdf'>Design</a></li>
	                <li><a href='https://docs.google.com/spreadsheets/d/1ctzq5cJrtxbbN4QMmKmnr7Zf_EJz6Oydv90SDeiX2-A/edit#gid=0'>Class Forum</a></li>
	                <li><a href='https://docs.google.com/spreadsheets/d/1L_rNxvIdASuzROTdYm2EgFEwXx5BJ5q0TOMI5d-vKzs/edit#gid=1875600178'>Task Assignment</a></li>
	                <li><a href='../devdoc/NetworkingPresentation.pdf'>Networking Document</a></li>
	            </ul>
          </div>

          <div class="medium-3 columns" style="border: 1px solid #466d98;">
             <ul class="side-nav">
              <li><a href="../index.php">Disscussion Board</a></li>
              <li><a href="logout.php">Logout</a></li>
            </ul>
         </div>
       

    <script src="js/vendor/jquery.js"></script>
	<script src="js/foundation.min.js"></script>
	<script>
  		$(document).foundation();
	</script>
</body>
</html>
<?php 
	}else{
?>
<html>
<head>
    <title>Discussion Board</title>
    <link rel="stylesheet" href="../css/forumstyle.css">
    <meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<meta http-equiv="Content-Type" content="text/html; charset=US-ASCII">
	<link rel="stylesheet" href="../css/foundation.css" />
	<script src="../js/vendor/modernizr.js"></script>
</head>
<body>
    <div class ="container" style="padding-top: 90px;">
        <a href="../index.php" id="logo">Discussion Board</a>
        <br/><br/>
        	<h4 style="color:#aa0000;">You must be developer to access this area.</h4>
        	<br/><br/>
        	<a href="index.php">&larr; Back</a>
    </div>
    <script src="js/vendor/jquery.js"></script>
	<script src="js/foundation.min.js"></script>
	<script>
  		$(document).foundation();
	</script>
</body>
</html>
<?php
	}
?>