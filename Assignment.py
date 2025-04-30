import random

# Item class defining how items will be stored and displyed if printed
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

# Character class for any player using the game
class Character:
    def __init__(self, name, hp=100):
        self.name = name # Name of the player
        self.hp = hp # Health of the player
        self.craft_inventory = []  # Craft inventory now holds Item objects
        self.weapon_inventory = [] # Weapon now holds weapon objects
        self.equipped_weapon = None # No wepons equipped initialy
        self.defence_item = [] # No defensive items eqipped initialy

    def is_alive(self): # Returs weather the player is alive or not
        return self.hp > 0

    def attack(self, enemy): # Player attacks an enemy
        damage = self.equipped_weapon.damage # Damage depends on which weapon is equipped
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        enemy.take_damage(damage) # Enemy takes damage

    def take_damage(self, damage): # Player takes damage
        self.hp -= damage # Player health goes down
        print(f"{self.name} takes {damage} damage! (HP: {self.hp})")

    def add_item(self, item): # Add a craft item to the craft inventory
        self.craft_inventory.append(item)

    def remove_item(self, item): # Remove an item for the craft inventory (after it has been used to craft)
        self.craft_inventory.remove(item)

    def add_weapon(self, item): # Add weapon to the weapon inventory
        self.weapon_inventory.append(item)

    def remove_weapon(self, item):
        for item in self.weapon_inventory:
            if item.name == "Health Potion":
                self.weapon_inventory.remove(item)
                break

    def show_craft_inventory(self): # Displays the craft items the player has left to use
        print("\nYour current craft inventory:")
        if not self.craft_inventory:
            print("  (empty)") # Shows if the inventory is empty
        else:
            for item in self.craft_inventory:
                print(f"  - {item.name}")
    
    def show_weapon_inventory(self): # Displays the weapons the player has
        print("\nYour current weapon inventory:")
        if not self.weapon_inventory:
            print("  (empty)") # Shows if the inventory is empty
        else:
            for item in self.weapon_inventory:
                print(f"  - {item.name}")

    def show_equipped_items(self): # Displays items that the player has equipped
        if self.equipped_weapon is None:
            print("No weapon equipped") # If there are no weapons equipped
        else:
            print(f"\nYou curently have {self.equipped_weapon} equipped")
        
        if len(self.defence_item) == 0:
            print("No defensive item equipped") # If there are no defensive items equipped
        else:
            print(f"You currently have {self.defence_item} equipped")
    
# Class for all weapons
class Weapon:
    def __init__(self, name="", damage=0, description=""):
        self.name = name
        self.damage = damage
        self.description = description

    def __str__(self): # Used to display print statements correctly
        return f"{self.name}"

    def equip_weapon(self, player): # Equips the weapon so the player can use it
        player.equipped_weapon = self
        print(f"\nYou have the {self.name} equipped.")

# Class for defensive items
class Defence:
    def __init__(self, name="", damage=0, description=""):
        self.name = name
        self.damage = damage
        self.description = description

    def __str__(self): # Used to display print statements correctly
        return f"{self.name}"

    def equip_defence(self, player): # Equips a defensive item so the player can use it
        player.defence_item = self
        print(f"\nYou have the {self.name} equipped.")


class BareHands(Weapon): # Bare hands weapon - all players start with this
    def __init__(self, name="Bare Hands", damage=5, description="weapon"): # Has the least amount of damage
        super().__init__(name, damage, description)

    def __str__(self): # Used to display print statements correctly
        return f"{self.name}"

class WoodenSword(Weapon): # A basic wooden sworn
    def __init__(self, name="Wooden Sword", damage=random.randint(5, 10), description="weapon"):
        super().__init__(name, damage, description)

    def __str__(self): # Used to display print statements correctly
        return f"{self.name}"

