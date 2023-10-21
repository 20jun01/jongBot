import random
from mahjong import agari
from mahjong.tile import TilesConverter
from collections import Counter

def choices_with_limit(pool, k, limit):
    selected = []
    counts = Counter()

    for _ in range(k):
        available_choices = [item for item in pool if counts[item] < limit]
        if not available_choices:
            break
        choice = random.choice(available_choices)
        selected.append(choice)
        counts[choice] += 1

    return selected

def chinitsu_tehai_generator() -> str:
    tiles = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    tiles_tmp = choices_with_limit(tiles, 13, 4)
    tiles_tmp.sort()
    tiles_str = "".join(tiles_tmp)
    return tiles_str

def chinitsu_agari_check(tiles: str) -> bool:
    """
    tiles: str(len=14) (ex. "11123455678999")

    return: bool (True if agari)
    """
    ag = agari.Agari()
    tiles_34 = TilesConverter.one_line_string_to_34_array(tiles + "p")
    return ag.is_agari(tiles_34)
