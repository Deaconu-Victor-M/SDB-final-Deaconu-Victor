from terminaltables import SingleTable
from models.promotions import Promotions
from ui.console_messages import stop
import ui.console_delete as console
from UI_main.console_admin import MenuAdmin
from UI_main.console_client import MenuClient
import ui.console_one_line as col


products_instace_list = []
cart_instance_list = []
promotions_instance_list =[]

from utils.take_data import import_data
import_data(products_instace_list, cart_instance_list,
            promotions_instance_list)

admin = MenuAdmin(products_instace_list, cart_instance_list,
                  promotions_instance_list)
client = MenuClient(products_instace_list,
                    cart_instance_list, promotions_instance_list)


options_users = [
    ["Key", "User"],
    ["1", "Admin"],
    ["2", "Client"],
    ["a", "About"],
    ["e", "Exit"],
]


def show_menu_user():
    while True:
        console.clear_console()
        option_table = SingleTable(options_users, title="Users")
        option_table.justify_columns = {
             0: "center",
             1: "left"
        }
        print(option_table.table)
        selected = input("> ")
        if selected == "e"or selected == "E":
            stop()
            quit()
        elif selected == "a" or selected == "A":
            col.show(
                title="About",
                message="Made by: Deaconu Victor || final project SDB || August 2021"
            )
        else:
            try:
                if selected == "1":
                    admin.admin_menu()
                if selected == "2":
                    client.client_menu()
            except KeyError:
                print("Invalid option!")
