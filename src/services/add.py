from datetime import datetime
from models.products import Products
from models.cart import Cart
from models.promotions import Promotions
import ui.console_delete as console
import ui.console_one_line as col
from terminaltables import SingleTable
from utils.repo import Repo
from utils.check_imputs import Checker
from utils.save_data import save_data
from ui.console_messages import  warning


def do_add_product(product_entity:  Repo, checker: Checker):
    
    new_barcode = ""
    new_name = ""
    new_price = None
    new_firm = ""
    new_quantity = None
    new_promotion = -1
    new_month = -1
    new_year = -1
    barcode_int= None

    _, products_list = product_entity.get()
    done_barcode = False
    while not done_barcode:
        bad_barcode = False
        nup = False
        barcode = input("Enter the product's bar code: ")
        try:
            barcode_int = int(barcode)
            if barcode_int <= 99999 or barcode_int > 999999:
                console.clear_console()
                col.show(
                    title="Info",
                    message="the Bar Code must be a 6 digit numeric value (ex: 123456)",
                    go_back=False
                )
                bad_barcode = True
        except ValueError:
            console.clear_console()
            col.show(
                title="Info",
                message="the Bar Code must be a 6 digit numeric value (ex: 123456)",
                go_back=False
            )
            bad_barcode = True
        if isinstance(products_list[0], Products):
            for entity in products_list:
                if entity.bar_code == barcode:
                    nup = True
                    console.clear_console()
                    col.show(
                        title="Info",
                        message="This item already exists",
                        go_back=False
                    )
        if nup is False:
            new_barcode= barcode
            if not bad_barcode:
                done_barcode = True
                # else:
                #     new_barcode = barcode
                #     done_barcode = True
    
    new_name = input("Enter the product's name: ")
    new_name = str(new_name)

    done_price = False
    while not done_price:
        price = input("Enter product's price: ")
        try:
            price = float(price)
            if price > 0:
                new_price = float(price)
                done_price = True
            else:
                console.clear_console()
                col.show(
                    title = "Info",
                    message = "the price must be higher than 0",
                    go_back = False
                )
        except ValueError:
            console.clear_console()
            col.show(
                title = "Info",
                message = "the price must be a numeric value",
                go_back = False
            )

    new_firm = input("Enter product's firm: ")

    done_quantity = False
    while not done_quantity:
        quantity = input("Enter the quantity of the  product(press enter for None): ")
        quantity =int(quantity)
        if quantity == "":
            new_quantity = 0
            done_quantity = True
        elif quantity < 0:
            col.show(
                title="Info",
                message="The quantity must be higher than 0",
                go_back=False
            )
        else:
            try:
                new_quantity = int(quantity)
                done_quantity = True
            except ValueError:
                console.clear_console()
                col.show(
                    title="Info",
                    message="the price must be a numeric value",
                    go_back=False
                    ) 
    product_entity.add(Products(new_barcode, new_name, new_price, new_firm, new_quantity, new_promotion, new_month, new_year))
    _, products_instance_list = product_entity.get()
    save_data(
        mode="single",
        only="products",
        product_instance_list=products_instance_list
    )
    col.show(
        title="Success",
        message="[SUCCESSFUL] New product added in supermarket"
    )


def do_add_cart(cart_entity:  Repo, checker: Checker, product_entity: Repo):
    new_barcode = ""
    new_name = ""
    new_quantity_taken = None
    new_tot_price_prod = None
    updated_quantity = 0
    exists = False

    print("In order to add a new product to the cart you need to it's bar code and it's name")
    input_ = input("Press enter  to see all the products: ")
    if input_ == "":
        _, products_list = product_entity.get()
        _, cart_list = cart_entity.get()
        if len(products_list) == 0 or products_list is None:
            col.show(
                title="Something went wrong",
                message="No products available at the moment or something went wrong"
            )
        else:
            table_data = [["BarCode", "Product", "Price", "Quantity"]]
            for product in products_list:
                table_data.append([product.bar_code, product.name,
                                  str(product.price), str(product.quantity)])
            product_table = SingleTable(table_data, title="Products")
            product_table.justify_columns = {
                0: "center",
                1: "left",
                2: "center",
                3: "center",
            }
            done_all = False
            while not done_all:
                console.clear_console()
                print(product_table.table)
                barcode = input(
                    "Select your item by typing the Bar Code or press b/B togo back: ")
                if barcode == "b" or barcode == "B" or barcode == "back":
                    break
                elif barcode is not None:
                    if isinstance(products_list[0], Products):
                        for entity in products_list:
                            if entity.bar_code == barcode:
                                exists=True
                                new_barcode = barcode
                                new_name = entity.name
                                quantity_taken = input("Select the quantity you want to take: ")
                                quantity_taken = int(quantity_taken)
                                if quantity_taken <= entity.quantity:
                                    new_quantity_taken = quantity_taken
                                    updated_quantity = entity.quantity - quantity_taken
                                    new_tot_price_prod = int(
                                        entity.price * new_quantity_taken)
                                    done_all = True
                                else:
                                    warning("Number to big \n")
                        if exists:
                            cart_entity.add(Cart(new_barcode, new_name,
                                                 new_quantity_taken, new_tot_price_prod))
                            save_data(
                                mode="single",
                                only="cart",
                                cart_instance_list=cart_list
                            )
                            product_entity.update(
                                type_of_entity="QUANTITY",
                                entity_id=barcode,
                                quantity=updated_quantity
                            )
                            save_data(
                                mode="single",
                                only="products",
                                product_instance_list=products_list,
                            )
                            col.show(
                                title="Success",
                                message="[SUCCESSFUL] New product added in the cart"
                            )
                    else:
                        col.show(
                            title="Warning",
                            message="This Bar Code doesn't exist.",
                        )
    

