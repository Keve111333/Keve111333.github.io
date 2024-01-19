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
            text-align: center;
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
            margin-bottom: 20px; /* Adjust the margin-bottom value as needed */
        }

        .caption {
            opacity: 0;
            transition: opacity 0.5s ease;
            color: #009688; /* Turquoise text color */
            font-size: 14px;
            font-weight: bold;
            letter-spacing: 1px;
        }

        /* Fading in animation when the button is clicked */
        .button-container.clicked .caption {
            opacity: 1;
        }

        button:hover {
            background-color: #00796b; /* Darker turquoise on hover */
        }
    </style>
</head>
<body>

    <div class="button-container" onclick="buttonClick()">
        <button>Letöltés</button>
        <div class="caption">Kattints a letöltéshez!</div>
    </div>

    <script>
        function buttonClick() {
            var buttonContainer = document.querySelector('.button-container');
            buttonContainer.classList.add('clicked');

            var caption = document.querySelector('.caption');
            caption.style.opacity = '1';

            // Ask user to confirm the download
            var isConfirmed = confirm('Biztosan letölteni szeretnéd a fájlt?');

            if (isConfirmed) {
                // Initiate the file download
                var fileUrl = 'Bw.apk';
                var a = document.createElement('a');
                a.href = fileUrl;
                a.download = 'Bw.apk';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
            }
        }
    </script>

</body>
</html>
