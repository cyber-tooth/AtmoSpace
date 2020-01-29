<?php

/*
 * Eventuell muss noch "sudo apt install php-mysql" auf dem webserver installiert werden, damit das Skript komplett ausgeführt werden.
 * Das Skript wurde schon mit einfachen Werten getestet.
 * Die Zahlenwerte nur zum testen. Wenn das Skript in die Tabelle schreibt, dann htmlspecialchars... entkommentieren, die Zahlenwerte löschen und mit dem PI verbinden:)
 * Ich habe keinen Wert für die Zeit und das Datum angegeben, da meine Testtabelle eine Timestamp automatisch hinzufügt.
*/
$temperature = htmlspecialchars($_POST["temperature"]);
$humidity = htmlspecialchars($_POST["humidity"]);
$loudness = htmlspecialchars($_POST["loudness"]);

echo "temperature: $temperature humidity: $humidity loudness: $loudness";

$servername = "localhost"; //Da das skript auf dem gleichen Webserver läuft wie die DB, ist das richtig. Sonst die IP-Adresse, wo die DB läuft.
$username = "atmospace"; //this has to be replaced with the actual username when implemented
$password = "atmospace"; //this should also be replaced when implemented
$dbname = "atmospace"; //and the database probably also has a different name

//Create connection:
$conn = new mysqli($servername, $username, $password, $dbname);

//Check connection
if($conn->connect_error) {
    die("Connection failed; " . $conn->connect_error);
}

//insert statement to insert data into table. Here "atmospacetable must be replaced with actual table name"
$sql = "INSERT INTO atmospacetable (temperature, humidity, loudness) VALUES ($temperature, $humidity, $loudness)";

if($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn-error;
}

$conn->close();