def do_add_promotion(promotion_entity:  Repo, checker: Checker, product_entity: Repo):
    day = datetime.today()
    month_today = day.month
    year_today = day.year
    new_promotion = None
    new_barcode = ""
    new_name = ""
    new_firm = ""
    new_month = None
    new_year = None
    exists = False
    print("In order to add a new product to the cart you need to it's bar code and it's name")
    input_ = input("Press enter  to see all the products: ")
    if input_ == "":
        _, products_list = product_entity.get()
        _, promotions_list= promotion_entity.get()
        if len(products_list) == 0 or products_list is None:
            col.show(
                title="Something went wrong",
                message="No products available at the moment. Please add products in order to create promotions"
            )
        else:
            table_data = [["Bar Code", "Product",  "Price", "Firm", "Promotion(y/n)"]]
            for product in products_list:
                table_data.append([product.bar_code, product.name,
                                  str(product.price), product.firm, f"{product.promotion}%-[YES]" if product.promotion != -1 else "[NO]"])
            product_table = SingleTable(table_data, title="Products")
            product_table.justify_columns = {
                0: "center",
                1: "left",
                2: "center",
                3: "center",
                4: "center"
            }
            done_all = False
            while not done_all:
                console.clear_console()
                print(product_table.table)
                barcode = input(
                    "Select your product by typing the Bar Code or press b/B togo back: ")
                barcode = str(barcode)
                if barcode == "b" or barcode == "B" or barcode == "back":
                    break
                elif barcode is not None:
                    if checker.check_if_exists_promo(bar_code=barcode):
                        col.show(
                            title="Info",
                            message="This product already has a promotion"
                        )
                    elif isinstance(products_list[0], Products):
                        for product in products_list:
                            if  product.bar_code == barcode:
                                new_barcode = barcode
                                new_name = product.name
                                new_firm = product.firm
                                done_promo = False
                                while not done_promo:
                                    try:
                                        promotion = input(
                                            "Enter the promotion you want your product to have: ")
                                        promotion = int(promotion)
                                        if promotion > 0 and promotion <= 100:
                                            new_promotion = promotion
                                            done_promo = True
                                        elif promotion == 0:
                                            col.show(
                                                title="Info",
                                                message="Nothing has changed (promotion was 0.00%)"
                                            )
                                            break
                                        else:
                                            col.show(
                                                title="Info",
                                                message="Number to big or to small",
                                                go_back=False
                                            )
                                    except ValueError:
                                        col.show(
                                            title="Warning",
                                            message="The promotion must be numeric(int)",
                                            go_back=False
                                        )
                                done_year = False
                                while not done_year:
                                    try:
                                        year_input = input("Enter expiration year: ")
                                        year_input = int(year_input)
                                        if year_input >= year_today:
                                            new_year = year_input
                                            done_year = True
                                        else:
                                            col.show(
                                                title="Info",
                                                message="The year must be higher than today's year",
                                                go_back=False
                                            )
                                    except ValueError:
                                        col.show(
                                            title="Info",
                                            message="The year must be numeric(int) (higher than {year_today})",
                                            go_back=False
                                        )
                                done_month = False
                                while not done_month:
                                    try:
                                        month_input = input("Enter an expiration month: ")
                                        month_input = int(month_input)
                                        if new_year == year_today:
                                            if month_input >= month_today and month_input < 13:
                                                new_month = month_input
                                                exists = True
                                                done_all = True
                                                done_month = True
                                            else:
                                                col.show(
                                                    title="Info",
                                                    message="The month must be higher than or equal to today's month)",
                                                    go_back=False
                                                )
                                        elif month_input > 0 and month_input < 13:
                                            new_month =  month_input
                                    except ValueError:
                                        col.show(
                                            title="Info",
                                            message="The month must be numeric(int) (between 1 and 12)",
                                            go_back=False
                                        )
                if exists == True:
                    promotion_entity.add(Promotions(
                        new_barcode, new_name, new_firm, new_promotion, new_month, new_year))
                    save_data(
                        mode="single",
                        only="promotion",
                        promotions_instance_list=promotions_list
                    )
                    product_entity.update(
                        type_of_entity="product",
                        entity_id=barcode,
                        promotion=new_promotion,
                        month=new_month,
                        year=new_year
                    )
                    save_data(
                        mode="single",
                        only="products",
                        product_instance_list=products_list,
                    )
                    col.show(
                        title="Success",
                        message="[SUCCESSFUL] New promotion added",
                    )

