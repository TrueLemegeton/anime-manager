import os


def pause_and_clear_console() -> None:
    """Pause the program and clear the console."""
    print()
    input('Нажмите Enter для продолжения...')
    os.system('cls' if os.name == 'nt' else 'clear')