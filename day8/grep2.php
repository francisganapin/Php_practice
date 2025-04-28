<?php
$input = ["Red","Pink","Green","Blue","Pupple"];

$result = preg_grep("/^p/i",$input);
print_r($result)
?>