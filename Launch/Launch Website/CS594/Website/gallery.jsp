<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">

<html>
	<head profile="http://www.w3.org/2005/10/profile">
<link rel="icon" 
      type="image/png" 
      href="img/fevicon2.png">
		<title>Gallery</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<meta http-equiv="Content-Type" content="text/html; charset=US-ASCII">
		<meta name="viewport" content="user-scalable=yes, width=1000" />
		<link rel="stylesheet" href="css/foundation.css" />
		<link rel="stylesheet" href="css/foundation-icons.css" />
		<script src="js/vendor/modernizr.js"></script>
		<script src="js/vendor/jquery.js"></script>
<script src="js/foundation/foundation.js"></script>
<script src="js/foundation/foundation.orbit.js"></script>
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
       <!-- <li><label>Login/Register</label></li> --> 
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
     
</c:if>
  <c:if test="${ not empty sessionScope['loginUser']}">
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
    <ul class="example-orbit" data-orbit>
   
  <li>
    <center><img src="img/SwordsFront.png" alt="The mysterious sword man." /></center>
    <div class="orbit-caption">
     The mysterious sword man.
    </div>
  </li>
  <li class="active">
   <center> <img src="img/Axefront.png" alt="The mighty Axe man." /></center>
    <div class="orbit-caption">
      The mighty axe man.
    </div>
   
  </li>
   <li class="active">
   <center> <img src="img/chat0.png"  /></center>
    
  </li>
   <li class="active">
   <center> <img src="img/chat1.png" /></center>
   
   
  </li>
   <li class="active">
   <center> <img src="img/contested0.png"  /></center>
   
   
  </li>
  <li class="active">
   <center> <img src="img/contested1.png"  /></center>
   
   
  </li>
  <li class="active">
   <center> <img src="img/contested2.png"  /></center>
   
   
  </li>
  <li class="active">
   <center> <img src="img/contested3.png"  /></center>
   
   
  </li>
 <!--  <li><div class="custom-flex-video-class">
 <center> <iframe src="https://www.youtube.com/embed/1biIRxTRCS8" width="960" height="540" frameborder="0"></iframe></center>
</div></li>-->
  
</ul>

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