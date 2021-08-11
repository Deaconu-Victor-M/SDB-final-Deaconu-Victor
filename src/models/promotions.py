class Promotions:
    """
    Class for the promotions of products in store

    Args:
        promotion (int):The promotion of the product
        bar_code (str): barcode of the product
        name (str): Nameofthe product
    """

    def __init__(self, bar_code: str, name: str, firm: str, promotion: int) -> None:
        self.bar_code = bar_code
        self.name = name
        self.firm = firm
        self.promotion = promotion
        
