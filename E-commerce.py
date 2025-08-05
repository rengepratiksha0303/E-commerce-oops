<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Simple Store</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Simple Store</h1>
  <div class="products">
    <div class="product">
      <h3>Product A</h3>
      <p>$10</p>
      <button onclick="addToCart('Product A', 10)">Add to Cart</button>
    </div>
    <div class="product">
      <h3>Product B</h3>
      <p>$15</p>
      <button onclick="addToCart('Product B', 15)">Add to Cart</button>
    </div>
    <div class="product">
      <h3>Product C</h3>
      <p>$20</p>
      <button onclick="addToCart('Product C', 20)">Add to Cart</button>
    </div>
  </div>

  <h2>Cart</h2>
  <ul id="cart"></ul>
  <p>Total: $<span id="total">0</span></p>

  <script src="script.js"></script>
</body>
</html>
body {
  font-family: Arial, sans-serif;
  margin: 20px;
  background-color: #f4f4f4;
}

.products {
  display: flex;
  gap: 20px;
}

.product {
  background: white;
  padding: 10px;
  border: 1px solid #ccc;
  width: 150px;
  text-align: center;
}

button {
  margin-top: 10px;
  padding: 5px 10px;
}
let total = 0;

function addToCart(productName, price) {
  const cart = document.getElementById('cart');
  const item = document.createElement('li');
  item.textContent = `${productName} - $${price}`;
  cart.appendChild(item);

  total += price;
  document.getElementById('total').textContent = total;
}
