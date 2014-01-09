<?php 
$str = '/usr/lib/python2.6/site-packages/gtk-2.0/gconf.so'; 
echo $str . "\n"; 
$replace = ''; 

echo preg_replace('/\.[^.]*$/', $replace, $str) . "\n"; 

echo preg_replace('/\.(.*)/', $replace, $str) . "\n"; 

echo preg_replace('/^(.*?)\//', $replace, $str) . "\n"; 

echo preg_replace('/(.*)\//', $replace, $str) . "\n"; 

preg_match('/(\/.*)\.(.*?)/', $str, $match); 
foreach ($match as $key => $value) { echo "$key => $value \n"; } 

preg_match('/(\/.*?)\.(.*)/', $str, $match); 
foreach ($match as $key => $value) { echo "$key => $value \n"; } 

preg_match('/(.*?)\/(.*)/', $str, $match); 
foreach ($match as $key => $value) { echo "$key => $value \n"; } 

preg_match('/(.*)\/(.*)/', $str, $match); 
foreach ($match as $key => $value) { echo "$key => $value \n"; } 
?>
