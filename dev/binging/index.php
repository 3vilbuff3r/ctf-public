<!DOCTYPE html>
<html>
    <head>
        <title> Keep Binging... </title>
    </head>
    <body>
<?php 
echo "<h1>I'll only talk to <a href='https://bing.com/'>Bing</a> &lt;3!.</h1>";

$agent = $_SERVER['HTTP_USER_AGENT'];

if(stripos($agent, "bingbot") !== false){
    echo "<p>Hello Bing!. Here's your flag: </p>";
    echo "<p>m365{my_ag3nt_1s_b1ng}</p>";
} else {
    echo "<h3>You're no bing, I don't like you :(</h3>";
}

?>
    </body>
</html>