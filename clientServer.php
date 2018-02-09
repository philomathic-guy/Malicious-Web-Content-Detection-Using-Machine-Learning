<?php
header("Access-Control-Allow-Origin: *");
$site=$_POST['url'];
$html = file_get_contents($site);
//echo $html;
$bytes=file_put_contents('markup.txt', $html);
$a=exec('/usr/bin/python /opt/lampp/htdocs/BE/test.py '.$site.' 2>&1 ');
echo $a;
?>
