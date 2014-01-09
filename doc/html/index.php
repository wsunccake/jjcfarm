<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head>

<?php
function findHtmlFiles($dir = '.', $pattern = '/./'){
  $files = array();
  $prefix = $dir . '/';
  $dir = dir($dir);
  while (false !== ($file = $dir->read())){
    if ($file === '.' || $file === '..') continue;
    $file = $prefix . $file;
    if (is_dir($file)) {
      $tmpList = findHtmlFiles($file, $pattern);
      $files = array_merge($files, $tmpList);
    }
    if (preg_match($pattern, $file)){
      $files[] = $file;
    }
  }
  return $files;
}
?>

<meta http-equiv="Content-Type" content="text/html" charset="zh_TW.UTF-8">
<title>FTP</title>
<link rel="stylesheet" href="defaults.css" type="text/css">
</head>

<body>

<?php
$files = findHtmlFiles('.', '/\.html$/');
$replace = '';
foreach ($files as $f)  {
  $title_name = preg_replace('/(.*)\//', $replace, $f);
  $title_name = preg_replace('/\.(.*)/', $replace, $title_name);
  echo "<a href=\"$f\">$title_name</a><br />\n";
}
?>

</body>
</html>


<!-- header -->


