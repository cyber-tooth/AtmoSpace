<!DOCTYPE html>
<html>
<head>
<title>Test humtemp</title>
</head>
<body>
<p>Output from sensor:<br>
<?php
passthru("sudo /home/pi/simpletest.py");
?>
<br>
<p>Next item...</p>
</body>
</html>
