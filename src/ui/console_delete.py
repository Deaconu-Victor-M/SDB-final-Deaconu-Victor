import os
import platform


def clear_console():
    """
    Clears the console
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
