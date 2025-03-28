<?php
    if($_SERVER['REQUEST_METHOD'] == 'POST'){
        $name = $_POST['name'];
        $email = $_POST['email'];

        $data = json_encode(['name' => $name, 'email' => $email]);

        $url = 'htpp://127.0.0.1:500/save';

        $ch = curl_init($url);
        curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
        curl_setopt($ch,CURLOPT_HTTPHEADER,['Content-Type: application/json']);
        curl_setopt($ch,CURLOPT_POST,true);
        curl_setopt($ch,CURLOPT_POSTFIELD,$data);

        $respose = curl_exec($ch);
        curl_close($ch);
    }

    ?>