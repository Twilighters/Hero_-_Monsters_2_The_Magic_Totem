from abc import ABC, abstractmethod
import random



class Item(ABC):
    """Абстрактный класс игрового предмета."""

    @abstractmethod
    def pick_up(self):
        """Метод, наличие которого обязательно у всех."""
        pass



    @abstractmethod
    def use(self, main_hero):
        """Метод, наличие которого обязательно у всех."""
        pass


class Sword(Item):
    attack = 5

    def pick_up(self):
        return 'Найденный меч помещен в рюкзак'

    def use(self, main_hero):
        return 'Нанесен удар мечом'


class Bow(Item):
    attack = 10

    def pick_up(self):
        return 'Найденный лук помещен в рюкзак'

    def use(self, main_hero):
        return 'Сделан выстрел из лука'


class Quiver(Item):

    def pick_up(self):
        return 'Найденный колчан помещен в рюкзак'

    def use(self, main_hero):
        return 'Колчан задействовался'


class BookOfSpells(Item):
    attack = 10

    def pick_up(self):
        return 'Найдена книга магии'

    def use(self, main_hero):
        return 'Наносит урон светлой магией'


class Apple(Item):
    healing = 20

    def pick_up(self):
        return 'Найдено яблоко'


    def use(self, main_hero):

        main_hero.heal(self.healing)
        main_hero.food.pop()
        return print("Текущее показатели здоровья равны", main_hero.hp)


class MagicTotem(Item):

    def pick_up(self):
        return 'Найден волшебный тотем'

    def use(self, main_hero):
        return 'Игра сохранена'


class ItemFactory(ABC):
    """Абстрактная фабрика игрового предмета."""

    @abstractmethod
    def create_item(self):
        """Создание абстрактного продукта."""
        pass


class SwordFactory(ItemFactory):
    """Конкретная фабрика меча."""

    def create_item(self):
        new_sword = Sword()
        new_sword.attack = random.randint(10, 30)
        return new_sword


class BowFactory(ItemFactory):
    """Конкретная фабрика лука."""

    def create_item(self):
        new_bow = Bow()
        new_bow.attack = random.randint(10, 30)
        return new_bow


class QuiverFactory(ItemFactory):
    """Конкретная фабрика колчана."""

    def create_item(self):
        return Quiver()


class BookOfSpellsFactory(ItemFactory):
    """Конкретная фабрика книги заклинаний."""

    def create_item(self):
        new_book_of_spells = Sword()
        new_book_of_spells.attack = random.randint(10, 30)
        return new_book_of_spells


class AppleFactory(ItemFactory):
    """Конкретная фабрика яблока."""

    def create_item(self):
        return Apple()


class MagicTotemFactory(ItemFactory):
    """Конкретная фабрика магического тотема."""

    def create_item(self):
        return MagicTotem()
