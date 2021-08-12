import os
from terminaltables import SingleTable
from utils.check_imputs import Checker
from utils.repo import Repo
import ui.console_delete as console
import ui.console_one_line as col
from services import add, delete, update
from datetime import datetime


class Options:

    def __init__(self, products_instance_list: list, cart_instance_list: list, promotions_instance_list:  list):
        self.products_instance_list = products_instance_list
        self.cart_instance_list = cart_instance_list
        self.promotions_instance_list = promotions_instance_list

    #? Client + Admin
    def show_products(self):
        day = datetime.today()
        month_today = day.month
        year_today = day.year
        products_entity = Repo(self.products_instance_list)
        search, products_list = products_entity.get(mode="all")

        if search == "found" and len(products_list) != 0:
            table_data = [["Bar Code", "Product", "Price", "Firm", "Quantity", "Promotion"]]
            for product in products_list:
                price_w_promotion = float(product.price  * product.promotion / 100) if product.promotion != -1 else product.price
                table_data.append([product.bar_code, product.name,
                                  str(format(price_w_promotion,  ".2f")), product.firm, str(product.quantity),
                                  "[NO]" if product.promotion == -1 else f"{product.promotion}%-[ACTIVE]" if product.year >= year_today and product.month >= month_today or product.year >= year_today and product.month <= month_today else "[NO PROMOTION]" if product.promotion == -1 else "[INACTIVE]"])
            product_table = SingleTable(table_data, title="Products")
            product_table.justify_columns = {
                0: "center",
                1: "left",
                2: "center",
                3: "left",
                4: "center",
                5: "left"
            }
            while True:
                console.clear_console()
                print(product_table.table)
                input_ = input("Type b/B or back to go back: ")
                if input_ == "b" or input_ == "B" or input_ == "back":
                    break
                else:
                    continue
        elif len(products_list) == 0:
            col.show(
                title="Info",
                message="No products! You  can add themfrom the menu or by changing the files"
            )
        else:
            col.show(
                title="Something went wrong",
                message="Please try again"
            )

    #? client
    def show_cart(self):
        cart_entity = Repo(self.cart_instance_list)
        search, cart_list = cart_entity.get(mode="all")

        if search == "found" and len(cart_list) != 0:
            table_data = [["Bar Code", "Product", "Quantity", "Price", "Promotion"]]
            for product in cart_list:
                table_data.append([str(product.bar_code), product.name, str(
                    product.quantity_taken), str(product.tot_price_prod)])
            cart_table = SingleTable(table_data, title="Products")
            cart_table.justify_columns = {
                0: "center",
                1: "center",
                2: "center",
                3: "center",
            }
            while True:
                console.clear_console()
                print(cart_table.table)
                input_ = input("Type b/B or back to go back: ")
                if input_ == "b" or input_ == "B" or input_ == "back":
                    break
                else:
                    continue
        elif len(cart_list) == 0:
            col.show(
                title="Info",
                message="Your cart is empty! Plz go back and buy something"
            )
        else:
            col.show(
                title="Something went wrong",
                message="Please try again"
            )

    #? Client
    def show_products_under(self):
        products_entity = Repo(self.products_instance_list)
        #promo_entity = Repo(self.promotions_instance_list)
        search, products_list = products_entity.get(mode="all")
        #_, promo_list = promo_entity.get(mode="all")
        max_price = input("Type the maximum price of the products to be shown: ")
        max_price = float(max_price)
        exists = False
        if search == "found" and len(products_list) != 0:
            table_data = [["Bar Code", "Product", "Normal Price"]]
            for product in products_list:
                if product.price <= max_price:
                    exists = True
                    table_data.append([str(product.bar_code), product.name, str(product.price)])
            product_table = SingleTable(table_data, title=f"Price: {max_price}")
            product_table.justify_columns = {
                1: "center",
                2: "left",
                3: "center",
            }
            if exists == True:
                while True:
                    console.clear_console()
                    print(product_table.table)
                    back = input("Type b/B or back to go back: ")
                    if back == "b" or back == "B" or back == "back":
                        break
                    else:
                        continue
            else:
                col.show(
                    title="Info",
                    message=f"No products under {max_price}"
                )
    #? admin
    def show_product_firm(self):
        products_entity = Repo(self.products_instance_list)
        search, products_list = products_entity.get(mode="all")
        new_firm = input("Select a firm to show products from: ")
        exists = False
        if search == "found" and len(products_list) != 0:
            table_data =  [["Bar Code", "Products"]]
            for product in products_list:
                if product.firm == new_firm:
                    exists = True
                    table_data.append([str(product.bar_code), product.name])
            if exists:
                product_table = SingleTable(table_data, title=f"Firm: {new_firm}")
                product_table.justify_columns = {
                    1: "center",
                    2: "left",
                }
                while True:
                    console.clear_console()
                    print(product_table.table)
                    input_ = input("Type b/B or back to go back: ")
                    if input_ == "b" or input_ == "B" or input_ == "back":
                        break
                    else:
                        continue
            else:
                col.show(
                    title="Info",
                    message="There are no items from that firm"
                )

    def show_product_promo(self):
        day = datetime.today()
        month_today = day.month
        year_today = day.year
        promotion_entity = Repo(self.promotions_instance_list)
        search, promo_list = promotion_entity.get(mode="all")
        if search == "found" and len(promo_list) != 0:
            table_data = [["Bar Code", "Product", "Firm", "promotion", "Expiration date (mo/year)", "Activity"]]
            for product in promo_list:
                table_data.append([product.bar_code, product.name, product.firm, f"{product.promotion}%", f"{product.month}.{product.year}",
                    "[ACTIVE]" if product.year >= year_today and product.month >= month_today or product.year >= year_today and product.month <= month_today else "[INACTIVE]"])
            promo_table = SingleTable(table_data, title="Products")
            promo_table.justify_columns = {
                0: "center",
                1: "center",
                2: "center",
                3: "center",
                4: "center",
            }
            while True:
                console.clear_console()
                print(promo_table.table)
                input_ = input("Type b/B or back to go back: ")
                if input_ == "b" or input_ == "B" or input_ == "back":
                    break
                else:
                    continue
        elif len(promo_list) == 0:
            col.show(
                title="Info",
                message="No promotions today"
            )
        else:
            col.show(
                title="Something went wrong",
                message="Please try again"
            )

    #? Admin
    def add_product(self):
        console.clear_console()
        col.show(
            title="Add a product",
            message="To add a new product do the followings",
            go_back=False
        )
        products_repo = Repo(self.products_instance_list)
        checker = Checker(products_repo)
        add.do_add_product(products_repo, checker)

    #? Client
    def add_cart(self):
        console.clear_console()
        col.show(
            title="Add a product in the cart",
            message="To add a new product do the followings",
            go_back=False
        )
        cart_repo = Repo(self.cart_instance_list)
        products_repo = Repo(self.products_instance_list)
        checker = Checker(cart_repo)
        add.do_add_cart(cart_repo, checker, products_repo)
    
    #? Admin
    def add_promotion(self):
        console.clear_console()
        col.show(
            title="Add a promotion",
            message="To add a new promotion do the followings",
            go_back=False
        )
        promotions_repo = Repo(self.promotions_instance_list)
        products_repo = Repo(self.products_instance_list)
        checker = Checker(promotions_repo)
        add.do_add_promotion(promotions_repo, checker, products_repo)


    #? Admin
    def remove_product(self):
        console.clear_console()
        col.show(
            title="Remove a product",
            message="To remove a product please complete the details below",
            go_back=False
        )
        product_repo = Repo(self.products_instance_list)
        checker = Checker(product_repo)
        delete.do_remove_product(product_repo, checker)

    def update_product(self):
        console.clear_console()
        col.show(
            title="Update a product",
            message="To update a product please complete the details below",
            go_back=False
        )
        products_repo = Repo(self.products_instance_list)
        checker = Checker(products_repo)
        update.do_update_product(products_repo, checker)
