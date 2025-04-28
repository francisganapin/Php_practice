<?php

$str = "<h1>Hello WorldÆØÅ!</h1>";

$clean = preg_replace(`/[^\x20-\x7E]/`,
    '',$clean);

echo $clean;

?>