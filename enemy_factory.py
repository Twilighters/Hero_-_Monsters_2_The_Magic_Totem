from abc import ABC, abstractmethod
from player_classes import *

class Enemy(ABC):
    """Абстрактный класс игрового противника."""
    monster_hp = None
    monster_attack = None

    @abstractmethod
    def attack(self):
        """Метод, наличие которого обязательно у всех."""
        pass


class Ogre(Enemy):
    def __init__(self):
        self.monster_hp = 15
        self.monster_attack = 4

    def attack(self):

        return 'Огр наносит удар дубиной'


class Skeleton(Enemy):

    def attack(self):
        return 'Скелет стреляет выстрел из лука'


class Goblin(Enemy):

    def attack(self):
        return 'Гоблин атакует темной магией'


class EnemyFactory(ABC):
    """Абстрактная фабрика игрового противника."""

    @abstractmethod
    def create_enemy(self):
        """Создание абстрактного продукта."""
        pass


class OgreFactory(EnemyFactory):
    """Конкретная фабрика огра."""

    def create_enemy(self):
        return Ogre()


class SkeletonFactory(EnemyFactory):
    """Конкретная фабрика скелета."""

    def create_enemy(self):
        return Skeleton()


class GoblinFactory(EnemyFactory):
    """Конкретная фабрика гоблина."""

    def create_enemy(self):
        return Goblin()
