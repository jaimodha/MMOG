<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">

<html>
	<head profile="http://www.w3.org/2005/10/profile">
<link rel="icon" 
      type="image/png" 
      href="img/fevicon2.png">
	<title>Contested</title>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<meta name="viewport" content="user-scalable=yes, width=1240" />
	<meta http-equiv="Content-Type" content="text/html; charset=US-ASCII">
	<link rel="stylesheet" href="css/foundation.css" />
	<title>Contested-Home</title>
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
 <c:if test="${empty sessionScope['loginUser']}">
      <ul class="off-canvas-list">
       <li><label>Navigation</label></li>
          <li><a href = 'home.jsp'> Home</a></li>
         <li><a href = 'about.jsp'>About</a></li>
        <li><a href = 'docs.jsp' > Docs</a></li>
        <li><a href = 'download.jsp'>   Download </a></li>
        <li><a href = 'gallery.jsp'> Gallery</a></li>
         <li><a href = '../Forum/home.php'> Developer Zone</a></li>
      <!--   <li><label>Login/Register</label></li> -->
      </ul>
     <!--   <font color="black"><c:if test="${not empty param.Msg }">
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
    	<br />
    	<br />
    	
		<br />
		<br />
		<br />
    	<br />
    	
	
  			
				<center>	
				<div id="homenew_hype_container" style="position:relative;overflow:hidden;width:1240px;height:469px;">
		<script type="text/javascript" charset="utf-8" src="homenew.hyperesources/homenew_hype_generated_script.js?89627"></script>
	</div>
				
				<a href="download.jsp">Download the game and become the controller of the mysterious land.</a>
			   </center>
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



<br />
<br />

 <script src="js/vendor/jquery.js"></script>
    <script src="js/foundation.min.js"></script>
    <script>
      $(document).foundation();
    </script>
</body>
	
	
	
</html>