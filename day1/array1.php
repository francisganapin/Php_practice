<?php

    $fruits = ['banana','apple','orange','peanut'];
    ?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fruits table</title>
</head>
<body>

        <table border='1' cellpadding='10' cellspacing='0'>
                <tr>
                    <th>ID<th>
                    <th>Fruit Name </th>
                </tr>
                <?php
                foreach ($fruits as $index => $fruits){
                    echo '<tr>';
                    echo '<td>' . ($index + 1) . '</td>';
                    echo "<td>" . htmlspecialchars($fruits) . "</td>";
                    echo '</tr>';
                }
                ?>
        </table>
    
</body>
</html>