class ForgedLongsword(Weapon): # Forged longsword
    def __init__(self, name="Forged Longsword", damage=random.randint(10, 15), description="weapon"): # Does a lot of damage
        super().__init__(name, damage, description)

    def __str__(self): # Used to display print statements correctly
        return f"{self.name}"
    
class SmallKnife(Weapon): # Small Knife
    def __init__(self, name="Small Knife", damage=4, description="weapon"): # Small amount of damage but you throw 5 in one attack
        super().__init__(name, damage, description)

    def __str__(self): # Used to display print statements correctly
        return f"{self.name}"

class SpikedClub(Weapon): # Spiked Club
    def __init__(self, name="Spiked Club", damage=random.randint(10, 15), description="weapon"):
        super().__init__(name, damage, description)

    def __str__(self): # Used to display print statements correctly
        return f"{self.name}"

class HealthPotion(Defence): # Health potion
    def __init__(self, name="Health Potion", damage=-20, description="potion"): # Gives health
        super().__init__(name, damage, description)

    def __str__(self): # Used to display print statements correctly
        return f"{self.name}"
    
    def use_potion(self, player):
        player.remove_weapon(HealthPotion())
        player.hp -= self.damage

class BlockPotion(Defence):
    def __init__(self, name="Block", damage=0, description="potion"):
        super().__init__(name, damage, description)
    
    def __str__(self): # Used to display print statements correctly
        return f"{self.name}"
    
    def use_potion(self):
        pass

class DoubleAttackPotion(Defence):
    def __init__(self, name="Double Attack", damage=0, description="potion"):
        super().__init__(name, damage, description)
    
    def __str__(self): # Used to display print statements correctly
        return f"{self.name}"
    
    def use_potion(self):
        pass

class DoubleDamagePotion(Defence):
    def __init__(self, name="Double Damage", damage=0, description="potion"):
        super().__init__(name, damage, description)
    
    def __str__(self): # Used to display print statements correctly
        return f"{self.name}"
    
    def use_potion(self):
        pass

class WoodenShield(Defence): # wooden shield
    def __init__(self, name="Wooden Shield", damage=0, description="defense"): # Does no damage
        super().__init__(name, damage)

    def __str__(self): # Used to display print statements correctly
        return f"{self.name}"

    def defend(self, player): # Used when you have the shield equipped
        if random.randint(1, 4) == 1: # 1 in 4 chance of defending an attack
            print(f"{player.name} defends the attack!")
        else:
            print("You failed to defend the attack!")
            return False

# Class for any enemys in the game
class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def is_alive(self): # Returns weather the enemy is alive or not
        return self.hp > 0


class Goblin(Enemy): # Goblin enemy - hardest level
    def __init__(self, name="goblin", hp=50): # Has the mosts hp
        super().__init__(name, hp)

    def attack(self, character): # Goblin attacks the player
        damage = random.randint(15, 20)
        print(f"{self.name} attacks {character.name} for {damage} damage!")
        if isinstance(character.defence_item, WoodenShield):
            if character.defence_item.defend(character):
                print("The shield blocked the attack!")
            else:
                character.take_damage(damage)
        else:
            character.take_damage(damage)

    def take_damage(self, damage): # Player attacks Goblin
        random_dodge = random.randint(1, 5) # 1 in 5 chance that the enemy doges the attack
        if random_dodge == 1:
            print(f"{self.name} dodges the attack!")
        else:
            self.hp -= damage
            print(f"{self.name} takes {damage} damage! (HP: {self.hp})")

    def enemy_drop(self, player):
        pass

    def unique_behaviour(self):
        pass

    def reward(self, player): # Reward for wining the game!!
        print("You have defeated all the enemys")
        print(f"Congratulations {player.name}!!")
        print("\nYour reward for defeating all three wild enemies is a rare trophy")
        print("       ___________")
        print("      '._==_==_=_.'")
        print("      .-\:      /-.")
        print("     | (|:.     |) |")
        print("      '-|:.     |-'")
        print("        \::.    /")
        print("         '::. .'")
        print("           ) (")
        print("         _.' '._")
        print("        """"""""")

