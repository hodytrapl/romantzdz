
# блок схема 1
flowchart TD
    Start([Начало]) --> LoadText[Загрузка текста\nload_text()]
    LoadText --> CheckText{Текст не пуст?}
    CheckText -- Нет --> End([Конец])
    CheckText -- Да --> ShowMenu[Показать меню\nshow_menu()]
    
    ShowMenu --> WaitChoice[Ожидание ввода выбора]
    WaitChoice --> Choice{Выбор пользователя}
    
    Choice -- 0 --> Exit([Выход])
    Choice -- от 1 до N --> GetAction[Получить пункт из MENU_ACTIONS\n(описание, модуль, функция)]
    GetAction --> ImportModule[Импорт модуля\nimportlib.import_module]
    ImportModule --> GetFunc[Получить функцию\ngetattr]
    GetFunc --> CallFunc[Выполнить функцию\nfunc(text)]
    CallFunc --> PrintResult[Вывод результата]
    PrintResult --> ShowMenu
    
    Choice -- неверный --> ShowError[Сообщение об ошибке]
    ShowError --> ShowMenu

    subgraph "Внешние зависимости"
        Mapping[mapping.py\nMENU_ACTIONS]
        Modules[Модули в папке modules/\nкаждый содержит функцию]
    end

    GetAction -.-> Mapping
    ImportModule -.-> Modules
    GetFunc -.-> Modules