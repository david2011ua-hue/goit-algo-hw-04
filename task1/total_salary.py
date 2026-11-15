from pathlib import Path


def total_salary(path):
    """
    Читає файл із зарплатами розробників (формат рядка: "Ім'я Прізвище,зарплата")
    і повертає кортеж (загальна сума, середня зарплата).
    """
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue  # пропускаємо порожні рядки

                try:
                    name, salary = line.split(",")
                    total += float(salary)
                    count += 1
                except ValueError:
                    print(f"Рядок {line_number} пошкоджений і пропущений: {line}")

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0
    except (OSError, UnicodeDecodeError) as error:
        print(f"Помилка читання файлу: {error}")
        return 0, 0

    if count == 0:
        return 0, 0

    average = total / count

    # Якщо числа цілі — повертаємо int, щоб вивід був "6000", а не "6000.0"
    if total.is_integer():
        total = int(total)
    if average.is_integer():
        average = int(average)

    return total, average


if __name__ == "__main__":
    salary_file = Path(__file__).parent / "salary_file.txt"
    total, average = total_salary(salary_file)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
