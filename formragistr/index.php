<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>(。>︿<)_θ</title>
</head>
<body>
<div class="login">
	<h1>Авторизация</h1>
    <form action = "index.php" method="post">
    	<input type="text" name="u" placeholder="Логин" required="required" />
        <input type="password" name="p" placeholder="Пароль" required="required" />
        <button type="submit" class="btn btn-primary btn-block btn-large">Вход</button>
    </form>
</div>


    
</body>
</html>


<?php

$x = "Humoyun";


if ($_POST["u"] == $x){
    header("Location: index.html");
}
elseif($_POST["u"] > $x){
    header("Location: /nothtml/not.html");
}

///////////PASSWORDS

$pass = "1234";
 
if ($_POST["p"] == $pass){
    header("Location: /html/page Succes.html");
}elseif($_POST["p"] > $pass){
    header("Location: /nothtml/not.html");
}










?>  

