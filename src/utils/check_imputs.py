from models.products import Products
#from models.cart import Cart
from models.promotions import Promotions
from ui.console_messages import fail
from utils.repo import Repo


class Checker:
    def __init__(self, entity_: Repo):
        self.entity_ = entity_

    def check_if_exists(self, bar_code: str = None) -> bool or None:
        if bar_code is not None:
            _, entity_list = self.entity_.get()
            if isinstance(entity_list[0], Products):
                for entity in entity_list:
                    if entity.bar_code is bar_code:
                        return True
        else:
            fail("bar_code Must not be None in utils::input_checker")
            return None

    def check_if_exists_promo(self, bar_code: str = None) -> bool or None:
        if bar_code is not None:
            _, entity_list = self.entity_.get()
            if isinstance(entity_list[0], Promotions):
                for entity in entity_list:
                    if entity.bar_code == bar_code:
                        return True
                return False
        else:
            fail("bar_code Must not be None in utils::input_checker")
            return None

