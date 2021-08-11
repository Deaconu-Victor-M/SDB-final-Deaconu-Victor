from terminaltables import SingleTable
from models.products import Products
from utils.check_imputs import  Checker
from utils.repo import Repo
from utils.save_data import save_data
import ui.console_delete as console
import ui.console_one_line as col
from ui.console_messages import warning

def do_update_product(product_entity: Repo, checker: Checker):
    get_barcode = False
    exists = False
    _, products_list= product_entity.get()

    while not get_barcode:
        barcode = input("Enter Bar Code or leave blank to se the products (b/B to go back): ")
        barcode_update= str(barcode)
        if barcode == "b" or barcode == "B" or barcode == "back":
            break
        elif barcode == "":
            table_data = [["Bar Code", "Product", "Quantity", "Price"]]
            for product in products_list:
                table_data.append([str(product.bar_code), product.name, str(product.quantity), str(product.price)])
            products_table= SingleTable(table_data, title = "Products")
            products_table.justify_columns = {
                0: "center",
                1: "left",
                2: "center",
                3: "center",
            }  
            console.clear_console()
            print(products_table.table)
        else:
            barcode = str(barcode)
            if isinstance(products_list[0], Products):
                for product in products_list:
                    if product.bar_code == barcode:
                        exists= True
                        name_title= product.name
                get_barcode = True
                done_quantity = False
                done_price = False
                new_barcode = None
                
                #?change Bar Code
                new_barcode = input(
                    f"If you want to change the Bar Code of {name_title} enter it now (leave blank to skip): ")
                if new_barcode != "":
                    #bad_barcode = False
                    try:
                        barcode_int = int(new_barcode)
                        if barcode_int <= 99999 or barcode_int > 999999:
                            console.clear_console()
                            col.show(
                                title="Info",
                                message="the Bar Code must be a 6 digit numeric value (ex: 123456)",
                            )
                            break
                            #bad_barcode = True
                        else:
                            new_barcode = str(new_barcode)
                    except ValueError:
                        console.clear_console()
                        col.show(
                            title="Info",
                            message="the Bar Code must be a 6 digit numeric value (ex: 123456)",
                        )
                        break
                else:
                    new_barcode = None


                #?change quantity
                while not done_quantity:
                    new_quantity = input(
                        f"If you want to change the quantity of {name_title} enter it now (leave blank to skip): ")
                    if new_quantity == "":
                        new_quantity = None
                        done_quantity= True
                    else:
                        try:
                            new_quantity = int(new_quantity)
                            print(new_quantity)
                            done_quantity = True
                        except ValueError:
                            col.show(
                                title="Info",
                                message="Invalid Quantity! Quantity must be a numeric(int) value"
                            )
                
                #?change firm
                new_firm = input(
                    f"If you want to change the firm of {name_title} enter it now (leave blank to skip): ")
                if new_firm == "":
                    new_firm = None
                else:
                    print(new_firm)

                #?change price

                while not done_price:
                    new_price = input(
                        f"If you want to change the price of {name_title} enter it now (leave blank to skip): ")
                    if new_price == "":
                        new_price = None
                        done_price = True
                    else:
                        try:
                            new_price = float(new_price)
                            print(new_price)
                            done_price = True
                        except ValueError:
                            col.show(
                                title="Info",
                                message="Invalid Quantity! Quantity must be a numeric(float) value"
                            )
            else:
                console.clear_console()
                col.show(
                    title="Info",
                    message="Invalid Bar Code!",
                    go_back=False
                )

            if exists == True:
                product_entity.update(
                    type_of_entity="product",
                    entity_id=barcode,
                    bar_code=new_barcode,
                    price=new_price,
                    firm=new_firm,
                    quantity=new_quantity,
                )

                save_data(
                    mode="single",
                    only="products",
                    product_instance_list=products_list
                )
                col.show(
                    title="Success",
                    message="The product was updated successfully"
                )
