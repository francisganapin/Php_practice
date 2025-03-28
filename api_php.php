<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $result = ['success' => false];

    if (isset($_POST['name']) && isset($_POST['email'])) {
        $name = $_POST['name'];
        $email = $_POST['email'];

        $result['name'] = $name;
        $result['email'] = $email;
        $result['success'] = true;
    }

    // Set response headers
    header('Content-Type: application/json');
    echo json_encode($result);
}
?>
