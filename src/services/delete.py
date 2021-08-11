from models.products import Products
from models.cart import Cart
import ui.console_delete as console
import ui.console_one_line as col
from terminaltables import SingleTable
from utils.repo import Repo
from utils.check_imputs import Checker
from utils.save_data import save_data
from ui.console_messages import warning

#? Admin
def do_remove_product(product_entity: Repo, checker: Checker):
    done_barcode = False
    _, products_list = product_entity.get()

    while not done_barcode:
        barcode = input("Enter the product's Bar Code that you want to remove (b/B to go back): ")
        if barcode == "":
            table_data = [["Bar Code", "Product"]]
            for product in products_list:
                table_data.append([str(product.bar_code), product.name])
            product_table = SingleTable(table_data, title="Products")
            product_table.justify_columns = {
                0: "center",
                1: "left",
            }
            console.clear_console()
            print(product_table.table)
        elif barcode == "b" or barcode == "B" or barcode == "back":
            break
        else:
            exists = False
            if isinstance(products_list[0], Products):
                for product in products_list:
                    if barcode == product.bar_code:
                        exists= True

            if exists == True:
                done_barcode = True
                product_entity.delete(barcode)
                _, products_instance_list = product_entity.get()
                save_data(
                    mode="single",
                    only="products",
                    product_instance_list=products_instance_list,
                )
                col.show(
                    title="Success",
                    message="The product was removed successfully"
                )
            else:
                console.clear_console()
                col.show(
                    title="Info",
                    message="Invalid Bar Code!",
                    go_back=False
                )

#!Client remove  from cart