import importlib
from importlib import util
from ui.console_messages import fail, stop

REQUIRED_MODULES = [
    "os",
    "platform",
    "json",
    "typing",
    "terminaltables"
]


def check_imports() -> None:
    """
    Checks to see if all modules can be imported.
    """
    for module in REQUIRED_MODULES:
        spec = importlib.util.find_spec(module)
        wasFound = spec is not None
        if not wasFound:
            fail(
                f"Module {module} was not found! It is required, please read the README!")
            stop()
            quit()
