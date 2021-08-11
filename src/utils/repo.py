from typing import Tuple
from ui.console_messages import warning, fail


class Repo:
    def __init__(self, instance_list: list):
        self.instance_list = instance_list

    def get(self, mode: str = "all", entity_id: str = None) -> Tuple[str, list or object]:
        if mode == "all":
            return ("found", self.instance_list)
        elif mode == "single":
            if entity_id is not None:
                for instance in self.instance_list:
                    if instance.bar_code == entity_id:
                        return ("found", instance)
                return ("not_found", None)
            else:
                warning("In single mode, entity_id must not be None")
                return ("failed", None)
        elif mode == "last":
            if len(self.instance_list) == 0:
                return ("not_found", None)
            return ("found", self.instance_list[-1])
        else:
            warning(
                "Invalid mode! Available modes: \"all\"(default), \"single\" or \"last\"")
            return ("failed", None)

    def add(self, entity: object) -> Tuple[str, str]:
        try:
            response, _ = self.get("single", entity)
            if response == "not_found":
                self.instance_list.append(entity)
                return ("ok", "Added successfully")
            elif response == "found":
                return ("warn", "This already exists")
            else:
                fail("Fail in repo::get")
                return ("fail", "Something went wrong")
        except Exception as e:
            fail(e)
            return ("fail", "Something went wrong")

    def delete(self, entity_code: str) -> Tuple[str, str]:
        resp, entity = self.get(mode="single", entity_id= entity_code)
        if resp == "found":
            self.instance_list.remove(entity)
            return ("ok", "Deleted successfully")
        else:
            return ("warn", "Not found, maybe already deleted")

    def update(self, type_of_entity: str, entity_id: str, **kwargs) -> Tuple[str, str]:

        #updating a product
        if type_of_entity == "product":
            search, entity = self.get(mode="single", entity_id=entity_id)
            if search == "found":
                if "bar_code" in kwargs and kwargs["bar_code"] is not None:
                    entity.bar_code = kwargs["bar_code"]
                if "price" in kwargs and kwargs["price"] is not None:
                    entity.price = kwargs["price"]
                if "firm" in kwargs and kwargs["firm"] is not None:
                    entity.firm = kwargs["firm"]
                if "quantity" in kwargs and kwargs["quantity"] is not None:
                    entity.quantity = kwargs["quantity"]
                if "promotion" in kwargs and kwargs["promotion"] is not None:
                    entity.promotion = kwargs["promotion"]
                return ("ok", "Updated successfully")
            else:
                return ("fail", "Not found")

        #updating a product form the cart
        elif type_of_entity == "cart":
            search, entity = self.get(mode="single", entity_id=entity_id)
            if search == "found":
                if "quantity_taken" in kwargs and kwargs["quantity_taken"] is not None:
                    entity.quantity_taken = kwargs["quantity_taken"]
                if "tot_price_prod" in kwargs and kwargs["tot_price_prod"] is not None:
                    entity.tot_price_prod = kwargs["tot_price_prod"]
                return ("ok", "Updated successfully")
            else:
                return ("fail", "Not found")

        #updating the quantity of the product left after Client added it inside the cart
        elif type_of_entity == "QUANTITY":
            search, entity = self.get(mode="single", entity_id=entity_id)
            if search == "found":
                if "quantity" in kwargs and kwargs["quantity"] is not None:
                    entity.quantity = kwargs["quantity"]
                return ("ok", "Updated successfully")
            else:
                return ("fail", "Not found")
        
        #update if product has promotion
        elif type_of_entity == "PROMOTIONS":
            search, entity = self.get(mode="single", entity_id=entity_id)
            if search == "found":
                if "promotion" in kwargs and kwargs["promotion"] is not None:
                    entity.promotion = kwargs["promotion"]
                return ("ok", "Updated successfully")
            else:
                return ("fail", "Not found")
        else:
            raise AttributeError("Invalid entity")
