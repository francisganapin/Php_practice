<?php

    $url ='http://127.0.0.1:5000/data/2';
    $respose = file_get_contents($url);

    $data =json_decode($respose,true);

        echo '<table border="1">';
        echo 
        '<tr>
        <td>Id</td> 
        <td>Name</td>
        <td>Age</td>
        <td>Membership</td>
        <td>Status</td>
        </tr>';

        foreach($data as $key => $value){
        echo '<tr>';
        echo '<td>'. htmlspecialchars($value['id'])  .'</td>';
        echo '<td>'. htmlspecialchars($value['name']) .'</td>';
        echo '<td>'.     htmlspecialchars($value['age']) .'</td>';
        echo '<td>'. htmlspecialchars($value['membershipType']) .'</td>';
        echo '<td>'.  htmlspecialchars($value['activeStatus']) .'</td>';
        echo '<tr>';
    }
        echo '</table>'
  
?>
