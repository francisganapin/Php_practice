<?php

    $items = ['appple21','banana','cherry34','date'];
    $result = preg_filter('/\d+/','',$items);
    print_r($result);
    
?>