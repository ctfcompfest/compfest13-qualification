<?php

  getenv('MYSQL_DBHOST') ? $db_host=getenv('MYSQL_DBHOST') : $db_host="localhost";
  getenv('MYSQL_DBPORT') ? $db_port=getenv('MYSQL_DBPORT') : $db_port="3306";
  getenv('MYSQL_DBUSER') ? $db_user=getenv('MYSQL_DBUSER') : $db_user="hanyabaca";
  getenv('MYSQL_DBPASS') ? $db_pass=getenv('MYSQL_DBPASS') : $db_pass="Bacaajajangandidrop";
  getenv('MYSQL_DBNAME') ? $db_name=getenv('MYSQL_DBNAME') : $db_name="challenge";

  if (strlen( $db_name ) === 0)
    $conn = new mysqli($db_host, $db_user, $db_pass);
  else
    $conn = new mysqli($db_host, $db_user, $db_pass, $db_name);

  // Check connection
  if ($conn->connect_error)
    die("Connection failed: " . $conn->connect_error);

  if (isset($_GET["name"])) {
    $keyword = str_replace(' ', '', $_GET["name"]);
    $keyword = str_replace('UNION', '', $keyword);
    $keyword = str_replace('SELECT', '', $keyword);
    $keyword = str_replace('union', '', $keyword);
    $keyword = str_replace('select', '', $keyword);
  } else {
    $keyword = "";
  }

  if (isset($_GET["sort"])) {
    if ($_GET["sort"] === "ASC") {
      $sortof = $_GET["sort"];
    } else {
    $sortof = "DESC";
  }
  
  } else {
    $sortof = "DESC";
  }

  $sql = "SELECT * FROM teamdata WHERE name LIKE '%".$keyword."%' ORDER BY points ".$sortof;

  if (!($result=mysqli_query($conn,$sql))) {
    // check ada error gak? kalau ada return errornya langsung
    if ($conn -> error) {
      $errortext = array(
        'error' => $conn -> error
      );
      header('Content-type: application/json');
      echo json_encode($errortext);
      $result -> free_result();
      $conn->close();
      http_response_code(500);
      exit(0);
    }    
  }

  $data = array();

  while($row = mysqli_fetch_row( $result )) {
    $team = array(
      'id' => $row[0],
      'name' => $row[1],
      'score' => $row[2]
    );
    array_push($data, $team);
  }
  header('Content-type: application/json');
  $json = json_encode( $data );
  if ($json)
    echo $json;
  else
    echo $data;

  $result -> free_result();
  $conn->close();
?>