class Troll(Enemy): # Troll enemy - meadium level
    def __init__(self, name="troll", hp=30):
        super().__init__(name, hp)

    def attack(self, character): # Troll attacks the player
        damage = random.randint(10, 15)
        print(f"{self.name} attacks {character.name} for {damage} damage!")
        if isinstance(character.defence_item, WoodenShield):
            if character.defence_item.defend(character):
                print("The shield blocked the attack!")
            else:
                character.take_damage(damage)
        else:
            character.take_damage(damage)

    def take_damage(self, damage): # Player attacks troll
        self.hp -= damage
        print(f"{self.name} takes {damage} damage! (HP: {self.hp})")

    def enemy_drop(self, player): # Troll drops items when you defeat it (add random chance items) ---------------------------------------------------------------------
        print("\nThe troll has dropped some items:")
        rarity = random.randint(1,8) # Accounts for diferent item rarity
        if rarity == 1: # 1 in 8 chance
            print("\nTroll Socks")
            print("Spiked Club")
            print("\n1. Inspect items") # Inspect, accept or decline items
            print("2. Accept items")
            print("3. Decline items")
            while True:
                choice = input("\nChoose what you would lke to do with the items:") # Player chooses what to do
                if choice == "1":
                    print("\nTroll Socks - For crafting")
                    print("Spiked Club - Wooden club with nails")
                elif choice == "2":
                    player.add_item(Item("Troll Socks", "For crafting"))
                    player.add_item(Item("Spiked Club", "Wooden club with nails"))
                    print("\nSuccess! Items added to your inventory.")
                    break
                elif choice == "3":
                    break
                else:
                    print("\nInvalid choice")
        elif rarity == 2 or rarity == 3 or rarity == 4: # 3 in 8 chance
            print("\nTroll Eyballs")
            print("Spiked Club")
            print("\n1. Inspect items") # Inspect, accept or decline items
            print("2. Accept items")
            print("3. Decline items")
            while True:
                choice = input("\nChoose what you would lke to do with the items:") # Player chooses what to do
                if choice == "1":
                    print("\nTroll Socks - For crafting")
                    print("Spiked Club - Wooden club with nails")
                elif choice == "2":
                    player.add_item(Item("Troll Eyeballs", "For crafting"))
                    player.add_item(Item("Spiked Club", "Wooden club with nails"))
                    print("\nSuccess! Items added to your inventory.")
                    break
                elif choice == "3":
                    break
                else:
                    print("\nInvalid choice")
        else: # 4 in 8 chance
            print("\nRock")
            print("Spiked Club")
            print("\n1. Inspect items") # Inspect, accept or decline items
            print("2. Accept items")
            print("3. Decline items")
            while True:
                choice = input("\nChoose what you would lke to do with the items:") # Player chooses what to do
                if choice == "1":
                    print("\nRock - For crafting")
                    print("Spiked Club - Wooden club with nails")
                elif choice == "2":
                    player.add_item(Item("Rock", "For crafting"))
                    player.add_item(Item("Spiked Club", "Wooden club with nails"))
                    print("\nSuccess! Items added to your inventory.")
                    break
                elif choice == "3":
                    break
                else:
                    print("\nInvalid choice")

    def unique_behaviour(self):
        pass

    def reward(self, player): # Reward for defeating the Troll
        print("\nYour reward for defeating the Troll is two new crafting item")
        print("     + Rope x1 to your inventory")
        print("     + Iron Ingot x1 to your inventory")
        player.add_item(Item("Rope", "For crafting")) # Reward items added stright into craft inventory
        player.add_item(Item("Iron Ingot", "For crafting"))
        print("\nHere is the content of your inventory")
        for item in player.craft_inventory:
            print(f"  - {item}")


