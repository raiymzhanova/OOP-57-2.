# # Наследование
# from pyclbr import Class
#
#
# # Родительский|Super класс
# class Hero:
#
#     def __init__(self, name, lvl,hp):
#         self.name = name
#         self.lv = lvl
#         self.hp = hp
#
#     def action(self):
#         return print("pass")
#
# obj1 = Hero("John Doe", 10, 100)
#
# # print(type(obj1))
# obj1.action()
#
#
# # Дочерний класс
# class HeroMage(Hero):
#
#     def __init__(self, name, hp, mp, lvl=1):
#         super().__init__(name, lvl, hp)
#         self.mp = mp
#
#     # def action(self):
#     #     return print('base action')
#
#     def cast_spell(self):
#         if self.mp == 0:
#             return print('Сорян маны нет иди спать !!')
#         else:
#             self.mp -= 100
#             return print('Огненный щар!!')
#
#     def rest(self):
#         self.mp += 50
#         return print("Отдыхаю")
#
#
# obj2 = HeroMage(mp=1000, name="Ardager", hp=100)
#
#
# #
# # print(obj2.mp)
# # obj2.cast_spell()
# # print(obj2.mp)
# # obj2.rest()
# # print(obj2.mp)
#
# # дочерний класс
# class HeroWarrior :
#     def __init__(self, name, hp, lvl, rage=0 ):
#         super().__init__(name, hp, lvl)
#         self.rage = rage
#
#     def action(self):
#             print("Герой готов к атаке!")
#
#      def attack(self):
#         if self.rage >= 100:
#             print("Герой наносит мощную атаку! Ярость сброшена.")
#             self.rage = 0
#             else:
#             print(f"Герой наносит обычную атаку. Ярость увеличена с {self.rage} на {self.rage + 25}.")
#             self.rage += 25
#
# base_hero = Hero(name="Алекс", hp=100, lvl=1)
#
