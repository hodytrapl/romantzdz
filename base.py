# main.py
"""
Главный скрипт системы анализа и трансформации текста.
Студенты добавляют свои модули в mapping.py и папку modules/.
Основной код не изменяется.
"""

import importlib
import sys

# Файл, связывающий пункты меню с именами модулей и функций
try:
    from mapping import MENU_ACTIONS
except ImportError:
    print("Ошибка: файл mapping.py не найден. Создайте его согласно инструкции.")
    sys.exit(1)


def load_text():
    """Загрузка текста из файла или ввод вручную."""
    choice = input("Загрузить текст из файла? (y/n): ").strip().lower()
    if choice == 'y':
        path = input("Введите путь к файлу: ").strip()
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Ошибка чтения файла: {e}")
            sys.exit(1)
    else:
        print("Введите текст (для завершения нажмите Enter дважды):")
        lines = []
        while True:
            line = input()
            if line == "" and lines and lines[-1] == "":
                break
            lines.append(line)
        return "\n".join(lines).strip()


def show_menu():
    """Отображение меню на основе зарегистрированных модулей."""
    print("\n===== Меню обработки текста =====")
    for idx, (desc, _, _) in enumerate(MENU_ACTIONS, 1):
        print(f"{idx}. {desc}")
    print("0. Выход")


def main():
    print("Добро пожаловать в систему обработки текста!")
    text = load_text()
    if not text:
        print("Текст пуст. Завершение работы.")
        return

    while True:
        show_menu()
        try:
            choice = int(input("Выберите действие: "))
        except ValueError:
            print("Введите число.")
            continue

        if choice == 0:
            print("До свидания!")
            break

        if 1 <= choice <= len(MENU_ACTIONS):
            _, module_name, function_name = MENU_ACTIONS[choice - 1]
            try:
                module = importlib.import_module(f"modules.{module_name}")
                func = getattr(module, function_name)
                result = func(text)
                print("\n--- Результат ---")
                print(result)
                print("-----------------\n")
            except Exception as e:
                print(f"Ошибка выполнения модуля: {e}")
        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()