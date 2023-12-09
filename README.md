<html>
<head>
  <title>Hacker Mód</title>
  <style>
    body {
      background-color: black;
      color: green;
      font-family: monospace;
      text-align: center;
      padding-top: 100px;
    }
    h1 {
      font-size: 50px;
    }
    p {
      font-size: 24px;
    }
    button {
      padding: 10px 20px;
      margin: 10px;
      font-size: 20px;
      background-color: green;
      color: black;
      border: none;
      cursor: pointer;
    }
  </style>
  <script>
    let binaryNumbers = document.getElementById("binaryNumbers");

    function generateRandomBinary() {
      let binary = Math.floor(Math.random() * 2);
      binaryNumbers.textContent += binary;
    }
  </script>
</head>
<body>
  <h1>HACKER MÓD</h1>
  <p>Bejelentkezés engedélyezve...</p>
  <div id="binaryNumbers"></div>
  <button onclick="generateRandomBinary()">Generálás</button>
  <button onclick="location.reload()">Újra</button>
</body>
</html>
