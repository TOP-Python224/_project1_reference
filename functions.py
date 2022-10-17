"""Дополнительный модуль: вспомогательные функции."""

# импорт из стандартной библиотеки
from pathlib import Path
from sys import path
from configparser import ConfigParser


# импорт дополнительных модулей
import data


# переменные модуля
script_dir = Path(path[0])
players_ini_path = script_dir / 'players.ini'
saves_ini_path = script_dir / 'saves.ini'


# работа с данными
def read_ini() -> bool:
    """Читает конфигурационные файлы, сохраняет прочитанные данные в глобальные переменные статистики и сохранений и возвращает True если приложение запущено впервые, иначе False."""
    # players.ini -> data.STATS
    players = ConfigParser()
    players.read(players_ini_path)
    for player in players.sections():
        data.STATS[player] = {
            k: int(v) if v.isdecimal() else v
            for k, v in players[player].items()
        }
    # saves.ini -> data.SAVES
    # saves = ConfigParser()
    # saves.read(saves_ini_path)
    # отсутствие сохранённых ранее имён игроков трактуем как первый запуск приложения
    if data.STATS:
        return False
    else:
        return True


def write_ini():
    """Записывает конфигурационные файлы, из глобальных переменных статистики и сохранений."""
    # data.STATS -> players.ini
    players = ConfigParser()
    for player in data.STATS:
        players[player] = data.STATS[player]
    with open(players_ini_path, 'w', encoding='utf-8') as f_out:
        players.write(f_out)
    # data.SAVES -> saves.ini
    # saves = ConfigParser()
    # with open(saves_ini_path, 'w', encoding='utf-8') as f_out:
    #     saves.write(f_out)


def draw_board(align_right: bool = False) -> str:
    """Формирует и возвращает строку, содержащую псевдографическое изображение игрового поля с сделанными ходами."""


# тесты
if __name__ == '__main__':
    read_ini()
    print(data.STATS)
