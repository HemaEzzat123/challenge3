from flask import Flask, render_template, request, render_template_string
import random

app = Flask(__name__)

app.secret_key = "cf49d97a5680998cbddbee283eeb03adbeda772b"

@app.route("/lol_no_one_will_see_whats_here")
def troll1():
    return render_template("troll1.html")

@app.route("/what_are_you_searching_for")
def troll2():
    return render_template("troll2.html")

@app.route("/", methods=["GET"])
def inject():
    hints = ["Lz9zZWNyZXQ9ZmxhZw==", "L2xvbF9ub19vbmVfd2lsbF9zZWVfd2hhdHNfaGVyZQ==", 
             "d2hhdF9hcmVfeW91X3NlYXJjaGluZ19mb3IK"];
    hint = hints[random.randint(0, len(hints)-1)]
    secret = request.args.get("secret", default="AzCTF{3n0f_tr0l!in}")
    
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>repeaaaaaat</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            /* Global Styles */
            :root {
                --primary-color: #1a5f7a;
                --secondary-color: #88c0d0;
                --accent-color: #2e3440;
                --text-color: #2e3440;
                --background-color: #eceff4;
            }

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                color: var(--text-color);
                background-color: var(--background-color);
            }

            a {
                text-decoration: none;
                color: inherit;
            }

            /* Header & Navigation */
            header {
                background-color: white;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                position: sticky;
                top: 0;
                z-index: 10;
            }

            nav {
                max-width: 1200px;
                margin: 0 auto;
                padding: 1rem;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            .logo img {
                height: 50px;
            }

            nav ul {
                display: flex;
                list-style: none;
            }

            nav ul li {
                margin-left: 2rem;
            }

            nav ul li a {
                color: var(--text-color);
                font-weight: 500;
                transition: color 0.3s ease;
            }

            nav ul li a:hover {
                color: var(--primary-color);
            }

            /* Hero Section */
            .hero {
                text-align: center;
                padding: 4rem 1rem;
                background: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.9)),
                border-radius: 10px;
                margin: 2rem auto;
                max-width: 1200px;
            }

            .hero h1 {
                font-size: 3rem;
                color: var(--primary-color);
                margin-bottom: 1rem;
            }

            .hero p {
                font-size: 1.2rem;
            }

            /* Product Section */
            .featured-products {
                max-width: 1200px;
                margin: 0 auto;
                padding: 2rem 1rem;
            }

            .featured-products h2 {
                text-align: center;
                font-size: 2rem;
                margin-bottom: 2rem;
                color: var(--primary-color);
            }

            .product-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 2rem;
            }

            .product-card {
                background: white;
                border-radius: 10px;
                padding: 1rem;
                text-align: center;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease;
            }

            .product-card:hover {
                transform: translateY(-5px);
            }

            .product-card img {
                width: 100%;
                height: 200px;
                object-fit: cover;
                border-radius: 5px;
                margin-bottom: 1rem;
            }

            .product-card h3 {
                margin-bottom: 0.5rem;
                color: var(--accent-color);
            }

            .product-card p {
                font-size: 0.95rem;
                margin-bottom: 1rem;
            }

            .btn {
                display: inline-block;
                padding: 0.5rem 1rem;
                background-color: var(--primary-color);
                color: white;
                border-radius: 5px;
                transition: background-color 0.3s ease;
            }

            .btn:hover {
                background-color: var(--secondary-color);
            }

            /* Footer */
            footer {
                text-align: center;
                padding: 2rem;
                background-color: var(--accent-color);
                color: white;
                margin-top: 3rem;
            }

            /* Meme Image for Debug or Branding */
            img[alt="meme image"] {
            }
        </style>
    </head>
    <body onscroll="repeat()">
        <header>
            <nav>
                <div class="logo">
                </div>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/products">Products</a></li>
                    <li><a href="/reports/generate">Reports</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/contact">Contact</a></li>
                </ul>
            </nav>
        </header>

        <main>
            <section class="hero">
                <h1>Welcome to Halib Al-Khair</h1>
                <p>Delivering the finest dairy products since 1985</p>
            </section>
            
 Hello,<div id="shit">
            <img src='/static/images/lol.png'>
            <img src='/static/images/lol.png'>
            <img src='/static/images/lol.png'>
            <img src='/static/images/lol.png'>
            <img src='/static/images/lol.png'>
            <img src='/static/images/lol.png'>
            <img src='/static/images/lol.png'>
            <img src='/static/images/lol.png'>
            <img src='/static/images/lol.png'>
            <img src='/static/images/lol.png'>
            <img src='/static/images/lol.png'>
            <img src='/static/images/lol.png'>
            <img src='/static/images/lol.png'>
            <img src='/static/images/lol.png'>
        </div> %s
        <!-- %s -->
            <section class="featured-products">
                <h2>Our Premium Products</h2>
                <div class="product-grid">
                    <div class="product-card">
                        <h3>Fresh Milk</h3>
                        <p>Farm-fresh whole milk</p>
                        <a href="/products?id=1" class="btn">Learn More</a>
                    </div>
                    <div class="product-card">
                        <h3>Natural Yogurt</h3>
                        <p>Creamy and healthy</p>
                        <a href="/products?id=2" class="btn">Learn More</a>
                    </div>
                    <!-- Add more products as needed -->
                </div>
            </section>
        </main>

        <footer>
            <p>&copy; 2024 Halib Al-Khair. All rights reserved.</p>
        </footer>

        <script>
            function repeat() {
                for (var i = 0; i < 10; i++) {
                    var lol = document.createElement("img");
                    lol.src = "/static/images/lol.png";
                    var shit = document.getElementById('shit');
                    shit.appendChild(lol);
                }
            }
        </script>
    </body>
    </html>
    """

    return render_template_string(template, secret=secret, hint=hint)


if __name__ == "__main__":
    app.run(debug=True)
