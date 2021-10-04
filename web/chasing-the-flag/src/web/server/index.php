<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Chasing The Flag | Finished</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>
  <body>
    <nav class="navbar navbar-dark bg-primary">
      <span class="navbar-brand mb-0 h1">Chasing The Flag</span>
    </nav>
    <div class="container mt-5">
      <h1>It's Over!</h1>
      <p>Congratulations! Now, winners can claim their code <a href="/generatecode.php">here</a>!</p>
      <div class="form-row align-items-center">
        <div class="col-md-9 my-1">
          <input type="text" class="form-control" placeholder="Keyword" id="keyword">
        </div>
        <div class="col-auto mt-1">
          <div class="form-check">
            <input class="form-check-input" type="checkbox" id="ascending">
            <label class="form-check-label" for="ascending">
              Ascending
            </label>
          </div>
        </div>
        <div class="col-auto my-1">
          <button onclick="refresh_table()" class="btn btn-primary">Search</button>
        </div>
      </div>
      <div class="row d-flex justify-content-center">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Team id</th>
              <th scope="col">Team name</th>
              <th scope="col">Points</th>
            </tr>
          </thead>
          <tbody id="table-contents">
          </tbody>
        </table>
      </div>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

    <script>

function clear_table() {
  $('#table-contents').empty();
}

function get_table() {
  url = "leaderboard.php";
  if ($('#keyword').val() !== "") {
    keyword = $('#keyword').val();
    keyword = keyword.split(" ").join("");
    keyword = keyword.split("'").join("");
    keyword = keyword.split("%").join("");
    url += "?name=" + keyword;
    if ($('#ascending').is(":checked")) {
      url += "&sort=ASC";
    }
  } else if ($('#ascending').is(":checked")) {
    url += "?sort=ASC";
  }
  $.ajax({
    url: url,
    success: load_table,
    error: error_alert
  });
}

function load_table(data) {
  data.forEach(insert_row);
}

function insert_row(row) {
  row_string = "<tr><td>" + row["id"] + "</td><td>" + row["name"] + "</td><td>" + row["score"] + "</td></tr>";
  $('#table-contents').append(row_string);
}

function error_alert(data) {
  if (data["error"]) {
    alert(data["error"]);
  }
}

function refresh_table() {
  clear_table();
  get_table();
}

$(document).ready(refresh_table);
    </script>
  </body>
</html>
