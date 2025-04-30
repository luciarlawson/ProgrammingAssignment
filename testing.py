import random

class Item:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}" if self.description else self.name
    
    def __eq__(self, other):
        return isinstance(other, Item) and self.name == other.name and self.description == other.description

    def __hash__(self):
        return hash((self.name, self.description))

class Character:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
        self.inventory = []  # Inventory now holds Item objects
        self.weapon = [] #Weapon now holds weapon objects

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)
    
    def add_weapon(self, item):
        self.weapon.append(item)


class Weapon:
    def __init__(self, name="", damage=0):
        self.name = name
        self.damage = damage

    def equip_weapon(self, player, choice):
        if choice in player.weapon:
            if choice == "Wooden Sword":
                self.woodenswordequipped = True
                self.forgedlongswordequipped = False
                self.smallknifeequipped = False
                self.spikedclubequipped = False
            elif choice == "Forged Longsword":
                self.woodenswordequipped = False
                self.forgedlongswordequipped = True
                self.smallknifeequipped = False
                self.spikedclubequipped = False
            elif choice == "Small Knife":
                self.woodenswordequipped = False
                self.forgedlongswordequipped = False
                self.smallknifeequipped = True
                self.spikedclubequipped = False
            elif choice == "Spiked Club":
                self.woodenswordequipped = False
                self.forgedlongswordequipped = False
                self.smallknifeequipped = False
                self.spikedclubequipped = True

class WoodenSword(Weapon):
    def __init__(self, name="Wooden Sword", damage=random.randint(5, 15)):
        super().__init__(name, damage)
        self.woodenswordequipped = False

class ForgedLongsword(Weapon):
    def __init__(self, name="Forged Longsword", damage=random.randint(15, 20)):
        super().__init__(name, damage)
        self.forgedlongswordequipped = False
    
class SmallKnife(Weapon):
    def __init__(self, name="Small Knife", damage=5):
        super().__init__(name, damage)
        self.smallknifeequipped = False

class SpikedClub(Weapon):
    def __init__(self, name="Spiked Club", damage=random.randint(5, 15)):
        super().__init__(name, damage)
        self.spikedclubequipped = False

player = Character("Lucia")
player.add_item(Item("Rope", "For crafting"))
player.add_weapon(WoodenSword)
player.add_weapon(WoodenSword)
WoodenSword.equip_weapon


