<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gmail Küldés</title>
    <script>
        // JavaScript kód a random szám generálásához
        function getRandomInt(min, max) {
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }

        // Függvény a gomb kattintására
        function setRandomSubject() {
            var randomSubject = "Tárgy #" + getRandomInt(1, 99999);
            document.getElementById("emailButton").href = "mailto:cimzett@gmail.com?subject=" + encodeURIComponent(randomSubject);
        }
    </script>
</head>
<body>

<h1>Küldj e-mailt!</h1>

<!-- Gomb a Gmail linkhez -->
<a id="emailButton" href="javascript:void(0);" onclick="setRandomSubject();" target="_blank">
    <button type="button">E-mail küldése</button>
</a>

</body>
</html>
