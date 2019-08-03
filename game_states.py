from enum import Enum

class GameStates(Enum):
    PLAYERS_TURN = 1
    ENEMY_TURN = 2
    PLAYER_DEAD = 3
    SHOW_INVENTORY = 4
    DROP_INVENTORY = 5
    TARGETING = 6
    LEVEL_UP = 7
    CHARACTER_SCREEN = 8
    HELP_SCREEN = 9
    LOOK_AT = 10
    SHOW_PICKUP = 11
    CHARACTER_CREATION = 12
    RESTING = 13
