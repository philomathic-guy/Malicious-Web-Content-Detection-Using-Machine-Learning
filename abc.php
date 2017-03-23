<?php
header("Access-Control-Allow-Origin: *");
//$a=(int)$_GET['no1'];
//$b=(int)$_GET['no2'];
//echo $a+$b;
$site=$_GET['url'];
$a=exec('python BE/test.py '.$site.' 2>&1 ');
echo $a;
?>
