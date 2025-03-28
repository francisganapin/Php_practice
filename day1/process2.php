<?php

if($_SERVER['REQUEST_METHOD']=='POST'){
    $name = htmlspecialchars($_POST['NAME']);
    $email = filter_var($_POST['email'],FILTER_SANITIZE_EMAIL);

    if(empty($name)|| empty($email)|| empty($age)){
        
    }
}