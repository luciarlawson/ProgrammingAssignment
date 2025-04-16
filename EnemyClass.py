import random


class Enemy:
    def __init__(self, name, hp=50):
        self.name = name
        self.hp = hp

    def is_alive(self):
        return self.hp > 0

    def attack(self, character):
        damage = random.randint(5, 10)
        print(f"{self.name} attacks {character.name} for {damage} damage!")
        print("\nDo you wish to take the damage or try and defend?")
        print("1. take damage")
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
