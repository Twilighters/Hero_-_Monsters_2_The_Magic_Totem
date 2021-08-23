from enemy_factory import *
from items_factory import *
from player_classes import *
import random
import sys

equip = []
monster_counter = 0
main_hero = Hero()
hero_attack = main_hero.weapons["sword"].attack
main_monster = Ogre()
hero_hp = main_hero.hp
monster_hp = main_monster.monster_hp
monster_attack = main_monster.monster_attack

# print(main_hero.hero)
# spawner_to_factory_mapping = {
#     "ogre": OgreFactory,
#     "skeleton": SkeletonFactory,
#     "goblin": GoblinFactory,
#     "apple": AppleFactory,
#     "bow": BowFactory,
#     "quiver": QuiverFactory,
#     "book_of_spells": BookOfSpellsFactory,
#     "magic_totem": MagicTotemFactory,
#     "sword": SwordFactory
# }

spawner_to_factory_mapping = {
    "ogre": OgreFactory,
    "apple": AppleFactory,
    "book_of_spells": BookOfSpellsFactory,
    "sword": SwordFactory
}

# enemy_type_list = ["ogre", "skeleton", "goblin"]
# item_type_list = ["sword", "apple", "bow", "quiver", "book_of_spells", "magic_totem"]
# class_type_list = ["mage", "warrior", "archer"]
enemy_type_list = ["ogre"]
item_type_list = ["sword", "apple", "book_of_spells"]


def choice() -> str:
    """Выбор игрока."""
    pl_choice = input("Введите 1 или 2 на клавиатуре: ")
    while pl_choice != "1" and pl_choice != "2":
        if pl_choice != "1" and pl_choice != "2":
            print("Ты должен ввести 1 или 2")
            pl_choice = input("1 или 2: ")

    return pl_choice


def choice_player() -> str:
    """Выбор класса для игрока."""
    pl_choice = input("1 или 2 или 3: ")
    while pl_choice != "1" and pl_choice != "2" and pl_choice != "3":
        if pl_choice != "1" and pl_choice != "2" and pl_choice != "3":
            print("Ты должен ввести 1 или 2 или 3")
            pl_choice = input("1 или 2 или 3: ")

    return pl_choice


# print("Перед схваткой выбери оружие!\nВыберите оружие: \n1. Меч\n2. Книга Заклинаний\n3. Лук")
# class_type = choice_player()
#
# def player_class(class_type) -> str:
#     hero = None
#     if class_type == "1":
#         hero = "Warrior"
#     elif class_type == "2":
#         hero = "Mage"
#     elif class_type == "3":
#         hero = "Archer"
#     return hero
#
# hero = player_class(class_type)
main_hero = Warrior()
main_monster = Ogre()


def switch_weapon(hero_attack):
    # print("Перед тобой монстр с Атакой:", main_monster.monster_attack, "\nс HP :", main_monster.monster_hp)
    print("Перед схваткой выбери оружие!\nВыберите оружие: \n1. Меч\n2. Книга Заклинаний\n3. Лук")
    choice_current_weapon = choice_player()

    if choice_current_weapon == "1":
        print("Ты выбрал меч")
        hero_attack = main_hero.weapons["sword"].attack * main_hero.sword_modifier
    elif choice_current_weapon == "2":
        print("Ты выбрал книгу заклинаний")
        hero_attack = main_hero.weapons["book_of_spells"].attack * main_hero.book_of_spells_modifier
    else:

        print("Ты выбрал лук")
        hero_attack = main_hero.weapons["bow"].attack * main_hero.bow_modifier
    return hero_attack


def fight(hero_hp, hero_attack, monster_hp, monster_attack):
    global monster_counter
    print("Будете ли вы драться с ним или убежите? \n1 - В БОЙ! \n2 - Убегаем!")
    while True:

        if choice() == "1":

            monster_hp = monster_hp - hero_attack
            print("Ты наносишь урон, HP монстра", monster_hp)
            hero_hp = hero_hp - monster_attack
            print("Тебе нанесли урон, твое HP", hero_hp)
            if hero_hp <= 0:
                print("По вам нанесен смертельный удар")
                print("Ты проиграл")
                sys.exit()
            elif monster_hp <= 0:
                monster_counter += 1
                print("Ты выиграл")
                break
        else:
            print("ты убежал")
            break
    return print("отработано", monster_counter)


