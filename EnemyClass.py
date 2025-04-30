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

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)


def save_data(self):
    with open("player_data.txt", "w") as file:
        file.write("Player data")
        file.write(f"\nname: {player.name}")
        file.write(f"\nhp: {player.hp}")
        for item in self.inventory:
            file.write(f"\ninventory: {item}")

player = Character("lucia")
player.add_item(Item("Stick", "For crafting"))
player.add_item(Item("Rope", "For crafting"))
player.add_item(Item("Rope", "For crafting"))

save_data(player)

