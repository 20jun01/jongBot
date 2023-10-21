import random
from mahjong import agari
from mahjong.tile import TilesConverter

def chinitsu_tehai_generator() -> list[str]:
    tiles = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return random.choices(tiles, k=13)

def chinitsu_agari_check(tiles: str):
    """
    tiles: str(len=14) (ex. "11123455678999")

    return: bool (True if agari)
    """

    ag = agari.Agari()
    tiles_34 = TilesConverter.one_line_string_to_34_array(tiles)
    return ag.is_agari(tiles_34)
