<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Webshop</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }

        header {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 1em;
        }

        section {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            padding: 2em;
        }

        .product {
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 1em;
            margin: 1em;
            width: 300px;
        }

        footer {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 1em;
            position: fixed;
            bottom: 0;
            width: 100%;
        }

        /* Add your additional styles here */

        #cart {
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 1em;
            margin: 1em;
            width: 300px;
            position: fixed;
            top: 80px;
            right: 20px;
        }
    </style>
</head>

<body>

    <header>
        <h1>Webshop</h1>
    </header>

    <section>
        <div class="product" id="product1">
            <h2>Product 1</h2>
            <p>Description of Product 1.</p>
            <p>Price: $20.00</p>
            <button onclick="addToCart('Product 1', 20.00)">Add to Cart</button>
        </div>

        <div class="product" id="product2">
            <h2>Product 2</h2>
            <p>Description of Product 2.</p>
            <p>Price: $25.00</p>
            <button onclick="addToCart('Product 2', 25.00)">Add to Cart</button>
        </div>
        <!-- Add more products as needed -->
    </section>

    <div id="cart">
        <h2>Shopping Cart</h2>
        <ul id="cart-items"></ul>
        <p>Total: $<span id="cart-total">0.00</span></p>
    </div>

    <footer>
        <p>&copy; 2024 Webshop. All rights reserved.</p>
    </footer>

    <script>
        let cartItems = [];
        let cartTotal = 0;

        function addToCart(productName, price) {
            cartItems.push({ name: productName, price: price });
            cartTotal += price;

            updateCart();
        }

        function updateCart() {
            const cartItemsElement = document.getElementById('cart-items');
            const cartTotalElement = document.getElementById('cart-total');

            // Clear previous items
            cartItemsElement.innerHTML = '';

            // Populate cart items
            cartItems.forEach(item => {
                const listItem = document.createElement('li');
                listItem.textContent = `${item.name} - $${item.price.toFixed(2)}`;
                cartItemsElement.appendChild(listItem);
            });

            // Update total
            cartTotalElement.textContent = cartTotal.toFixed(2);
        }
    </script>

</body>

</html>
