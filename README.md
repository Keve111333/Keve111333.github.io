<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Download File</title>
</head>
<body>

    <button onclick="downloadFile()">letöltés</button>

    <script>
        function downloadFile() {
            var fileUrl = 'test-1_0_0.apk';
            var a = document.createElement('a');
            a.href = fileUrl;
            a.download = 'downloaded_file.txt';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        }
    </script>

</body>
</html>
