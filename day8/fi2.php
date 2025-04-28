

<?php 

$input = [
    'Its is 5 o clock',
    '40 days',
    'No number Here',
    'In the year 2000'
];

$result = preg_filter('/[0-9]+/','($0)',$input);
print_r($result);


?>