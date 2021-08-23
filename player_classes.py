from abc import ABC, abstractmethod
from items_factory import Sword, Bow, BookOfSpells



class Player(ABC):
    """Абстрактный класс игрока."""
    hp = None
    sword_modifier = 1
    bow_modifier = 1
    book_of_spells_modifier = 1
    weapons = {
        "sword": Sword,
        "bow": Bow,
        "book_of_spells": BookOfSpells,
    }
    food = []
    quiver_is_equipped = False
    melee_evade = 0
    range_evade = 0
    magic_evade = 0

    @abstractmethod
    def choice(self):
        """Метод, наличие которого обязательно у всех."""
        pass

    @abstractmethod
    def attack(self):
        """Метод, наличие которого обязательно у всех."""
        pass

    @abstractmethod
    def use(self):
        """Метод, наличие которого обязательно у всех."""
        pass

    def heal(self, heal_value):
        """Метод исцеления."""
        self.hp += 20



class Hero(Player):

    def __init__(self):
        self.hp = 100
        self.weapons["sword"] = Sword
        self.sword_modifier = 1.2
        self.melee_evade = 20
    hero = None
    def choice(self) -> None:

        return None

    def attack(self) -> None:
        return None

    def use(self) -> None:
        return None

class Warrior(Player):

    def __init__(self):
        self.hp = 15
        self.weapons["sword"] = Sword
        self.sword_modifier = 1.2
        self.melee_evade = 20

    def choice(self) -> str:
        """Выбор игрока."""
        pl_choice = input("1 или 2: ")
        while pl_choice != "1" and pl_choice != "2":
            if pl_choice != "1" and pl_choice != "2":
                print("Ты должен ввести 1 или 2")
                pl_choice = input("1 или 2: ")

        return pl_choice

    def attack(self):
        return 'Воин атакует'

    def use(self):
        return 'Воин Использует предмет'


class Mage(Player):
    def __init__(self):
        self.hp = 100
        self.weapons["sword"] = Sword
        self.book_of_spells_modifier = 1.2
        self.magic_evade = 20

    def choice(self) -> str:
        """Выбор игрока."""
        pl_choice = input("1 или 2: ")
        while pl_choice != "1" and pl_choice != "2":
            if pl_choice != "1" and pl_choice != "2":
                print("Ты должен ввести 1 или 2")
                pl_choice = input("1 или 2: ")

        return pl_choice

    def attack(self):
        return 'Маг Атакует светлой магией'

    def use(self):
        return 'Маг Использует предмет'


class Archer(Player):
    def __init__(self):
        self.hp = 100
        self.weapons["sword"] = Sword
        self.bow_modifier = 1.2
        self.range_evade = 20

    def choice(self) -> str:
        """Выбор игрока."""
        pl_choice = input("1 или 2: ")
        while pl_choice != "1" and pl_choice != "2":
            if pl_choice != "1" and pl_choice != "2":
                print("Ты должен ввести 1 или 2")
                pl_choice = input("1 или 2: ")

        return pl_choice

    def attack(self):
        return 'Лучник делает выстрел из лука'

    def use(self):
        return 'Лучник Использует предмет'
