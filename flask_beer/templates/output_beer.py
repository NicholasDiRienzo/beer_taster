

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>Starter Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="../static/css/bootstrap.min.css" rel="stylesheet">

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <link href="../../assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="starter-template.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="../../assets/js/ie-emulation-modes-warning.js"></script>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Project name</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

<br><br>

<div class="container">
    <div class="starter-template">
        <h2>Output Page</h2>
        <p>Enter some user input</p>
    </div>

    <div class = "container">

      <form  action="/output" method="GET">
        <div class="form-group">
          <label for="birth_month">Birth Month:</label>
          <input type="text" id="birth_month" name='birth_month' placeholder="e.g. ">
        </div>
        <div>
          <button type="submit" class="btn btn-default btn-lg">Find these Cesareans!</button>
        </div>
      </form>
    </div>
    <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="../static/js/bootstrap.min.js"></script>

  </div> <!-- /.container-->

    <div class="container">
      <div class="starter-template">
        <h3>Results:</h3>
        <p class="lead">Below is the result of your query.<br> You just took user input and looked up the information. Now we need to expand the functionality!</p>
      </div>

      <table class="table table-hover">
      <tr><th>index</th>
      {% for birth in births %}
      <tr><td>{{ beer_list }}</td><td>{{ birth['attendant']}}</td><td> {{ birth['birth_month'] }}</td></tr>
      {% endfor %}
      </table>


     </div><!-- /.container -->

    <div class="container">
      <div class="starter-template">
        <h3>Another Result:</h3>
        <p class="lead">Now we've taken the input and called a function from your package.<br>The result is {{the_result}}</p>
      </div>


      <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
      <script src="../static/js/bootstrap.min.js"></script>


     </div><!-- /.container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="../../dist/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../../assets/js/ie10-viewport-bug-workaround.js"></script>

<script src="statics/js/bootstrap.min.js"></script
  </body>
</html>

