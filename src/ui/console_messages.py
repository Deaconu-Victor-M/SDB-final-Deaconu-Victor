def start():
    """
    Show the start message
    """
    print("[START] Booting...")


def stop():
    """
    Show the stop message
    """
    print("[STOP] Exiting...")


def warning(msg: str):
    """
    Show a warning message

    Args:
        msg (str): The message
    """
    print(f"[WARNING] {msg}")


def fail(error: Exception or str):
    """
    Show a fail message

    Args:
        error (Exception or str): The message or Exception
    """
    print(f"[FAIL] {error}")


def success(msg: str):
    """
    Show a success message

    Args:
        msg (str): The message
    """
    print(f"[SUCCESSFUL] {msg}")
