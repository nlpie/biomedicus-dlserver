<!doctype html>
<html lang="en">
<head>
    <title>NLP/IE Downloads</title>
    <link rel="stylesheet"
          href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
          integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
          crossorigin="anonymous">

    <link rel="stylesheet"
          href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css"
          integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp"
          crossorigin="anonymous">
</head>
<body>
<div class="content container-fluid">
    <h1>NLP/IE Downloads</h1>
    % for section in sections:
        <h2>{{section['name']}}</h2>
        %if section['description'] is not None:
        %include(section['description'])
        %end
        <h4>UMLS License Required</h4>
        <table class="table table-striped">
            % for file, size, time in section['umls_files']:
            <tr>
                <td>
                    <p>
                        <a href="verify-umls/{{file}}">{{file}}
                            <small>{{time}} - {{size}}</small>
                        </a>
                    </p>
                </td>
            </tr>
            %end
        </table>
    %end
</div>

<script src="//code.jquery.com/jquery-2.2.0.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
        integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"
        crossorigin="anonymous"></script>

</body>
</html>