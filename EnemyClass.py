import random


class Crafting:
    def __init__(self, name):
        self.name = name
        self.inventory=["Stick", "Rope"]

    def show_recipes(self):
        print("Here is a list of craftible items:")
        print("")
        print("1. Wooden Sword - Does up to 15 damage")
        print("     - Stick x1")
        print("     - Rope x1")
        print("")
        print("2. Wooden Shield - Gives you a 50:50 chance of defending an attack")
        print("     - Stick x2")
        print("     - Rope x1")
        print("")
        print("3. Forged Longsword - Does up to 20 damage")
        print("     - Iron ingot x1")
        print("     - Rope x1")
        print("")

    def show_items(self):
        print("These are the items in your inventory")
        print("")
        print(self.inventory)

    def level1(self):
        player.add_item(Item("Wooden Sword", "A basic wooden sword."))
        print("Success!")
        print("A Wooden Sword was added to your invertory")

    def level2(self):
        player.add_item(Item("Wooden Shield", "A basic wooden shield"))
        print("Success!")
        print("A Wooden Shield was added to your invertory")

    def level3(self):
        player.add_item(Item("Forged Longsword", "A forged sword for intense attacks"))
        print("Success!")
        print("A Forged Longsword was added to your invertory")

    



player = Crafting("lucia")
player.level1()