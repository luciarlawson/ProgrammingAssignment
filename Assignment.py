import random

class Item:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}" if self.description else self.name

class Character:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
        self.inventory = []  # Inventory now holds Item objects

    def is_alive(self):
        return self.hp > 0

    def attack(self, enemy):
        damage = random.randint(5, 15)
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        enemy.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage! (HP: {self.hp})")

    def show_recipes(self):
        print("\nHere is a list of craftible items:")
        print("\n1. Wooden Sword - Does up to 15 damage")
        print("     - Stick x1")
        print("     - Rope x1")
        print("\n2. Wooden Shield - Gives you a 50:50 chance of defending an attack")
        print("     - Stick x2")
        print("     - Rope x1")
        print("\n3. Forged Longsword - Does up to 20 damage")
        print("     - Iron ingot x1")
        print("     - Rope x1")

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, n):
        self.inventory.pop(n)

    def show_inventory(self):
        print("Inventory:")
        if not self.inventory:
            print("  (empty)")
        else:
            for item in self.inventory:
                print(f"  - {item}")

    def level1(self):
        self.add_item(Item("Wooden Sword", "A basic wooden sword."))
        self.remove_item(0)
        self.remove_item(1)
        print("\nSuccess!")
        print("A Wooden Sword was added to your inventory")

    def level2(self):
        self.add_item(Item("Wooden Shield", "A basic wooden shield"))
        print("\nSuccess!")
        print("A Wooden Shield was added to your inventory")

    def level3(self):
        self.add_item(Item("Forged Longsword", "A forged sword for intense attacks"))
        print("\nSuccess!")
        print("A Forged Longsword was added to your inventory")

class Enemy:
    def __init__(self, name, hp=50):
        self.name = name
        self.hp = hp

    def is_alive(self):
        return self.hp > 0


class Goblin(Enemy):
    def __init__(self, name="goblin", hp=50):
        super().__init__(name, hp)

    def attack(self, character):
        damage = random.randint(15, 20)
        print(f"{self.name} attacks {character.name} for {damage} damage!")
        print("\nDo you wish to try and defend?")
        print("You can only use defensive items a set amount of times")
        print("\n1. Take damage")
        print("2. Try and defend")
        choice = input("Choose your action: ")
        if choice == '1':
            character.take_damage(damage)
        elif choice == '2':
            print(f"{character.name} defends the attack!")
        else:
            print("Invalid action. Please choose 1 or 2.")


    def take_damage(self, damage):
        random_dodge = random.randint(1, 4)
        if random_dodge == 1:
            print(f"{self.name} dodges the attack!")
        else:
            self.hp -= damage
            print(f"{self.name} takes {damage} damage! (HP: {self.hp})")


class Troll(Enemy):
    def __init__(self, name="troll", hp=30):
        super().__init__(name, hp)

    def attack(self, character):
        damage = random.randint(10, 15)
        print(f"{self.name} attacks {character.name} for {damage} damage!")
        print("\nDo you wish to try and defend?")
        print("You can only use defensive items a set amount of times")
        print("\n1. Take damage")
        print("2. Try and defend")
        choice = input("Choose your action: ")
        if choice == '1':
            character.take_damage(damage)
        elif choice == '2':
            print(f"{character.name} defends the attack!")
        else:
            print("Invalid action. Please choose 1 or 2.")


    def take_damage(self, damage):  
        self.hp -= damage
        print(f"{self.name} takes {damage} damage! (HP: {self.hp})")

    def unique_behaviour(self):
        pass


class Zombie(Enemy):
    def __init__(self, name="zombie", hp=20):
        super().__init__(name, hp)

    def attack(self, character):
        damage = random.randint(5, 10)
        print(f"{self.name} attacks {character.name} for {damage} damage!")
        print("\nDo you wish to try and defend?")
        print("\n1. Take damage")
        print("2. Try and defend")
        choice = input("Choose your action: ")
        if choice == '1':
            character.take_damage(damage)
        elif choice == '2':
            print(f"{character.name} defends the attack!")
        else:
            print("Invalid action. Please choose 1 or 2.")

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage! (HP: {self.hp})")

    def unique_behaviour(self):
        pass

    def reward(self, player):
        print("\nYour reward for defeating the Zombie is a new crafting item")
        player.add_item(Item("Rock", "For crafting"))
        for item in player.inventory:
            print(f"  - {item}")
        

def combat(player, enemy):
    print("\nThere are three enemies you will be fighting:")
    print("1. Goblin     level - hard")
    print("2. Troll      level - medium")
    print("3. Zombie     level - easy")
    print("\nYou can only use defensive items a set amount of times")

    print(f"\nA wild {enemy.name} appears!")
    while player.is_alive() and enemy.is_alive():
        # Player's turn
        print("\nYour turn:")
        print("1. Attack")
        print("2. Flee")
        print("3. Show Inventory")
        action = input("Choose your action: ")

        if action == '1':
            player.attack(enemy)
        elif action == '2':
            if random.random() < 0.5: # random.random() generates a random number between 0-1
                print("You successfully fled!")
                return
            else:
                print("Failed to flee!")
        elif action == '3':
            player.show_inventory()
            continue  # Skip enemy turn to allow further action after checking inventory.
        else:
            print("Invalid action. Please choose 1, 2, or 3.")
            continue

        # Enemy's turn if still alive
        if enemy.is_alive():
            print(f"\n{enemy.name}'s turn:")
            enemy.attack(player)

    if player.is_alive():
        print(f"\nYou defeated the {enemy.name}!")
        enemy.reward(player)
    else:
        print("\nYou have been defeated.")

def main_menu():
    while True:
        print("\n=== RPG Starter Adventure ===")
        print("1. Start Game")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter your character's name: ")
            player = Character(name)
            player.add_item(Item("Stick", "For crafting"))
            player.add_item(Item("Rope", "For crafting"))
            player.show_recipes()
            while True:
                item_choice = input("Please choose which item you wish to craft (1,2 or 3):")
                if item_choice == "1":
                    player.level1()
                    break
                elif item_choice == "2" or item_choice == "3":
                    print("You do not have enough items to craft this")
                else:
                    print("Invalid choice.")
            if player.is_alive():
                combat(player, Zombie())
        elif choice == '2':
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()