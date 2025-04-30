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
        self.craft_inventory = []  # Inventory now holds Item objects
        self.weapon_inventory = [] #Weapon now holds weapon objects

    def is_alive(self):
        return self.hp > 0

    def attack(self, enemy):
        damage = random.randint(5, 15)
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        enemy.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage! (HP: {self.hp})")

    def add_item(self, item):
        self.craft_inventory.append(item)

    def remove_item(self, item):
        self.craft_inventory.remove(item)

    def add_weapon(self, item):
        self.weapon_inventory.append(item)

    def show_craft_inventory(self):
        print("\nYour current craft inventory:")
        if not self.craft_inventory:
            print("  (empty)")
        else:
            for item in self.craft_inventory:
                print(f"  - {item}")
    
    def show_weapon_inventory(self):
        print("\nYour current weapon inventory:")
        if not self.weapon_inventory:
            print("  (empty)")
        else:
            for item in self.weapon_inventory:
                print(f"  - {item}")
    

class Weapon:
    def __init__(self, name="", damage=0):
        self.name = name
        self.damage = damage

    def equip_weapon(self, player, choice):
        if choice in player.weapon_inventory:
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


class Enemy:
    def __init__(self, name, hp):
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
        print("\n1. Take damage")
        print("2. Try and defend")
        choice = input("Choose your action: ")
        if choice == '1':
            character.take_damage(damage)
        elif choice == '2':
            if random.randint(1, 3) == 1:
                print(f"{character.name} defends the attack!")
            else:
                print("You failed to defend the attack!")
        else:
            print("Invalid action. Please choose 1 or 2.")


    def take_damage(self, damage):
        random_dodge = random.randint(1, 4)
        if random_dodge == 1:
            print(f"{self.name} dodges the attack!")
        else:
            self.hp -= damage
            print(f"{self.name} takes {damage} damage! (HP: {self.hp})")

    def enemy_drop(self, player):
        pass

    def unique_behaviour(self):
        pass

    def reward(self, player):
        print("You have defeated the Goblin")
        print("Congratulations!")
        print("\nYour reward for defeating all three wild enemies is a rare trophy")
        print("   ___________")
        print("  '._==_==_=_.'")
        print("  .-\:      /-.")
        print(" | (|:.     |) |")
        print("  '-|:.     |-'")
        print("    \::.    /")
        print("     '::. .'")
        print("       ) (")
        print("     _.' '._")
        print("    """"""""")

class Troll(Enemy):
    def __init__(self, name="troll", hp=30):
        super().__init__(name, hp)

    def attack(self, character):
        damage = random.randint(10, 15)
        print(f"{self.name} attacks {character.name} for {damage} damage!")
        print("\nDo you wish to try and defend?")
        print("\n1. Take damage")
        print("2. Try and defend")
        choice = input("Choose your action: ")
        if choice == '1':
            character.take_damage(damage)
        elif choice == '2':
            if random.randint(0,1) == 0:
                print(f"{character.name} defends the attack!")
            else:
                print("\nYou failed to defend the attack!")
                character.take_damage(damage)
        else:
            print("Invalid action. Please choose 1 or 2.")

    def take_damage(self, damage):  
        self.hp -= damage
        print(f"{self.name} takes {damage} damage! (HP: {self.hp})")

    def enemy_drop(self, player):
        print("\nThe troll has dropped some items:")
        print("\nSpiked Club")
        print("Troll Eyebalss")
        print("\n1. Inspect items")
        print("2. Accept items")
        print("3. Decline items")
        while True:
            choice = input("\nChoose what you would lke to do with the items:")
            if choice == "1":
                print("\nSpiked Club - Wooden club with nails")
                print("Troll Eyeballs - For crafting")
            elif choice == "2":
                player.add_item(Item("Spiked Club", "Wooden club with nails"))
                player.add_item(Item("Troll Eyeballs", "For crafting"))
                print("\nSuccess! Items added to your inventory.")
                break
            elif choice == "3":
                break
            else:
                print("\nInvalid choice")

    def unique_behaviour(self):
        pass

    def reward(self, player):
        print("\nYour reward for defeating the Troll is two new crafting item")
        print("     + Rope x1 to your inventory")
        print("     + Iron Ingot x1 to your inventory")
        print("\nHere is the content of your inventory")
        player.add_item(Item("Rope", "For crafting"))
        player.add_item(Item("Iron Ingot", "For crafting"))
        for item in player.craft_inventory:
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

    def enemy_drop(self, player):
        print("\nThe zombie has dropped some items:")
        print("\nSmall Knife")
        print("Zombie Snot")
        print("\n1. Inspect items")
        print("2. Accept items")
        print("3. Decline items")
        while True:
            choice = input("\nChoose what you would lke to do with the items:")
            if choice == "1":
                print("\nSmall Knife - Set of small throwing knives")
                print("Zombie Snot - For crafting")
            elif choice == "2":
                player.add_item(Item("Small Knife", "Set of small throwing knives"))
                player.add_item(Item("Zombie Snot", "For crafting"))
                print("\nSuccess! Items added to your inventory.")
                break
            elif choice == "3":
                break
            else:
                print("\nInvalid choice")

    def unique_behaviour(self):
        pass

    def reward(self, player):
        print("\nYour reward for defeating the Zombie is a new crafting item")
        print("     + Rock x1 to your inventory")
        player.add_item(Item("Rock", "For crafting"))


