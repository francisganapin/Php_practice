<?php

    $url = "https://jsonplaceholder.typicode.com/posts/1";
    $ch = curl_init($url);


    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $respose = curl_exec($ch);
    curl_close($ch);

    $data = json_decode($response,true);
    echo 'Title'. $data['title'];

    ?>