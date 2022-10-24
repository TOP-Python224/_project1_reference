"""Дополнительный модуль: партия."""

# импорт дополнительных модулей
import data


def human_turn(training: bool = False) -> int:
    """Запрашивает у игрока и возвращает корректную координату ячейки поля для текущего хода."""


def bot_turn(token_index: int, training: bool = False) -> int:
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


def game() -> data.Score | None:
    """Управляет игровым процессом для каждой новой или загруженной партии."""


# тесты
if __name__ == '__main__':
    print(check_win())