class Zombie(Enemy): # Zombie enemy - easy level
    def __init__(self, name="zombie", hp=20): # Has the lowest hp
        super().__init__(name, hp)

    def attack(self, character): # Zombie attacks player
        damage = random.randint(5, 10)
        print(f"{self.name} attacks {character.name} for {damage} damage!")
        character.take_damage(damage)

    def take_damage(self, damage): # Player attacks zombie
        self.hp -= damage
        print(f"{self.name} takes {damage} damage! (HP: {self.hp})")

    def enemy_drop(self, player): # Zombie drops items when you defeat it
        print("\nThe zombie has dropped some items:")
        rarity = random.randint(1,4)
        if rarity == 1:
            print("\nZombie Leg")
            print("Zombie Snot")
            print("\n1. Inspect items") # Inspect, accept or decline items
            print("2. Accept items")
            print("3. Decline items")
            while True:
                choice = input("\nChoose what you would lke to do with the items:") # Player chooses what to do
                if choice == "1":
                    print("\nZombie Leg - For crafting")
                    print("Zombie Snot - For crafting")
                elif choice == "2":
                    player.add_item(Item("Zombie Leg", "For crafting"))
                    player.add_item(Item("Zombie Snot", "For crafting"))
                    print("\nSuccess! Items added to your inventory.")
                    break
                elif choice == "3":
                    break
                else:
                    print("\nInvalid choice")
        else:
            print("\nSmall Knife")
            print("Zombie Snot")
            print("Rope")
            print("\n1. Inspect items") # Inspect, accept or decline items
            print("2. Accept items")
            print("3. Decline items")
            while True:
                choice = input("\nChoose what you would lke to do with the items:") # Player chooses what to do
                if choice == "1":
                    print("\nSmall Knife - Set of small throwing knives")
                    print("Zombie Snot - For crafting")
                    print("Rope - For crafting")
                elif choice == "2":
                    player.add_weapon(SmallKnife())
                    player.add_item(Item("Zombie Snot", "For crafting"))
                    player.add_item(Item("Rope", "For crafting"))
                    print("\nSuccess! Items added to your inventory.")
                    break
                elif choice == "3":
                    break
                else:
                    print("\nInvalid choice")

    def unique_behaviour(self):
        pass

    def reward(self, player): # Reward for defeating the zombir
        print("\nYour reward for defeating the Zombie is a new crafting item")
        print("     + Rock x1 to your inventory")
        player.add_item(Item("Rock", "For crafting")) # Item added stright to craft inventory

