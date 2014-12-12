<?php 
	try{
		$pdo = new PDO('mysql:host=csproject.calstatela.edu; dbname=gamedev', 'gamedev', '3tb=PChh');
	}catch(PDOException $e){
		exit('Database connection error.');
	}
?>