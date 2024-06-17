<?php
// action_page.php

// Configuration
$db_host = 'localhost';
$db_username = 'your_username';
$db_password = 'your_password';
$db_name = 'your_database';

// Connect to database
$conn = new mysqli($db_host, $db_username, $db_password, $db_name);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: ". $conn->connect_error);
}

// Get form data
$username = $_POST['username'];
$password = $_POST['password'];
$email = $_POST['email'];

// Validate form data
if (empty($username) || empty($password) || empty($email)) {
    echo "Please fill in all fields.";
    exit;
}

// Insert data into database
$query = "INSERT INTO users (username, password, email) VALUES ('$username', '$password', '$email')";
if ($conn->query($query) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: ". $query. "<br>". $conn->error;
}

// Close connection
$conn->close();

?>
