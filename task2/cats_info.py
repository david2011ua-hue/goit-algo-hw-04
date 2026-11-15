from pathlib import Path


def get_cats_info(path):
    """
    Читає файл з інформацією про котів (формат рядка: "id,ім'я,вік")
    і повертає список словників з ключами "id", "name", "age".
    """
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue  # пропускаємо порожні рядки

                try:
                    cat_id, name, age = line.split(",")
                    cats.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Рядок {line_number} пошкоджений і пропущений: {line}")

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
    except (OSError, UnicodeDecodeError) as error:
        print(f"Помилка читання файлу: {error}")

    return cats


if __name__ == "__main__":
    cats_file = Path(__file__).parent / "cats_file.txt"
    cats_info = get_cats_info(cats_file)
    print(cats_info)
