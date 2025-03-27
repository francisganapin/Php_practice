<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Input</title>
</head>
<body>
        
        <form action='process.php' method='POST'>
            <label for='name'>Enter your name:</label>
            <input type='text' id='name' name='name' required>
            <br>
            <label for='email'>Enter your email:</label>
            <input type='email' id='email' name='email' required>
            <br><br>
            <button type='submit'>Submit</button>
        </form>


</body>
</html>