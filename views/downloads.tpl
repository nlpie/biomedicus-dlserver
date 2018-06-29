<!doctype html>
<html lang="en">
<head>
    <title>BioMedICUS Downloads</title>
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
    <h1>BioMedICUS Downloads</h1>
    <p>BioMedICUS has two options available for required model files:</p>
    <ul>
        <li>A more-comprehensive data set available on this page that includes terms from SNOMED CT
            and other restricted data sets, but requiring individuals to be licensed as users of the
            UMLS Metathesaurus. You can get a UMLS license at no charge
            <a href="https://www.nlm.nih.gov/databases/umls.html">here</a>. Use of the SNOMED CT
            data in these models may require a fee if you are not in a
            <a href="https://www.snomed.org/members/">IHTSDO member country</a>.
        </li>
        <li>A less-comprehensive, baseline data set that does not include terms from SNOMED CT,
            available from
            <a href="http://github.com/nlpie/biomedicus/releases">
                github.com/nlpie/biomedicus/releases/
            </a>.
        </li>
    </ul>
    <h4>UMLS Licensed</h4>
    <table class="table table-striped">
        % for file, size, time in umls:
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
</div>

<script src="//code.jquery.com/jquery-2.2.0.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
        integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"
        crossorigin="anonymous"></script>

</body>
</html>
