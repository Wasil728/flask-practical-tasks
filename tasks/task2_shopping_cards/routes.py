from flask import Blueprint, render_template

task2_bp = Blueprint('task2', __name__, template_folder='templates')

@task2_bp.route('/')
def index():
    # List of 8 products
    products_list = [
        {"name": "Laptop", "price": 50000, "category": "Electronics", "discount": 2000, "image": "images/dock.svg"},
        {"name": "Smartphone", "price": 20000, "category": "Electronics", "discount": 1000, "image": "images/camera.svg"},
        {"name": "Headphones", "price": 2000, "category": "Accessories", "discount": 200, "image": "images/headphones.svg"},
        {"name": "Keyboard", "price": 1000, "category": "Accessories", "discount": 100, "image": "images/keyboard.svg"},
        {"name": "Mouse", "price": 500, "category": "Accessories", "discount": 50, "image": "images/mouse.svg"},
        {"name": "Monitor", "price": 10000, "category": "Electronics", "discount": 500, "image": "images/smartwatch.svg"},
        {"name": "Speaker", "price": 1500, "category": "Audio", "discount": 150, "image": "images/speaker.svg"},
        {"name": "Powerbank", "price": 800, "category": "Accessories", "discount": 80, "image": "images/powerbank.svg"}
    ]

    # calculate final price for each product
    for product in products_list:
        product['final_price'] = product['price'] - product['discount']

    return render_template('task2_shopping_cards/index.html', products=products_list)
