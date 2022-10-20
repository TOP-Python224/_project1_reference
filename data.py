"""Дополнительный модуль: глобальные переменные и константы."""


# глобальные переменные данных
STATS = {}
SAVES = {}

PLAYERS = []
TOKENS = ('X', 'O')

DIM = 3
RANGE = range(DIM)
RANGE_FLAT = range(DIM**2)

TURNS = []
BOARD = [''] * DIM**2

TRAINING = False

# глобальные константы
APP_TITLE = "КРЕСТИКИ-НОЛИКИ"
PROMPT = ' > '

COMMANDS = {
    'начать новую партию': ('game', 'партия', 'g', 'п'),
    'выйти из игры': ('quit', 'выход', 'q', 'в')
}
