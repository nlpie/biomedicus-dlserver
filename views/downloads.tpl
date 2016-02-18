

<!doctype html>
<html lang="en">
<head>
  <title>BioMedICUS Downloads</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"
        integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css"
        integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">
</head>
<body>
<div class="content container-fluid">
    <h1>Biomedicus Downloads</h1>

    <h3>System Downloads</h3>
    <table class="table table-striped">
    % for item in system:
    <tr>
        <td>
            <p>
                <a href="open/system/{{item}}">{{item}}</a>
            </p>
        </td>
    </tr>
    %end
    </table>

    <h3>Data/Model downloads</h3>

    <h4>Open</h4>
    <table class="table table-striped">
    % for item in open_data:
    <tr>
        <td>
            <p>
                <a href="open/data/{{item}}">{{item}}</a>
            </p>
        </td>
    </tr>
    %end
    </table>

    <h4>UMLS Licensed</h4>
    <table class="table table-striped">
    % for item in umls:
    <tr>
        <td>
            <p>
                <a href="verify-umls/{{item}}">{{item}}</a>
            </p>
        </td>
    </tr>
    %end
    </table>
</div>

<script src="//code.jquery.com/jquery-2.2.0.min.js"></script>

<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"
        integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS"
        crossorigin="anonymous"></script>

</body>
</html>
