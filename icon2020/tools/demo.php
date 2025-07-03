<html>
 <head>
  <title>PHP Test</title>
 </head>
 <body>
 <?php

$signed_url = "http://172.16.26.35:8080/";
$ch = curl_init($signed_url);
curl_setopt($ch, CURLOPT_PORT, 8080);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HEADER, 0);
$data= curl_exec($ch);
echo $data;
curl_close($ch);


?> 
 </body>
</html>

