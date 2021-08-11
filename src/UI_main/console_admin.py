from terminaltables import SingleTable
from UI_main.console_menu_options import Options
from ui.console_messages import stop
import ui.console_delete as console



class MenuAdmin:
    def __init__(self, product_instance_list: list, cart_instance_list: list, promotions_instance_list: list):
        self.product_instance_list = product_instance_list
        self.cart_instance_list = cart_instance_list
        self.promotions_instance_list = promotions_instance_list
        self.options = Options(self.product_instance_list,
                               self.cart_instance_list,
                               self.promotions_instance_list)

        self.admin_options = [
            ["Key", "Commands"],
            ["1", "Add a product"],
            ["2", "Add a promotion"],
            ["3", "Remove a product"],
            ["4", "Update a product"],
            ["5", "Show all products"],
            ["6", "Show product from firm"],
            ["b", "Back"],
            ["e", "Exit"],
        ]

        self.options = {
            "1": self.options.add_product,
            "2": self.options.add_promotion,
            "3": self.options.remove_product,
            "4": self.options.update_product,
            "5": self.options.show_products,
            "6": self.options.show_product_firm,
        }

    def admin_menu(self):
        while True:
            console.clear_console()
            option_table = SingleTable(self.admin_options, title="Admin Menu")
            option_table.justify_columns = {
                0: "center",
                1: "left",
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
