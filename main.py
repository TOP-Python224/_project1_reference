"""Модуль верхнего уровня: для учебного проекта Крестики-Нолики."""

# импорт дополнительных модулей
import data
import functions
import help
import gameset
import game


# 1. Чтение данных из текстовых файлов данных
# 2. ЕСЛИ первый запуск:
if functions.read_ini():
    # вывод раздела помощи
    help.show_help()
    pass

# 3. Запрос имени игрока
functions.get_player_name()

# суперцикл
while True:
    # 4. Ожидание ввода команды
    command = input(data.PROMPT)

    # new
    if command in data.COMMANDS['начать новую партию']:
        # 5. Запрос режима игры:
        gameset.game_mode()
        # партия
        res = game.game()
        # 19. Удаление автосохранения и обновление статистики
        functions.update_stats(res)

    elif command in data.COMMANDS['выйти из игры']:
        break

# 21. Обработка завершения работы приложения