class Crafting:
    def show_recipes(self):
        print("\nHere is a list of craftible items:")
        print("\n1. Wooden Sword - Does up to 15 damage")
        print("     - Stick x1")
        print("     - Rope x1")
        print("\n2. Wooden Shield - Gives you a 1 in 4 chance of defending an attack")
        print("     - Rock x1")
        print("     - Rope x1")
        print("\n3. Forged Longsword - Does up to 20 damage")
        print("     - Iron ingot x1")
        print("     - Rope x1")
        print("\n4. Health Potion - Increases your health by 20hp")
        print("     - Zombie Snot x1")
        print("     - Troll Eyeballs x1")

    def craft1(self, player):
        player.add_weapon(WoodenSword)
        #player.add_item(Item("Wooden Sword", "A basic wooden sword"))
        player.remove_item(Item("Stick", "For crafting"))
        player.remove_item(Item("Rope", "For crafting"))
        print("\nSuccess!")
        print("A Wooden Sword was added to your weapons inventory")

    def craft2(self, player):
        #----------------------------------------------------------------------------------------------
        #player.add_weapon(WoodenShield)
        player.add_item(Item("Wooden Shield", "A basic wooden shield"))
        player.remove_item(Item("Rock", "For crafting"))
        player.remove_item(Item("Rope", "For crafting"))
        print("\nSuccess!")
        print("A Wooden Shield was added to your invertory")

    def craft3(self, player):
        player.add_weapon(ForgedLongsword)
        #player.add_item(Item("Forged Longsword", "A forged sword for intense attacks"))
        player.remove_item(Item("Iron Ingot", "For crafting"))
        player.remove_item(Item("Rope", "For crafting"))
        print("\nSuccess!")
        print("A Forged Longsword was added to your weapons invertory")

    def craft4(self, player):
        player.add_item(Item("Health Potion", "Increases your hp by 20"))
        player.remove_item(Item("Zombie Snot", "For crafting"))
        player.remove_item(Item("Troll Eyeballs", "For crafting"))
        print("\nSuccess!")
        print("A Health Potion was added to your invertory")

    def craft_menu(self, player):
        while True:
            craft_choice = input("\nPlease choose which item you wish to craft (1,2 or 3):")
            if craft_choice == "1" or craft_choice == "one":
                if Item("Stick", "For crafting") in player.craft_inventory and Item("Rope", "For crafting") in player.craft_inventory:
                    self.craft1(player)
                    break
                else:
                    print("\nYou do not have the correct items to craft this")
            elif craft_choice == "2" or craft_choice == "two":
                if Item("Rock", "For crafting") in player.craft_inventory and Item("Rope", "For crafting") in player.craft_inventory:
                    self.craft2(player)
                    break
                else:
                    print("\nYou do not have the correct items to craft this")
            elif craft_choice == "3" or craft_choice == "three":
                if Item("Iron Ingot", "For crafting") in player.craft_inventory and Item("Rope", "For crafting") in player.craft_inventory:
                    self.craft3(player)
                    break
                else:
                    print("\nYou do not have the correct items to craft this")
            elif craft_choice == "4" or craft_choice == "four":
                if Item("Zombie Snot", "For crafting") in player.inventory and Item("Troll Eyeballs", "For crafting") in player.inventory:
                    self.craft4(player)
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
        print("2. Equip/Use items")
        print("3. Show Inventory")
        action = input("Choose your action: ")

        if action == '1':
            player.attack(enemy)
        elif action == "2":
            
            #Equip_items function
            #print list
            #input to ask what they wanna print (.strip().title())
            #

            pass
        elif action == '3':
            player.show_craft_inventory()
            player.show_weapon_inventory()
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
        enemy.enemy_drop(player)
    else:
        print("\nYou have been defeated.")

def main_menu():
    while True:
        print("\n=== RPG Starter Adventure ===")
        print("1. Start Game")
        print("2. Load data")
        print("3. Exit")
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
            player.show_craft_inventory()
            crafter.craft_menu(player)
            print("\nTime to fight!")
            combat(player, Zombie())
            crafter.show_recipes()
            player.show_craft_inventory()
            crafter.craft_menu(player)
            print("\nTime to fight!")
            combat(player, Troll())
            crafter.show_recipes()
            player.show_craft_inventory()
            crafter.craft_menu(player)
            print("\nTime to fight!")
            combat(player, Goblin())
        elif choice == "2":
            pass
        elif choice == "3":
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
