<?php
header("Access-Control-Allow-Origin: *");
$site=$_POST['url'];
$html = file_get_contents($site);
//echo $html;
$bytes=file_put_contents('markup.txt', $html);

// Can use this if your default interpreter is Python 2.x.
// Has some problem executing 'which python2'. So, absolute path is just simpler.
//$python_path=exec("which python 2>&1 ");
//$decision=exec("$python_path test.py $site 2>&1 ");

$decision=exec("/Library/Frameworks/Python.framework/Versions/2.7/bin/python2 test.py $site 2>&1 ");
echo $decision;
?>