# Class for crafting weapons and defensive items
class Crafting:
    def show_recipes(self): # Displays a list of craftable items and the "ingredients"
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
        print("\n5. Double Attack Potion- Allows you to have two turns attacking")
        print("     - Troll Socks x1")
        print("     - Rope x1")
        print("\n6. Double Damage Potion- Doubles the damage of your weapon for one turn")
        print("     - Zombie leg x1")
        print("     - Stick x1")
        print("\n7. Block Potion- Block the enemys attack")
        print("     - Zombie Snot x1")
        print("     - Rock x1")

    def craft1(self, player): # Crafts a wooden sword, adds to inventory and removes the items you used
        player.add_weapon(WoodenSword())
        player.remove_item(Item("Stick", "For crafting"))
        player.remove_item(Item("Rope", "For crafting"))
        print("\nSuccess!")
        print("A Wooden Sword was added to your weapons inventory")

    def craft2(self, player): # Crafts a wooden shield, adds to inventory and removes the items you used
        player.add_weapon(WoodenShield())
        player.add_item(Item("Wooden Shield", "A basic wooden shield"))
        player.remove_item(Item("Rock", "For crafting"))
        player.remove_item(Item("Rope", "For crafting"))
        print("\nSuccess!")
        print("A Wooden Shield was added to your inventory")

    def craft3(self, player): # Crafts a forged longsword, adds to inventory and removes the items you used
        player.add_weapon(ForgedLongsword())
        player.remove_item(Item("Iron Ingot", "For crafting"))
        player.remove_item(Item("Rope", "For crafting"))
        print("\nSuccess!")
        print("A Forged Longsword was added to your weapons inventory")

    def craft4(self, player): # Crafts a health potion, adds to inventory and removes the items you used
        player.add_weapon(HealthPotion())
        player.remove_item(Item("Zombie Snot", "For crafting"))
        player.remove_item(Item("Troll Eyeballs", "For crafting"))
        print("\nSuccess!")
        print("A Health Potion was added to your inventory")

    def craft5(self, player): # Crafts a double attack, adds to inventory and removes the items you used
        player.add_weapon(DoubleAttackPotion())
        player.remove_item(Item("Troll Socks", "For crafting"))
        player.remove_item(Item("Rope", "For crafting"))
        print("\nSuccess!")
        print("A Double Attack was added to your inventory")

    def craft6(self, player): # Crafts a double damage, adds to inventory and removes the items you used
        player.add_weapon(DoubleDamagePotion())
        player.remove_item(Item("Zombie Leg", "For crafting"))
        player.remove_item(Item("Stick", "For crafting"))
        print("\nSuccess!")
        print("A Double Damage was added to your inventory")

    def craft7(self, player): # Crafts a block, adds to inventory and removes the items you used
        player.add_weapon(BlockPotion())
        player.remove_item(Item("Zombie Snot", "For crafting"))
        player.remove_item(Item("Rock", "For crafting"))
        print("\nSuccess!")
        print("A Block was added to your inventory")

    def craft_menu(self, player): # Crafting menu so players can choose what to craft
        while True:
            craft_choice = input("\nPlease choose which item you wish to craft or type 8 to cancel craft:")
            if craft_choice == "1": # Player craft wooden sword
                if Item("Stick", "For crafting") in player.craft_inventory and Item("Rope", "For crafting") in player.craft_inventory:
                    self.craft1(player)
                    break
                else:
                    print("\nYou do not have the correct items to craft this")
            elif craft_choice == "2": # Player crafts wooden shield
                if Item("Rock", "For crafting") in player.craft_inventory and Item("Rope", "For crafting") in player.craft_inventory:
                    self.craft2(player)
                    break
                else:
                    print("\nYou do not have the correct items to craft this")
            elif craft_choice == "3": # Player crafts forged longsword
                if Item("Iron Ingot", "For crafting") in player.craft_inventory and Item("Rope", "For crafting") in player.craft_inventory:
                    self.craft3(player)
                    break
                else:
                    print("\nYou do not have the correct items to craft this")
            elif craft_choice == "4": # Player crafts health potion
                if Item("Zombie Snot", "For crafting") in player.craft_inventory and Item("Troll Eyeballs", "For crafting") in player.craft_inventory:
                    self.craft4(player)
                    break
                else:
                    print("\nYou do not have the correct items to craft this")
            elif craft_choice == "5": # Player crafts double attack potion
                if Item("Troll Socks", "For crafting") in player.craft_inventory and Item("Rope", "For crafting") in player.craft_inventory:
                    self.craft5(player)
                    break
                else:
                    print("\nYou do not have the correct items to craft this")
            elif craft_choice == "6": # PLayer crafts double damage potion
                if Item("Zombie Leg", "For crafting") in player.craft_inventory and Item("Stick", "For crafting") in player.craft_inventory:
                    self.craft6(player)
                    break
                else:
                    print("\nYou do not have the correct items to craft this")
            elif craft_choice == "7": # Player crafts block potion
                if Item("Zombie Snot", "For crafting") in player.craft_inventory and Item("Rock", "For crafting") in player.craft_inventory:
                    self.craft7(player)
                    break
                else:
                    print("\nYou do not have the correct items to craft this")
            elif craft_choice == "8": # Option to close the craft menu and go back to fighting
                player.add_weapon(BareHands())
                print("Exiting craft menu")
                break
            else:
                print("\nInvalid choice")

        
