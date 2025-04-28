<?php
$str = "The rain in Spain Falls mainly on the Plans.";
$pattern = '/ain/i';

if(preg_match_all($pattern,$str,$matches)){
    print_r($matches);
}

?>