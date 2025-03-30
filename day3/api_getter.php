<?php

    $url = 'http://127.0.0.1:5000/data/';

    $response = file_get_contents($url);

    $data = json_decode($response,true);

    echo "First Name: ".  $data['first_name'] . "<br>";
    echo "Last Name: ". $data['last_name'];

    ?>