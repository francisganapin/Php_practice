<?php

    if ($_SERVER['REQUEST_METHOD'] === 'POST'){
       $username = $_POST['username'];
       $email = $_POST['email'];

       $data = json_encode(['username' => $username, 'email' => $email]);

       $url = "http://127.0.0.1:5000/save/database";

       $ch = curl_init($url);
       curl_setopt($ch, CURLOPT_RETURNTRANSFER,true);
       curl_setopt($ch, CURLOPT_HTTPHEADER,['Content-Type: application/json']);
       curl_setopt($ch,CURLOPT_POST,true);
       curl_setopt($ch,CURLOPT_POSTFIELDS,$data);

       $response = curl_exec($ch);
       curl_close($ch);

       echo $response;
    }

    ?>