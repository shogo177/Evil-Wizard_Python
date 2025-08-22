# Lee Evil Wizard prog
import random
# This code implements a simple text-based RPG battle system where the player can choose a character class and fight against an Evil Wizard.
# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.block_next = False  # For shield/evade mechanics

    def attack(self, opponent):
        # Randomize attack damage (between 80% - 120% of attack power)
        damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        if opponent.block_next:  # If opponent has shield/evade active
            print(f"{opponent.name} evades or blocks the attack!")
            opponent.block_next = False
        else:
            opponent.health -= damage
            print(f"{self.name} attacks {opponent.name} for {damage} damage!")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = random.randint(15, 30)  # Heal between 15-30 HP
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"{self.name} heals for {heal_amount}! Health is now {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def special_ability(self, opponent):
        print(f"{self.name} uses Power Strike!")
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} deals {damage} damage to {opponent.name}!")


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_ability(self, opponent):
        print(f"{self.name} casts Fireball!")
        damage = self.attack_power + random.randint(10, 20)
        opponent.health -= damage
        print(f"{self.name} burns {opponent.name} for {damage} damage!")


# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=20)

    def special_ability(self, opponent):
        choice = input("Choose ability: 1. Quick Shot (double attack)  2. Evade (dodge next attack)\n")
        if choice == "1":
            print(f"{self.name} uses Quick Shot!")
            for _ in range(2):
                self.attack(opponent)
        elif choice == "2":
            print(f"{self.name} prepares to evade the next attack!")
            self.block_next = True
        else:
            print("Invalid choice! Turn wasted.")


# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=22)

    def special_ability(self, opponent):
        choice = input("Choose ability: 1. Holy Strike (bonus damage)  2. Divine Shield (block next attack)\n")
        if choice == "1":
            print(f"{self.name} uses Holy Strike!")
            damage = self.attack_power + 15
            opponent.health -= damage
            print(f"{self.name} smites {opponent.name} for {damage} damage!")
        elif choice == "2":
            print(f"{self.name} raises a Divine Shield and will block the next attack!")
            self.block_next = True
        else:
            print("Invalid choice! Turn wasted.")


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        regen = random.randint(5, 10)
        self.health += regen
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates {regen} health! Current health: {self.health}/{self.max_health}")


# Function to create character
def create_character():
    print("Choose your character class:")
    print("1. Swag Warrior")
    print("2. Swag Mage")
    print("3. Swag Archer")
    print("4. Swag Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


# Battle System
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")
        show_stats = False  # flag

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            show_stats = True  # defer stats display until end
        else:
            print("Invalid choice. Try again.")
            continue  

                 # Wizard only acts if player did a "real move"
        if wizard.health > 0 and choice in ['1', '2', '3']:
            print("\n--- Wizard's Turn ---")
            wizard.regenerate()
            wizard.attack(player)

        # Show stats at the end of the round (below last actions)
        if show_stats:
            print("\n📊 Current Stats:")
            player.display_stats()
            wizard.display_stats()

        # Check defeat
        if player.health <= 0:
            print(f"\n💀 {player.name} has been defeated! The Evil Wizard reigns supreme.")
            break

    if wizard.health <= 0:
        print(f"\n🎉 Victory! The wizard {wizard.name} has been defeated by {player.name}!")


def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()
