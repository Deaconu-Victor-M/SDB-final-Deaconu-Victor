from terminaltables import SingleTable
from UI_main.console_menu_options import Options
from ui.console_messages import stop
import ui.console_delete as console


class MenuClient:
    def __init__(self, product_instance_list: list, cart_instance_list: list, promotions_instance_list: list):
        self.product_instance_list = product_instance_list
        self.cart_instance_list = cart_instance_list
        self.promotions_instance_list = promotions_instance_list
        self.options = Options(self.product_instance_list,
                               self.cart_instance_list,
                               self.promotions_instance_list)

        self.client_options = [
            ["key", "Commands"],
            ["1", "Buy products"],
            ["2", "Show all products"],
            ["3", "Show  products under X price"],
            ["4", "Show products with promotions"],
            ["5", "Show cart"],
            ["b", "Back"],
            ["e", "Exit"],

        ]

        self.options = {
            "1": self.options.add_cart,
            "2": self.options.show_products,
            "3": self.options.show_products_under,
            "4": self.options.show_product_promo,
            "5": self.options.show_cart,
        }

    def client_menu(self):
        while True:
            console.clear_console()
            option_table = SingleTable(self.client_options, title="Admin Menu")
            option_table.justify_columns = {
                0: "center",
                1: "left"
            }
            print(option_table.table)
            selected = input("> ")
            if selected == "b" or selected == "B" or selected == "back":
                break
            elif selected == "e"or selected == "E":
                stop()
                quit()
            else:
                try:
                    self.options[selected]()
                except KeyError:
                    print("Invalid option!")
