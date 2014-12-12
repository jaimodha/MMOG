<?php 
    include_once('includes/connection.php');
    include_once('includes/article.php');


    if(isset($_POST['username'], $_POST['password'], $_POST['repassword'])){
    	$username = $_POST['username'];
    	$password = md5($_POST['password']);
    	$repassword = md5($_POST['repassword']);

    	$query = $pdo -> prepare("SELECT * FROM dusers WHERE user_name = ?");
		$query -> bindValue(1, $username);
		$query -> execute();
		$num = $query->rowCount();

    	if(empty($username) or empty($password) or empty($repassword)){
    		$error = "All fields are required.";
    	}else if($password != $repassword){
            $error = "Passwords do not match.";
        }else if($num == 1){
            $error = "Username already taken.";
        }else{
            $query1 = $pdo -> prepare("INSERT INTO dusers (user_name, user_password) VALUES (?, ?)");
            $query1 -> bindValue(1, $username);
            $query1 -> bindValue(2, $password);
            $query1 -> execute();

            header('Location: admin/index.php');
            exit();
        }
    	
    }
?>


<html>
<head>
    <title>Discussion Board</title>
    <link rel="stylesheet" href="css/forumstyle.css">
</head>
<body>
    <div class ="container">
        <a href="../index.php" id="logo">Discussion Board</a>
        <br/><br/>

        <?php if(isset($error)){?>
        	<small style="color:#aa0000;"><?php echo $error;?></small>
        	<br/><br/>
        <?php } ?>
        <form action="register.php" method="post" autocomplete="off">
        	<input type="text" name="username" placeholder="Username"/><br/><br/>
        	<input type="password" name="password" placeholder="Password"/><br/><br/>
        	<input type="password" name="repassword" placeholder="Re-Password"/><br/><br/>
        	<input type="submit" name="submit" value="Register"/>
        </form>
    </div>
</body>
</html>