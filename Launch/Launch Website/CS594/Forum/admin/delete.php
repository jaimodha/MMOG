<?php 
	session_start();
	include_once('../includes/connection.php');
	include_once('../includes/article.php');

	$article = new Article;

	if(isset($_SESSION['logged_in']) and $_SESSION['user'] == "admin"){
		if(isset($_GET['id'])){
			$id = $_GET['id'];

			$query = $pdo->prepare("DELETE FROM articles WHERE article_id = ?");
			$query->bindValue(1, $id);
			$query->execute();

			header('Location: delete.php');
		}
		$articles = $article->fetch_all();
?>

<html>
<head>
    <title>Discussion Board</title>
    <link rel="stylesheet" href="../css/forumstyle.css">
</head>
<body>
    <div class ="container">
        <a href="../index.php" id="logo">Discussion Board</a>
        <br/>

        <h4>Select an article to Delete from the DropDown Menu.</h4>
        
        <form action="delete.php" method="get">
        	<select onchange="this.form.submit();" name="id">
        		<option>None</option>
        		<?php  foreach ($articles as $article) {?>
        			<option value="<?php echo $article['article_id']?>"><?php echo $article['article_title']?></option>
        		<?php } ?>
        	</select>
        </form>
         <a href="../index.php">&larr; Back</a>
    </div>
</body>
</html>

<?php
	}else{
		header('Location: ../index.php');
	}
?>