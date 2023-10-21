from enum import Enum

PREFIX = "mahjong"
ji_list = ["ton", "nan", "sha", "pe", "haku", "hatsu", "tyun"]

class TileType(Enum):
    Man = "man"
    Pin = "pin"
    Sou = "sou"
    Ji = "ji"

def convert_to_message(number: int, tile_type: TileType):
    if tile_type == TileType.Ji:
        if number < 1 or number > 7:
            raise ValueError('{} is not valid tile number.'.format(number))
        return PREFIX + ji_list[number - 1]
    return PREFIX + str(number) + tile_type.value

def convert_chinitsu_str_to_message(tiles: str, tile_type: TileType):
    message = ""
    for tile in tiles:
        message += convert_to_message(int(tile), tile_type)
    return message