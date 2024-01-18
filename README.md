<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Download File</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-color: #00bcd4; /* Turquoise background */
        }

        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            background-color: #009688; /* Turquoise button color */
            color: #fff;
            border: none;
            border-radius: 5px;
            outline: none;
        }

        button:hover {
            background-color: #00796b; /* Darker turquoise on hover */
        }
    </style>
</head>
<body>

    <button onclick="downloadFile()">Letöltés</button>

    <script>
        function downloadFile() {
            var fileUrl = 'Bw.apk';
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
