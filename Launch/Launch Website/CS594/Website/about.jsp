<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">

<html>
	<head profile="http://www.w3.org/2005/10/profile">
<link rel="icon" 
      type="image/png" 
      href="img/fevicon2.png">
		<title>About Us</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<meta http-equiv="Content-Type" content="text/html; charset=US-ASCII">
		<meta name="viewport" content="user-scalable=yes, width=1000" />
		<link rel="stylesheet" href="css/foundation.css" />
		<link rel="stylesheet" href="css/foundation-icons.css" />
		<script src="js/vendor/modernizr.js"></script>
	</head>
	<body>
		<div class="off-canvas-wrap" data-offcanvas>
  <div class="inner-wrap">
    <nav class="tab-bar">
    
	  
      <section class="left tab-bar-section">
        <h1 class="title"><img src = 'img/iconlogo.png' /></h1>
      </section>
      <section class="right-small">
        <a class="right-off-canvas-toggle menu-icon" href="#"><span></span></a>
      </section>
    </nav>


    <aside class="right-off-canvas-menu">
 <!--<c:if test="${empty sessionScope['loginUser']}">-->
      <ul class="off-canvas-list">
       <li><label>Navigation</label></li>
         <li><a href = 'home.jsp'> Home</a></li>
         <li><a href = 'about.jsp'>About</a></li>
        <li><a href = 'docs.jsp' > Docs</a></li>
        <li><a href = 'download.jsp'>   Download </a></li>
        <li><a href = 'gallery.jsp'> Gallery</a></li>
         <li><a href = '../Forum/home.php'> Developer Zone</a></li>
      <!--    <li><label>Login/Register</label></li>-->
      </ul>
      <!--  <font color="black"><c:if test="${not empty param.Msg }">
      	<c:out value="${param.Msg}"/>
      </c:if>
      </font>
      <font color="red"><c:if test="${not empty param.errMsg}">
            <c:out value="${param.errMsg}" />
       </c:if></font>
   <form method = 'POST' action = 'process.jsp' >	
      			<br/>
      			Username:<br />
      			<input type = 'text' name = 'uname'/><br />
      			Password:<br />
      			<input type = 'password' name = 'pwd'/><br />
      			<center>
      			<input type = 'submit' name = 'login' value = 'Login' />
      			<input type = 'submit' name = 'register' value = 'Register' /><br />
      			</center>
      </form>
     
</c:if>-->
  <!--<c:if test="${ not empty sessionScope['loginUser']}">
    <ul class="off-canvas-list">
       <li><label>Navigation</label></li>
        <li><a href = 'home.jsp'> Home</a></li>
         <li><a href = 'about.jsp'>About</a></li>
        <li><a href = 'docs.jsp' > Docs</a></li>
        <li><a href = '#'> Download </a></li>
        <li><a href = 'gallery.jsp'> Gallery</a></li>
      </ul>
<a href="logout.jsp">Logout </a></c:if>
 -->
    </aside>

    <section class="main-section">
      <!-- content goes here -->
    	<br />
	<br />
	<div class="row">
			<div class="medium-2 columns">
			</div>
			<div class="medium-10 columns">
				<img  src = 'img/Logo1.png' />
			</div>
		</div>
		
		<br />
		<br />
	
	<div class="row">
		<div class="medium-1 columns">
 		</div>
 		<div class="medium-11 columns">
 		<font color="#ffd700"><p>Contested is a MMOG that takes place in a medieval setting that supports up to fifty versus fifty player versus player combat. There are two factions competing for control points that provide advantages. The main objective is to capture control the majority of the world map while defending your territory.</p></font>
 		
			 <!--  <div id="aboutpage_hype_container" style="position:relative;overflow:hidden;width:1000px;height:540px;">
				<script type="text/javascript" charset="utf-8" src="aboutpage.hyperesources/aboutpage_hype_generated_script.js?65533"></script>
			</div>-->
		</div>
	</div>
	<div class="row">
		<div class="medium-1 columns">
 		</div>
 		<div class="medium-11 columns">
 		<font color="#ffd700"><p>This game design aims towards a cartoony description of a medieval-fantasy world where team-work is crucial to capturing objectives and gaining the upper hand. Teams are identified by their colors (red or blue) and minimalistic character design is preferred with playable classes and NPCs guarding control points. The map is a cartoony description of a jungle or green fields with trees, hills, grass and rivers.</p></font>
		</div>
	</div>
	<div class="row">
		<div class="medium-1 columns">
 		</div>
 		<div class="medium-11 columns">
 		<font color="#ffd700"><p>Contested is the massive multiplayer game that is delivered as a part of the course CS 454/ CS 594 (Multiplayer Online Game Development) at California State University Los Angeles by the enrolled students in the class of Fall 2014 under the guidance of Dr. Eun-Young Kang.</p></font>
		</div>
	</div>
		<br />
		<br />
		<br />
		<br />
		<br />
		<br />
		<br />
		<br />
		<br />
		<br />
		<br />
		<br />
		
  		
    </section>

  <a class="exit-off-canvas"></a>

  </div>
</div>

		
		
	
		
		
		<script src="js/vendor/jquery.js"></script>
    	<script src="js/foundation.min.js"></script>
    	<script>
      		$(document).foundation();
    	</script>
	</body>
</html>
