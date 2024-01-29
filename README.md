<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weboldal Címe</title>
    <style>
        body {
            background-color: #2c3e50;
            color: #ecf0f1;
            font-family: 'Arial', sans-serif;
        }

        h1, h2, h3 {
            color: #ecf0f1;
        }

        button {
            background-color: #3498db;
            color: #ecf0f1;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            margin: 10px;
            cursor: pointer;
        }

        button:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>

    <h1>Sunny Videa</h1>

    <h2>Filmeink</h2>

    <button onclick="openVideo('https://m.youtube.com/watch?v=EmYWSzwtN8c')">Az állarcos gyilkos 1</button>

    <script>
        function openVideo(videoUrl) {
            window.open(videoUrl, '_blank');
        }
    </script>

</body>
</html>
