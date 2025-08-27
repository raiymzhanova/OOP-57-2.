class Hero:

    def __init__(self, name, hp, mp, lvl):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.lvl = lvl

    def action(self):
        print("base action")


class HeroMage(Hero):

    def __init__(self, name, hp, mp, lvl, spell_book):
        super().__init__(name, hp, mp, lvl)
        self.spell_book = spell_book

    def show_spells(self):
        print("Доступные заклинания:")
        for spell in self.spell_book:
            print(f"- {spell}")



class HeroWarrior(Hero):

    def __init__(self, name, hp, mp=0, lvl=1):
        super().__init__(name, hp, mp, lvl)
        self.rage = 0

    def action(self):

        print("Герой готов к атаке!")

    def attack(self):

        if self.rage >= 100:
            print(f"{self.name} наносит мощную атаку! Ярость сброшена.")
            self.rage = 0
        else:
            print(f"{self.name} наносит обычную атаку. Ярость увеличена на 25.")
            self.rage += 25
        print(f"Текущая ярость: {self.rage}")


mage = HeroMage(name="Merlin", hp=80, mp=500, lvl=5, spell_book=["Fireball", "Teleport"])
warrior = HeroWarrior(name="Conan", lvl=8, hp=150)

print("Проверка Мага")
mage.action()
mage.show_spells()

print("Проверка Воина")
warrior.action()
warrior.attack()
warrior.attack()
warrior.attack()
warrior.attack()
warrior.attack()