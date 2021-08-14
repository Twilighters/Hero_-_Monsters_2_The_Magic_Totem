from enemy_factory import *
from items_factory import *
from player_classes import *

players_current_class = ""
players_current_weapon = "sword"
monster_counter = 0
hp = 10
attack = 10

monster_hp = 0
monster_attack = 0

spawner_to_factory_mapping = {
    "ogre": OgreFactory,
    "skeleton": SkeletonFactory,
    "goblin": GoblinFactory,
    "apple": AppleFactory,
    "bow": BowFactory,
    "quiver": QuiverFactory,
    "book_of_spells": BookOfSpellsFactory,
    "magic_totem": MagicTotemFactory,
    "sword": SwordFactory
}

import random

enemy_type_list = ["ogre", "skeleton", "goblin"]
item_type_list = ["apple", "bow", "quiver", "book_of_spells", "magic_totem", "sword"]
class_type_list = ["mage", "warrior", "archer"]


def choice_player() -> str:
    """Выбор класса для игрока."""
    print("Игра началась! \nДля начала необходимо выбрать класс, Выберите класс: \n1. Воин\n2. Маг\n3. Лучник")
    pl_choice = input("1 или 2 или 3: ")
    while pl_choice != "1" and pl_choice != "2" and pl_choice != "3":
        if pl_choice != "1" and pl_choice != "2" and pl_choice != "3":
            print("Ты должен ввести 1 или 2 или 3")
            pl_choice = input("1 или 2 или 3: ")

    return pl_choice


class_type = choice_player()
if class_type == "1":
    players_current_class = "warrior"
elif class_type == "2":
    players_current_class = "mage"
elif class_type == "3":
    players_current_class = "archer"

print(players_current_class)
for i in range(10):

    rnd_event = random.randint(1, 2)
    if rnd_event == 1:
        SPAWNER_TYPE = random.choice(enemy_type_list)
        spawner = spawner_to_factory_mapping[SPAWNER_TYPE]()

        enemy = spawner.create_enemy()
        action = enemy.attack()
        print(action)
    elif rnd_event == 2:
        SPAWNER_TYPE = random.choice(item_type_list)
        spawner = spawner_to_factory_mapping[SPAWNER_TYPE]()

        item = spawner.create_item()
        action = item.use()
        print(action)
