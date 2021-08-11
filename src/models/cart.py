from models.products import Products


class Cart:
    """Class for the products  in the client's shopping cart

    Args:
    name (str): Name of the product that the client took
    bar_code (str): Bar code of the product
    quantity_taken (int) = The quantity the tha client took of one product
    tot_price_prod (float) = The price of the total quantity of one product
    """

    def __init__(self, bar_code: str, name: str, quantity_taken: int, tot_price_prod: float) -> None:
        self.bar_code = bar_code
        self.name = name
        self.quantity_taken = quantity_taken
        self.tot_price_prod = tot_price_prod
