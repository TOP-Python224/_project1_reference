"""Дополнительный модуль: партия."""

# импорт из стандартной библиотеки
from math import ceil

# импорт дополнительных модулей
import data
import functions
import bot


def human_turn() -> int | None:
    """Запрашивает у игрока и возвращает корректную координату ячейки поля для текущего хода."""


def bot_turn() -> int:
    """Вычисляет и возвращает координату ячейки поля для текущего хода бота в зависимости от сложности."""


def check_win() -> bool:
    """Проверяет текущую партию на наличие победной комбинации."""
    series = []
    main_diag, anti_diag = [], []
    for i in data.RANGE:
        series += [data.BOARD[i*data.DIM:(i+1)*data.DIM]]
        series += [data.BOARD[i::data.DIM]]
        main_diag += [data.BOARD[i+i*data.DIM]]
        anti_diag += [data.BOARD[(i+1)*data.DIM-i-1]]
    series += [main_diag, anti_diag]

    for seq in series:
        if len(set(seq)) == 1:
            if all(seq):
                return True
    return False


def game(loaded: bool = False) -> data.Score | None:
    """Управляет игровым процессом для каждой новой или загруженной партии."""
    turns = ((0, 1)*ceil(data.CELLS / 2))[:data.CELLS]
    if loaded:
        turns = turns[len(data.TURNS):]
    for i in turns:
        if data.PLAYERS[i] in ('#1', '#2'):
            # 14. Расчёт хода бота
            cell_index = bot_turn()
        else:
            # 12. Запрос хода игрока
            cell_index = human_turn()
            # б) ЕСЛИ ввод пустой:
            if cell_index is None:
                # сохранение незавершённой партии (используется автосохранение)
                return None
        # 15. Обновление глобальных переменных
        data.TURNS += [cell_index]
        data.BOARD[cell_index] = data.TOKENS[i]
        # выполнение автосохранения
        data.SAVES[tuple(data.PLAYERS)] = data.TURNS
        # обновление текстовых файлов данных
        functions.write_ini()
        # 16. ЕСЛИ обучение:
        if data.TRAINING:
            margin = (0, functions.gts()[0] - 1)[i]
            # вывод подписи, чей ход на игровом поле
            if data.PLAYERS[i] in ('#1', '#2'):
                print(' # это ход бота #'.rjust(margin))
            else:
                print(f' # это ход игрока {data.PLAYERS[i]} #'.rjust(margin))
        # 17. Вывод игрового поля со сделанным ходом
        functions.draw_board(bool(i))
        # 18. ЕСЛИ есть победная комбинация:
        if check_win():
            # вывести сообщение о победе i-того игрока
            # ...
            return ({'wins': (i+1)%2, 'fails': i%2, 'ties': 0},
                    {'wins': i%2, 'fails': (i+1)%2, 'ties': 0})
    # ЕСЛИ есть ничья
    return ({'wins': 0, 'fails': 0, 'ties': 1},
            {'wins': 0, 'fails': 0, 'ties': 1})


# тесты
if __name__ == '__main__':
    game()
