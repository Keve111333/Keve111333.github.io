<html lang="hu">
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

        .button-container {
            position: relative;
        }

        button {
            position: relative;
            z-index: 1;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            background-color: #009688; /* Turquoise button color */
            color: #fff;
            border: none;
            border-radius: 5px;
            outline: none;
            display: block;
            margin: 0 auto;
        }

        .caption {
            position: absolute;
            top: -30px;
            opacity: 0;
            transition: opacity 0.5s ease;
            color: #009688; /* Turquoise text color */
            font-size: 14px;
            font-weight: bold;
            letter-spacing: 1px;
        }

        /* Fading in animation when the page loads */
        .fade-in {
            opacity: 1;
        }

        .button-container .caption.fade-in {
            opacity: 1;
        }

        button:hover {
            background-color: #00796b; /* Darker turquoise on hover */
        }
    </style>
</head>
<body>

    <div class="button-container">
        <button onclick="downloadFile()">Letöltés</button>
        <div class="caption fade-in">A Gorduska Podcast Eredeti Játéka (DEMO)!</div>
    </div>

    <script>
        // Add this script to add the fade-in class after a delay
        window.onload = function() {
            var caption = document.querySelector('.caption');
            setTimeout(function() {
                caption.classList.add('fade-in');
            }, 1000); // Adjust the delay in milliseconds as needed
        };

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
