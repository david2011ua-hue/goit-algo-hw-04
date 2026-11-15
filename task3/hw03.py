import sys
from pathlib import Path

from colorama import Fore, Style, init

# autoreset=True — колір автоматично скидається після кожного print
init(autoreset=True)


def print_tree(directory: Path, indent: str = "") -> None:
    """Рекурсивно виводить структуру директорії з кольорами."""
    try:
        # Спочатку папки, потім файли; всередині — за алфавітом
        items = sorted(directory.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    except PermissionError:
        print(f"{indent}{Fore.RED}[немає доступу]")
        return

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        connector = "┗ " if is_last else "┣ "

        if item.is_dir():
            print(f"{indent}{connector}{Fore.BLUE}{Style.BRIGHT}📂 {item.name}")
            next_indent = indent + ("  " if is_last else "┃ ")
            print_tree(item, next_indent)
        else:
            print(f"{indent}{connector}{Fore.GREEN}📜 {item.name}")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"{Fore.YELLOW}Використання: python hw03.py /шлях/до/директорії")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"{Fore.RED}Помилка: шлях '{path}' не існує.")
        sys.exit(1)

    if not path.is_dir():
        print(f"{Fore.RED}Помилка: '{path}' не є директорією.")
        sys.exit(1)

    print(f"{Fore.MAGENTA}{Style.BRIGHT}📦 {path.resolve().name}")
    print_tree(path)


if __name__ == "__main__":
    main()
