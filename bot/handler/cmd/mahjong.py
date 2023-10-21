import random
from mahjong import agari
from mahjong.tile import TilesConverter

def chinitsu_tehai_generator() -> str:
    tiles = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    tiles_tmp = random.choices(tiles, k=13)
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
