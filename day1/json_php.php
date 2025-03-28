<?php

$data = ['name' => 'Francis','age' => 25];
$jsonData = json_encode($data);

echo $jsonData;

?>


<?php

$jsonString = '{"name":"Francis","age":25}';
$data = json_decode($jsonString,true);

echo $data["name"];

    ?>