# Combat between the player and an enemy
def combat(player, enemy):
    print("\nTime to fight!")
    print(f"\nA wild {enemy.name} appears!")
    while player.is_alive() and enemy.is_alive():
        # Player's turn
        player.show_equipped_items() # Shows player which items they have equipped
        print("\nYour turn:")
        print("1. Attack")
        print("2. Equip/Use items")
        print("3. Show Inventory")
        print("4. Craft")
        action = input("Choose your action: ") # Player chooses

        if action == '1': # Player chooses to attack
            if player.equipped_weapon == None:
                weapon = BareHands()
                weapon.equip_weapon(player)
            player.attack(enemy)
        elif action == "2": # Allows player to equip items or use potions
            option = input("\nWould like to 1 equip an item or 2 use a potion: ")
            if option == "1":
                player.show_weapon_inventory()
                while True:
                    found = False
                    choice = input("\nPlease type which weapon you would like to equip: ").strip().title()
                    for item in player.weapon_inventory:
                        if choice == item.name:
                            if isinstance(item, Weapon):
                                item.equip_weapon(player)
                            elif isinstance(item, Defence):
                                item.equip_defence(player)
                            found = True
                            break
                    if found:
                        print(f"{choice} has been equipped!")
                        break
                    else:
                        print("\nInvalid choice")
                continue # Skip enemy turn to allow further action after equipping a weapon.
            elif option == "2":
                for item in player.weapon_inventory:
                    if item.description == "potion":
                        print(item.name)
                        #potion = input("Which of your potions would youi like to use:")
                    else:
                        print("\nYou do not have any potions to use")

                '''potion = HealthPotion()
                potion.use_potion(player)
                print(player.hp)'''
                continue # Skip enemy turn to allow further action after using a potion.
        elif action == '3': # Shows players inventory
            player.show_craft_inventory()
            player.show_weapon_inventory()
            continue  # Skip enemy turn to allow further action after checking inventory.
        elif action == "4": # Allows player to craft items
            crafter = Crafting()
            crafter.show_recipes()
            player.show_craft_inventory()
            crafter.craft_menu(player)
            continue # Skip enemy turn to allow further action after crafting.
        else:
            print("Invalid action. Please choose 1, 2, or 3.")
            continue

        # Enemy's turn if still alive
        if enemy.is_alive():
            print(f"\n{enemy.name}'s turn:")
            enemy.attack(player)

    if player.is_alive(): # If the payer defeats the enemy
        print(f"\nYou defeated the {enemy.name}!")
        enemy.reward(player)
        enemy.enemy_drop(player)
    else:
        print("\nYou have been defeated.")

# Main menu used to run the game
def main_menu():
    while True:
        print("\n=== RPG Starter Adventure ===") # Displays the menu to players
        print("1. Start Game")
        print("2. Load data")
        print("3. Exit")
        choice = input("Enter your choice: ") # player chooses
        if choice == '1':
            # Displays the enemys you with be fighting
            print("\nThere are three enemies you will be fighting:")
            print("   Zombie     level - easy")  
            print("   Troll      level - medium")
            print("   Goblin     level - hard")
            name = input("\nEnter your character's name: ") # Player chooses there name
            player = Character(name)
            player.add_item(Item("Stick", "For crafting")) # Add some basic crafting items when they start
            player.add_item(Item("Rope", "For crafting"))
            player.add_item(Item("Rope", "For crafting"))
            crafter = Crafting()
            crafter.show_recipes()
            player.show_craft_inventory()
            crafter.craft_menu(player)
            combat(player, Zombie()) # Fight with each enemy
            combat(player, Troll())
            combat(player, Goblin())
        elif choice == "2": # Save data to a file
            pass
        elif choice == "3": # Exit game
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__": # Run game
    main_menu()
