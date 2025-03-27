<?php 


$fruits = ['banana','apple','orange'];
echo $fruits[0];

?>



<?php

$person = ['name'=> 'john','age' => 25, 'gender' => 'male'];
echo $person['name'];

?>

<?php

$students = [
    ['name' => 'Alice','age' => 22],
    ['name' => 'Bob','age' => 23],
];

echo $students[1]['name'];
?>



<?php

    $fruits = ['banana','apple','orange'];
    foreach ($fruits as $fruits){
        echo $fruits . '<br>';
    }



?>
