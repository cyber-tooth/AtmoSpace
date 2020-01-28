<?php

/*
 * Eventuell muss noch "sudo apt install php-mysql" auf dem webserver installiert werden, damit das Skript komplett ausgeführt werden.
 * Das Skript wurde schon mit einfachen Werten getestet.
 */

$servername = "localhost"; //Da das skript auf dem gleichen Webserver läuft wie die DB, ist das richtig. Sonst die IP-Adresse, wo die DB läuft.
$username = "root"; //this has to be replaced with the actual username when implemented
$password = "passwort"; //this should also be replaced when implemented
$dbname = "atmospace"; //and the database probably also has a different name

$result_array = array();

/* Create connection */
$conn = new mysqli($servername, $username, $password, $dbname);

/* Check connection */
if ($conn->connect_error) {
    die("Connection to database failed: " . $conn->connect_error);
}

/* SQL query to get results from database and table therein. Here "atmospacetable" must be replaced with actual table name.
The same is true of course for the column names."*/

$sql = "SELECT date_time, temperature, humidity, loudness FROM atmospacetable ORDER BY date_time desc LIMIT 1";

$result = $conn->query($sql);

/* If there are results from database push to result array */

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        array_push($result_array, $row);
    }
}
header('Content-type: application/json');
echo json_encode($result_array[0]);

$conn->close();

