<?php
    session_start();
    include_once('includes/connection.php');
    include_once('includes/article.php');

    $article = new Article;
    $articles = $article->fetch_all();
?>

<html>
<head>
    <title>Discussion Board</title>
    <link rel="stylesheet" href="css/forumstyle.css">
</head>
<body>
    <div class ="container">
        <a href="index.php" id="logo">Discussion Board</a>
        <ol>
        <?php foreach ($articles as $article) {?>
                <li>
                    <a href="article.php?id=<?php echo $article['article_id']; ?>">
                        <?php echo $article['article_title']?>
                    </a> - 
                    <small> 
                        posted <?php echo date('l jS', $article['article_timestamp']);?>
                    </small>
                </li>
        <?php } ?>
        </ol>
        <br />
        <a href = "admin">Developer Options</a> 
        <?php if(empty($_SESSION['logged_in'])){ ?>
        / <a href = "register.php">Become a Developer</a>  
        <?php } ?>
        / <a href="admin/devdoc.php">Developer Documentation</a>
    </div>
</body>
</html>