from terminaltables import SingleTable
import ui.console_delete as console


def show(title:  str, message: str, go_back: bool = True):
    if go_back:
        while True:
            table_message = [[message]]
            table = SingleTable(table_message, title=title)
            console.clear_console()
            print(table.table)
            input_ = input("Type B/b or back to go back: ")
            if input_ == "b" or input_ == "B" or input_ == "back":
                break
            else:
                continue
    else:
        table_message = [[message]]
        table = SingleTable(table_message, title=title)
        console.clear_console()
        print(table.table)