# fight(hero_hp, hero_attack, monster_hp, monster_attack)

print(monster_counter)

for i in range(3):

    # rnd_event = random.randint(1, 2)
    rnd_event = 1
    if rnd_event == 1:
        SPAWNER_TYPE = random.choice(enemy_type_list)
        spawner = spawner_to_factory_mapping[SPAWNER_TYPE]()
        if SPAWNER_TYPE == "ogre":
            ogre_factory = OgreFactory()
            main_monster = ogre_factory.create_enemy()
            print("Перед тобой возник монстр со следующими характеристиками: \nАтака:", main_monster.monster_attack, "\nHP:", main_monster.monster_hp)
            print("Твои HP равны:", hero_hp)
            fight(hero_hp, hero_attack, monster_hp, monster_attack)
        enemy = spawner.create_enemy()
        action = enemy.attack()
        print(action)
#     elif rnd_event == 2:
#         SPAWNER_TYPE = random.choice(item_type_list)
#         spawner = spawner_to_factory_mapping[SPAWNER_TYPE]()
#         if SPAWNER_TYPE == "apple":
#             print("яблучко")
#             apple_factory = AppleFactory()
#             new_apple = apple_factory.create_item()
#             main_hero.food.append(new_apple)
#             main_hero.food[0].use(main_hero)
#         elif SPAWNER_TYPE == "sword":
#             print("Мечик")
#             sword_factory = SwordFactory()
#             print("Характеристики Силы Атаки вашего меча - ", main_hero.weapons["sword"].attack)
#             new_sword = sword_factory.create_item()
#             print("Характеристики Силы Атаки нового меча - ", new_sword.attack,
#                   "\nХотите ли вы взять новый меч?\n1 - Да\n2 - Нет")
#             pl_choice = choice()
#             if pl_choice == "1":
#                 main_hero.weapons["sword"] = new_sword
#                 print("Теперь текущие характеристики Силы Атаки меча - ", main_hero.weapons["sword"].attack)
#             else:
#                 print("Вы решили оставить свой старый меч с Силой Атаки - ", main_hero.weapons["sword"].attack)
#
#         elif SPAWNER_TYPE == "book_of_spells":
#             print("книжко")
#             book_of_spells_factory = BookOfSpellsFactory()
#             print("Характеристики Маг. Атаки вашей Книги Заклинаний - ", main_hero.weapons["book_of_spells"].attack)
#             new_book_of_spells = book_of_spells_factory.create_item()
#             print("Характеристики Маг. Атаки новой Книги Заклинаний - ", new_book_of_spells.attack,
#                   "\nХотите ли вы взять новую Книгу Заклинаний?\n1 - Да\n2 - Нет")
#             pl_choice = choice()
#             if pl_choice == "1":
#                 main_hero.weapons["book_of_spells"] = new_book_of_spells
#                 print("Теперь текущая Маг. Атака Книги Заклинаний - ",
#                       main_hero.weapons["book_of_spells"].attack)
#             else:
#                 print("Вы решили оставить свою старую Книгу Заклинаний с Маг. Атакой - ",
#                       main_hero.weapons["book_of_spells"].attack)

# item = spawner.create_item()
# action = item.use(main_hero)
# print(action)

# print(main_hero)
# sword_factory1 = SwordFactory()
# print(main_hero.weapons["sword"].attack)
# main_hero.weapons["sword"] = sword_factory1.create_item()
# print(main_hero.weapons["sword"].attack)

# apple_factory1 = AppleFactory()
# new_apple = apple_factory1.create_item()
# main_hero.food.append(new_apple)
# main_hero.food.append(new_apple)
# main_hero.food[0].use(main_hero)

print("в инвентаре сейчас:",
      "\nМеч:", main_hero.weapons["sword"].attack,
      "\nКнига Заклинаний:", main_hero.weapons["book_of_spells"].attack)
print("Текущее HP:", main_hero.hp)
print("Текущее HP монстра:", main_monster.monster_hp)
print("Текущее атака монстра:", main_monster.monster_attack)

if __name__ == '__main__':
    print('Эта программа запущена из main.py.')
else:
    print('Меня импортировали в другой модуль.')
