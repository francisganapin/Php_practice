<?php

    if($_SERVER['REQUEST_METHOD']== 'POST'){
        if(!empty($_POST['name'])){
            $name = htmlspecialchars($_POST['name']);
            echo 'Hello,' . $name;
        }
        else{
            echo 'Please enter your name.';
        }
    }

    ?>