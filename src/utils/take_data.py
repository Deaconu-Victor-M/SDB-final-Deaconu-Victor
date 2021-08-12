import json
from models.products import Products
from models.cart import Cart
from models.promotions import Promotions

def import_data(product_instace_list: list, cart_instace_list: list, promotions_instance_list: list) -> None:
    try:
        with open ("data/products.json", 'r') as products_file:
            json_ = json.load(products_file)
            products_ = json_["products"]
            for product_ in products_:
                product_instace_list.append(
                    Products(
                        product_["bar_code"],
                        product_["name"],
                        product_["price"],
                        product_["firm"],
                        product_["quantity"],
                        product_["promotion"],
                        product_["month"],
                        product_["year"]
                    )
                )
    except FileNotFoundError:
        print("[WARNING] products.json doesn't exist! -> Products not loaded")

    try:
        with open("data/cart.json", 'r') as cart_file:
            json_ = json.load(cart_file)
            cart_products_ = json_["cart"]
            for cart_product_ in cart_products_:
                cart_instace_list.append(
                    Cart(
                        cart_product_["bar_code"],
                        cart_product_["name"],
                        cart_product_["quantity_taken"],
                        cart_product_["tot_price_prod"]
                    )
                )
    except FileNotFoundError:
        print("[WARNING] cart.json doesn't exist! -> Cart not loaded loaded")

    try:
        with open("data/promotions.json", 'r') as promotions_file:
            json_ = json.load(promotions_file)
            promotions_ = json_["promotions"]
            for promotion in promotions_:
                promotions_instance_list.append(
                    Promotions(
                        promotion["bar_code"],
                        promotion["name"],
                        promotion["firm"],
                        promotion["promotion"],
                        promotion["month"],
                        promotion["year"]
                    )
                )
    except FileNotFoundError:
        print("[WARNING] promotions.json doesn't exist! -> Promotions not loaded loaded")
