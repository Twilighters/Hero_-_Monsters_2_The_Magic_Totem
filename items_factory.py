from abc import ABC, abstractmethod


class Item(ABC):
    """Абстрактный класс игрового предмета."""

    @abstractmethod
    def pick_up(self):
        """Метод, наличие которого обязательно у всех."""
        pass

    @abstractmethod
    def use(self):
        """Метод, наличие которого обязательно у всех."""
        pass

class Sword(Item):

    def pick_up(self):
        return 'Найденный меч помещен в рюкзак'

    def use(self):
        return 'Нанесен удар мечом'



class Bow(Item):

    def pick_up(self):
        return 'Найденный лук помещен в рюкзак'

    def use(self):
        return 'Сделан выстрел из лука'

class Quiver(Item):

    def pick_up(self):
        return 'Найденный колчан помещен в рюкзак'

    def use(self):
        return 'Колчан задействовался'


class BookOfSpells(Item):

    def pick_up(self):
        return 'Найдена книга магии'

    def use(self):
        return 'Наносит урон светлой магией'

class Apple(Item):

    def pick_up(self):
        return 'Найдено яблоко'

    def use(self):
        return 'Очки здоровья восстановлены'

class MagicTotem(Item):

    def pick_up(self):
        return 'Найден волшебный тотем'

    def use(self):
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
        return Sword()


class BowFactory(ItemFactory):
    """Конкретная фабрика лука."""

    def create_item(self):
        return Bow()


class QuiverFactory(ItemFactory):
    """Конкретная фабрика колчана."""

    def create_item(self):
        return Quiver()

class BookOfSpellsFactory(ItemFactory):
    """Конкретная фабрика книги заклинаний."""

    def create_item(self):
        return BookOfSpells()

class AppleFactory(ItemFactory):
    """Конкретная фабрика яблока."""

    def create_item(self):
        return Apple()

class MagicTotemFactory(ItemFactory):
    """Конкретная фабрика магического тотема."""

    def create_item(self):
        return MagicTotem()