from enemy_factory import *
from items_factory import *
from player_classes import *

hero = None
equip = []
# player_is_currently_equipped = "sword"
# quiver_is_equipped = False
monster_counter = 0
# attack = 10

# monster_hp = 150
# monster_attack = 0

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
    print("Игра началась! \nДля начала необходимо выбрать класс\nВыберите класс: \n1. Воин\n2. Маг\n3. Лучник")
    pl_choice = input("1 или 2 или 3: ")
    while pl_choice != "1" and pl_choice != "2" and pl_choice != "3":
        if pl_choice != "1" and pl_choice != "2" and pl_choice != "3":
            print("Ты должен ввести 1 или 2 или 3")
            pl_choice = input("1 или 2 или 3: ")

    return pl_choice


class_type = choice_player()

if class_type == "1":
    hero = Warrior()
elif class_type == "2":
    hero = Mage()
elif class_type == "3":
    hero = Archer()

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


hero = Warrior()
sword_factory1 = SwordFactory()
print(hero.weapons["sword"].attack)
hero.weapons["sword"] = sword_factory1.create_item()
print(hero.weapons["sword"].attack)


apple_factory1 = AppleFactory()
new_apple = apple_factory1.create_item()
hero.food.append(new_apple)
hero.food[0].use()




if __name__ == '__main__':
    print('Эта программа запущена сама по себе.')
else:
    print('Меня импортировали в другой модуль.')
