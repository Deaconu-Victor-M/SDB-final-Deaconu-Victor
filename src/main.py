def main():
    from ui.console_messages import start
    start()

    from utils.check_imports import check_imports
    check_imports()

    from UI_main.console_user import show_menu_user
    show_menu_user()
    
main()
