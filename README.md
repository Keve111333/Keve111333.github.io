<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Webshop</title>
    <style>
        body {
            font-family: 'Montserrat', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            color: #333;
        }

        h1 {
            font-size: 2em;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .product {
            width: 80%;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .product:hover {
            transform: scale(1.05);
        }

        .product img {
            max-width: 100%;
            border-radius: 8px;
            margin-bottom: 10px;
        }

        p {
            color: #777;
        }

        .button-container {
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
        }

        .button {
            padding: 10px 20px;
            background-color: #007BFF;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .button:hover {
            background-color: #0056b3;
        }

        .promo-container {
            margin-top: 30px;
            padding: 20px;
            background-color: #007BFF;
            color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>

<h1>Exkluzív Gorduska Merch</h1>

<div class="product">
    <img src="og_merch.jpg" alt="Termék 1">
    <h2>OG Merch</h2>
    <p>Ár: 5500Ft</p>
</div>

<div class="product">
    <img src="karacsonyi_merch.jpg" alt="Termék 2">
    <h2>Karácsonyi Merch</h2>
    <p>Ár: 5800Ft</p>
</div>

<div class="product">
    <img src="IMG_20231213_192239.jpg" alt="Termék 3">
    <h2>Gordus Aláírás Kártya</h2>
    <p>Ár: 1000Ft</p>
</div>

<div class="button-container">
    <a href="https://youtu.be/mnjOLKoLiX8" target="_blank" class="button">tutorial (e-mail)</a>
    <a href="https://youtube.com/shorts/gc2SFRRbQHM" target="_blank" class="button">tutorial (fizetés)</a>
    <a href="mailto:gorduskapodcast@gmail.com?subject=vasarlas" target="_blank" class="button">E-mail</a>
</div>

<div class="promo-container">
    <h2>Promókód</h2>
    <p>Használd az alábbi kódot e-mail üzenet során, ha mind a három terméket megveszed:</p>
    <ul>
        <li>MINDHAROM2324 - 20% kedvezmény</li>
    </ul>
    
</div>

</body>
</html>
