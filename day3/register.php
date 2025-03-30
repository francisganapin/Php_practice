<?php

    if($_SERVER["REQUEST_METHOD"] == "POST"){
        $card_id = $_POST['card_id'];
        $first_name = $_POST['first_name'];
        $last_name = $_POST['last_name'];
        $expiry = $_POST['expiry'];

        $data = json_encode([
            "card_id" => $card_id,
            "first_name" => $first_name,
            "last_name" => $last_name,
            "expiry" => $expiry,
                ]);

        $url = 'http://127.0.0.1:5000/member/register';
        
        $ch = curl_init($url);
        curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
        curl_setopt($ch,CURLOPT_HTTPHEADER,['Content-type: application/json']);
        curl_setopt($ch,CURLOPT_POST,true);
        curl_setopt($ch,CURLOPT_POSTFIELDS,$data);

        $response = curl_exec($ch);
        curl_close($ch);

        echo $response;
    }

    ?>