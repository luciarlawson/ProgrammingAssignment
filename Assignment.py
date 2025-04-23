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

    def is_alive(self):
        return self.hp > 0

    def attack(self, enemy):
        damage = random.randint(5, 15)
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        enemy.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage! (HP: {self.hp})")

    '''def show_recipes(self):
        print("\nHere is a list of craftible items:")
        print("\n1. Wooden Sword - Does up to 15 damage")
        print("     - Stick x1")
        print("     - Rope x1")
        print("\n2. Wooden Shield - Gives you a 50:50 chance of defending an attack")
        print("     - Stick x2")
        print("     - Rope x1")
        print("\n3. Forged Longsword - Does up to 20 damage")
        print("     - Iron ingot x1")
        print("     - Rope x1")'''

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def show_inventory(self):
        print("Inventory:")
        if not self.inventory:
            print("  (empty)")
        else:
            for item in self.inventory:
                print(f"  - {item}")

    def level1(self):   
        self.add_item(Item("Wooden Sword", "A basic wooden sword"))
        self.remove_item(Item("Stick", "For crafting"))
        self.remove_item(Item("Rope", "For crafting"))
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

    def unique_behaviour(self):
        pass

    def reward(self, player):
        print("You have defeated the Goblin")
        print("Congratulations!")
        print("\nYour reward for defeating all three wild enemies is a rare trophy")

class Troll(Enemy):
    def __init__(self, name="troll", hp=30):
        super().__init__(name, hp)

    def attack(self, character):
        damage = random.randint(10, 15)
        print(f"{self.name} attacks {character.name} for {damage} damage!")
        print("\nDo you wish to try and defend?")
        print("You can only use your wooden shild twice before it breaks from impact!!")
        print("\n1. Take damage")
        print("2. Try and defend")
        choice = input("Choose your action: ")
        if choice == '1':
            character.take_damage(damage)
            count += 1
        elif choice == '2':
            if random.randint(0,1) == 0:
                print(f"{character.name} defends the attack!")
            else:
                print("\nyou failed to defend the attack!")
                character.take_damage(damage)
                print("You have used you shield twice already")
        else:
            print("Invalid action. Please choose 1 or 2.")

    def take_damage(self, damage):  
        self.hp -= damage
        print(f"{self.name} takes {damage} damage! (HP: {self.hp})")

    def unique_behaviour(self):
        pass

    def reward(self, player):
        print("\nYour reward for defeating the Troll is two new crafting item")
        print("     + Rope x1 to your inventory")
        print("     + Iron Ingot x1 to your inventory")
        print("\nHere is the content of your inventory")
        player.add_item(Item("Rope", "For crafting"))
        player.add_item(Item("Iron Ingot", "For crafting"))
        for item in player.inventory:
            print(f"  - {item}")


class Zombie(Enemy):
    def __init__(self, name="zombie", hp=20):
        super().__init__(name, hp)

    def attack(self, character):
        damage = random.randint(5, 10)
        print(f"{self.name} attacks {character.name} for {damage} damage!")
        character.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage! (HP: {self.hp})")

    def unique_behaviour(self):
        pass

    def reward(self, player):
        print("\nYour reward for defeating the Zombie is a new crafting item")
        print("     + Rock x1 to your inventory")
        print("\nHere is the content of your inventory")
        player.add_item(Item("Rock", "For crafting"))
        for item in player.inventory:
            print(f"  - {item}")


class Crafting:
    @staticmethod
    def show_recipes():
        print("\nHere is a list of craftible items:")
        print("\n1. Wooden Sword - Does up to 15 damage")
        print("     - Stick x1")
        print("     - Rope x1")
        print("\n2. Wooden Shield - Gives you a 50:50 chance of defending an attack")
        print("     - Rock x1")
        print("     - Rope x1")
        print("\n3. Forged Longsword - Does up to 20 damage")
        print("     - Iron ingot x1")
        print("     - Rope x1")
  
    def craft1(self, player):
        player.add_item(Item("Wooden Sword", "A basic wooden sword"))
        player.remove_item(Item("Stick", "For crafting"))
        player.remove_item(Item("Rope", "For crafting"))
        print("\nSuccess!")
        print("A Wooden Sword was added to your inventory")

    def craft2(self, player):
        player.add_item(Item("Wooden Shield", "A basic wooden shield"))
        player.remove_item(Item("Rock", "For crafting"))
        player.remove_item(Item("Rope", "For crafting"))
        print("\nSuccess!")
        print("A Wooden Shield was added to your invertory")

    def craft3(self, player):
        player.add_item(Item("Forged Longsword", "A forged sword for intense attacks"))
        player.remove_item(Item("Iron Ingot", "For crafting"))
        player.remove_item(Item("Rope", "For crafting"))
        print("\nSuccess!")
        print("A Forged Longsword was added to your invertory")

    def craft_menu(self, player):
        while True:
            craft_choice = input("\nPlease choose which item you wish to craft (1,2 or 3):")
            if craft_choice == "1" or craft_choice == "one":
                if Item("Stick", "For crafting") in player.inventory and Item("Rope", "For crafting") in player.inventory:
                    self.craft1(player)
                    break
                else:
                    print("\nYou do not have the correct items to craft this")
            elif craft_choice == "2" or craft_choice == "two":
                if Item("Rock", "For crafting") in player.inventory and Item("Rope", "For crafting") in player.inventory:
                    self.craft2(player)
                    break
                else:
                    print("\nYou do not have the correct items to craft this")
            elif craft_choice == "3" or craft_choice == "three":
                if Item("Iron Ingot", "For crafting") in player.inventory and Item("Rope", "For crafting") in player.inventory:
                    self.craft3(player)
                    break
                else:
                    print("\nYou do not have the correct items to craft this")
            else:
                print("\nInvalid choice")

        

def combat(player, enemy):
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
            print("\nThere are three enemies you will be fighting:")
            print("1. Zombie     level - easy")  
            print("2. Troll      level - medium")
            print("3 . Goblin     level - hard")
            name = input("\nEnter your character's name: ")
            player = Character(name)
            player.add_item(Item("Stick", "For crafting"))
            player.add_item(Item("Rope", "For crafting"))
            player.add_item(Item("Rope", "For crafting"))
            crafter = Crafting()
            crafter.show_recipes()
            crafter.craft_menu(player)
            combat(player, Zombie())
            crafter.show_recipes()
            crafter.craft_menu(player)
            combat(player, Troll())
            crafter.show_recipes()
            crafter.craft_menu(player)
            combat(player, Goblin())

        elif choice == '2':
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
