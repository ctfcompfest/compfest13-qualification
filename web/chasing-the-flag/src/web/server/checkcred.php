<?php

  if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    exit(0);
  }

  if ( !isset($_POST['username'], $_POST['password']) ) {
    http_response_code(401);
    exit(0);
  }

  getenv('MYSQL_DBHOST') ? $db_host=getenv('MYSQL_DBHOST') : $db_host="localhost";
  getenv('MYSQL_DBPORT') ? $db_port=getenv('MYSQL_DBPORT') : $db_port="3306";
  getenv('MYSQL_DBUSER') ? $db_user=getenv('MYSQL_DBUSER') : $db_user="hanyabaca";
  getenv('MYSQL_DBPASS') ? $db_pass=getenv('MYSQL_DBPASS') : $db_pass="Bacaajajangandidrop";
  getenv('MYSQL_DBNAME') ? $db_name=getenv('MYSQL_DBNAME') : $db_name="challenge";

  if (strlen( $db_name ) === 0)
    $conn = new mysqli("$db_host", $db_user, $db_pass);
  else
    $conn = new mysqli("$db_host", $db_user, $db_pass, $db_name);

  // Check connection
  if ($conn->connect_error)
    die("Connection failed: " . $conn->connect_error);

  // Prepare our SQL, preparing the SQL statement will prevent SQL injection.
  if ($stmt = $conn->prepare('SELECT id, password FROM teamcreds WHERE username = ? AND winner')) {
    // Bind parameters (s = string, i = int, b = blob, etc), in our case the username is a string so we use "s"
    $stmt->bind_param('s', $_POST['username']);
    $stmt->execute();
    // Store the result so we can check if the account exists in the database.
    $stmt->store_result();

    if ($stmt->num_rows > 0) {
      $stmt->bind_result($id, $password);
      $stmt->fetch();
      if ($_POST['password'] === $password) {
        // Return flag
        $flag = array("flag" => "COMPFEST13{get-fifty-percent-off-in-CTF-Course-using-this-code_c765355330}");
        header('Content-type: application/json');
        echo json_encode($flag);
      } else {
        http_response_code(401);
      }
    } else {
      // Incorrect username
      http_response_code(401);
    }

    $stmt->close();
  }

?>