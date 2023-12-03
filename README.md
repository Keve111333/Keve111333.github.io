<html lang="hu">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Szám kitaláló játék</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      background-color: #f4f4f4;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      transition: background-color 0.5s;
    }
    .container {
      background-color: #fff;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    h1 {
      margin-bottom: 20px;
    }
    input {
      padding: 10px;
      margin-right: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
      width: 100px;
      text-align: center;
    }
    button {
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      background-color: #4CAF50;
      color: white;
      cursor: pointer;
    }
    p {
      margin-top: 20px;
      font-weight: bold;
      opacity: 0;
      transition: opacity 0.5s ease;
    }
    .show {
      opacity: 1;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Gondoltam egy számra 1 és 100 között!</h1>
    <p>Te hány tippből találod ki?</p>
    <input type="number" id="guess" placeholder="Tipp" onkeydown="if (event.keyCode == 13) document.getElementById('checkButton').click()">
    <button id="checkButton" onclick="checkGuess()">Tipp Gomb</button>
    <p id="message"></p>
    <label for="theme">Háttérszín változtatása: </label>
    <select id="theme" onchange="changeBackground()">
      <option value="#f4f4f4">Alapértelmezett</option>
      <option value="#000">Fekete</option>
      <option value="#808080">Szürke</option>
      <option value="#fff">Fehér</option>
    </select>
  </div>
  <script>
    let randomNumber = Math.floor(Math.random() * 100) + 1;
    let attempts = 0;

    function checkGuess() {
      let userGuess = document.getElementById('guess').value;
      attempts++;
      if (userGuess == randomNumber) {
        showMessage(`Gratulálok! ${attempts} próbálkozásból találtad el a számot!`, 'green');
      } else if (userGuess < randomNumber) {
        showMessage('Túl alacsony, próbáld újra!', 'red');
      } else {
        showMessage('Túl magas, próbáld újra!', 'red');
      }
      document.getElementById('guess').value = '';
      changeBackground();
    }

    function showMessage(message, color) {
      let messageElement = document.getElementById('message');
      messageElement.innerHTML = message;
      messageElement.style.color = color;
      messageElement.classList.add('show');
      setTimeout(function() {
        messageElement.classList.remove('show');
      }, 2000);
    }

    function changeBackground() {
      let selectedColor = document.getElementById('theme').value;
      if (document.getElementById('guess').value == randomNumber) {
        document.body.style.backgroundColor = selectedColor;
      }
    }
  </script>
</body>
</html>
