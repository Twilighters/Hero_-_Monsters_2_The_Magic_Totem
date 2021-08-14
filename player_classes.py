from abc import ABC, abstractmethod


class Player(ABC):
    """Абстрактный класс игрока."""

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


class Mage(Player):

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


class Warrior(Player):

    def choice(self) -> str:
        """Выбор игрока."""
        pl_choice = input("1 или 2: ")
        while pl_choice != "1" and pl_choice != "2":
            if pl_choice != "1" and pl_choice != "2":
                print("Ты должен ввести 1 или 2")
                pl_choice = input("1 или 2: ")

        return pl_choice

    def attack(self):
        return 'Воин Наносит удар мечом'

    def use(self):
        return 'Воин Использует предмет'


class Archer(Player):

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
