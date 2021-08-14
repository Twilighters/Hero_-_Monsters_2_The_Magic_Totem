from enemy_factory import *
from items_factory import *

spawner_to_factory_mapping = {
    "ogre": OgreFactory,
    "skeleton": SkeletonFactory,
    "goblin": GoblinFactory,
    "apple": AppleFactory
}

import random

enemy_type_list = ["ogre", "skeleton", "goblin"]
item_type_list = ["apple", "bow", "quiver", "book_of_spells", "magic_totem", "sword"]

for i in range(10):
    SPAWNER_TYPE = random.choice(enemy_type_list)

    spawner = spawner_to_factory_mapping[SPAWNER_TYPE]()

    enemy = spawner.create_enemy()
    action = enemy.attack()
    print(action)
