<!DOCTYPE html>
<html>
    <head>
        <title> Oom nom nom... </title>
    </head>
    <body>
<?php 
echo "<h1>Become admin to get a flag!.</h1>";

$admin_cookie = $_COOKIE["admin"];
if($admin_cookie === null || $admin_cookie === ""){
    setcookie("admin", "false");
}
if($admin_cookie === "true"){
    echo "<p>You've got it. Here's your flag:</p>";
    echo "<p>m365{i_at3_y0ur_c00ki3}</p>";
} else {
    echo "<p>You ain't admin. Go back.</p>";
}
?>
    </body>
</html>