<!DOCTYPE html>
<html>
    <head>
        <title> Ping pong utils... </title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    </head>
    <body class="container-fluid">
<?php 

echo "<h1>Ping pong utils.</h1>";
echo "<p></p>";
echo "<pre>Here's a tool if you'd like to ping someone. </pre>";
echo "<pre>A friend of mine told me to senitize the user input so prevent myself from getting hacked.</pre>";
echo "<pre>I know how to write secure code. Hack me if you can.</pre>";
echo "<p></p>";
if(isset($_POST['ip'])){

    $ip = $_POST['ip'];
    if(stripos($ip, " ")){
        echo "<pre>There is no hostname on the entire internet that has spaces in its name.</pre>";
        echo "<pre>What exactly are you trying to do? </pre>";
    } else {
        echo "<pre>";
        passthru("ping -c 1 -w 2 " . $_POST['ip']);
        echo "</pre>";    
    }
} 
echo "<p></p>";
echo "<form method='POST'>";
echo "<label> IP address to ping: </label>";
echo "<input type='text' name='ip' placeholder='127.0.0.1'>";
echo "<input type='submit' value='Ping it!'>";
echo "</form>";
echo "<p></p>";

echo "<!-- If you ever are able to hack, report it to me by getting the secret from '/etc/flag'. -->";
?>
    </body>
</html>