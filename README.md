<!DOCTYPE html>
<html lang="hu">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Szám kitaláló játék</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
    }
  </style>
</head>
<body>
  <h1>Gondolj egy számra 1 és 100 között!</h1>
  <p>Nézd meg, hogy milyen gyorsan kitalálom!</p>
  <input type="number" id="guess" placeholder="Tippeld meg a számot">
  <button onclick="checkGuess()">Tippeld meg</button>
  <p id="message"></p>
  <script>
    let randomNumber = Math.floor(Math.random() * 100) + 1;
    let attempts = 0;

    function checkGuess() {
      let userGuess = document.getElementById('guess').value;
      attempts++;
      if (userGuess == randomNumber) {
        document.getElementById('message').innerHTML = `Gratulálok! ${attempts} próbálkozásból találtad el a számot!`;
      } else if (userGuess < randomNumber) {
        document.getElementById('message').innerHTML = 'Túl alacsony, próbáld újra!';
      } else {
        document.getElementById('message').innerHTML = 'Túl magas, próbáld újra!';
      }
    }
  </script>
</body>
</html>
