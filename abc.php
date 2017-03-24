<?php
header("Access-Control-Allow-Origin: *");
//$a=(int)$_GET['no1'];
//$b=(int)$_GET['no2'];
//echo $a+$b;
$site=$_GET['url'];
echo "<script type='text/javascript'>alert('$site');</script>";
$a=exec('/usr/bin/python /opt/lampp/htdocs/BE/test.py '.$site.' 2>&1 ');
echo $a;
?>
