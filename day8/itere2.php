<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <?php
    function getIterable():iterable{
        return['a','b','c'];

    }

    $myIterable = getIterable();
    foreach($myIterable as $item){
        echo $item;
    }
    ?>


</body>
</html>