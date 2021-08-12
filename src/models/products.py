from models.promotions import Promotions


class Products:
    """
    Class for the products in the supermarket
    
    Args:
        bar_code (str): Bar Code product
        name (str): Name of the product
        price (float): Price of the product / piece
        firm (str): The firm of which the product came from
        quantity (int):Number of said product in the supermarket
    """

    def __init__(self, bar_code: str, name: str, price: float, firm: str, quantity: int, promotion: int, month: int, year: int) -> None:
        self.bar_code = bar_code
        self.name = name
        self.price = price
        self.firm = firm
        self.quantity = quantity
        self.promotion = promotion
        self.month = month
        self.year = year