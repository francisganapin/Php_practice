<?php

$name = 'John';
$age = '25';
$price = '99.99';

echo "Name: $name, Age: $age, Price: $price";

?>


<?php

    $age = 20;

    if ($age >= 18){
        echo "your are adult.";
    } else{
        echo "You are a minor";
    }
    ?>


<?php 
    for($i = 1; $i <= 5; $i++){
        echo "Number: $i <br>";
    }

    ?>


<?php
$i =1;
    while($i <=5){
        echo "While: $i <br>";
        $i++;
    }
    ?>


<?php
    function greet($name){
        return "Hello, $name!";
    }
    echo greet('Francis');
    ?>