import json


def save_data(mode: str = "complete", only: str = None, product_instance_list: list = None, cart_instance_list: list = None, promotions_instance_list: list = None) -> None:
    """
    Save products in shop // cart 

    Args:
        mode (str, optional): "complete"/"single". Defaults to "complete".
        only (str, optional): If None saves all
        product_instance_list(list, optional): Instance list of the products in the supermarket
        cart_instance_list(list, optional): Instance list of the products in the cart

    """
    
    if mode == "complete":
        if product_instance_list is not None and cart_instance_list is not None:
            save_all(product_instance_list, cart_instance_list,
                     promotions_instance_list)
        else:
            raise ValueError("For complete mode, bot instance lists must have at  least 1  argument")
    elif mode  == "single":
        if only == "products":
            if product_instance_list is not None:
                proccess_save_product(product_instance_list)
            else: 
                raise ValueError("The product_instance_list must not be  None")
        elif only == "cart":
            if cart_instance_list is not None:
                proccess_save_cart(cart_instance_list)
            else:
                raise ValueError("The cart_instance_list must not be None")
        elif only == "promotion":
            if promotions_instance_list is not None:
                proccess_save_promotions(promotions_instance_list)
        else:
            raise AttributeError(
                "Invalid \"only\" argument! Valid args: products or cart")
    else:
        raise AttributeError("Available modes: complete and single")


def save_all(product_instance_list: list, cart_instance_list: list, promotions_instance_list: list) -> None:
    proccess_save_product(product_instance_list)
    proccess_save_cart(cart_instance_list)
    proccess_save_promotions(promotions_instance_list)

def proccess_save_product(product_instance_list: list) -> None:
    """
    Saving the data in the products.json file 
    (for admins to add products)

    Args:
        product_instance_list (list): Instance list of the products in the supermarket
    """
    with open("data/products.json", 'w') as products_file:
        products_ = []
        for product in product_instance_list:
            products_.append(
                {
                    "bar_code": product.bar_code,
                    "name": product.name,
                    "price": product.price,
                    "firm": product.firm,
                    "quantity": product.quantity,
                    "promotion": product.promotion
                }
            )
        _save = {"products": products_}
        json.dump(
            _save,
            products_file,
            indent=2
        )


def proccess_save_cart(cart_instance_list: list) -> None:
    """
    Saving the data in the cart.json file 
    (for clients to add products in the cart & save them)

    Args:
        cart_instance_list (list): Instance list of the products in the cart
    """
    with open("data/cart.json", 'w') as cart_file:
        products_ = []
        for product in cart_instance_list:
            products_.append(
                {
                    "bar_code": product.bar_code,
                    "name": product.name,
                    "quantity_taken": product.quantity_taken,
                    "tot_price_prod": product.tot_price_prod
                }
            )
        _save = {"cart": products_}
        json.dump(
            _save,
            cart_file,
            indent=2
        )


def proccess_save_promotions(promotions_instance_list: list) -> None:
    """
    Saving the data in the promotions.json file 
    (for admin to add promotions to certain products

    Args:
        promotions_instance_list (list): Instance list of the promotions in the supermarket
    """
    with open("data/promotions.json", 'w') as promotions_file:
        products_ = []
        for product in promotions_instance_list:
            products_.append(
                {
                    "bar_code": product.bar_code,
                    "name": product.name,
                    "firm": product.firm,
                    "promotion": product.promotion
                }
            )
        _save = {"promotions": products_}
        json.dump(
            _save,
            promotions_file,
            indent=2
        )
    
