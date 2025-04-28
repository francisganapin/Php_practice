<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

<?php 
    function printIterable(iterable
    $myIterable
    ){
        foreach($myIterable as $item){
           echo $item; 
        }
    }

    $arr = ['a','n','c'];
    printIterable($arr);
    ?>

</body>
</html>