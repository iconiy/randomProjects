class Person:
    """Setup person class here, define starting values"""
    def __init__(self):
        self.starting_mana = 0
        self.starting_potions = 5
        self.name = "Simon"
        self.energy = 50
        self.used_potions = 0
        self.max_mana = 250

    # Setup potion method here, recharges energy with each use
    def potion(self):
        self.energy += 50
        self.starting_potions -= 1
        self.used_potions += 1
        print('Potion used')
        return self.energy

    # Mediate class and its while loop
    def meditate(self):
        while self.energy > 0 and self.starting_mana < self.max_mana - 1:
                self.energy -= 1
                # Potion gets used here if energy drops to 0
                if self.energy == 0 and self.starting_potions > 0:
                    Person.potion(self)
                self.starting_mana += 3
                print(str(self.starting_mana) + " mana")
                print(str(self.energy) + " energy")
        print(f'{self.name} used {self.used_potions} potions, and has {self.energy} remaining energy and {self.starting_potions} potions remaining.')



if __name__ == "__main__":
    Simon = Person()
    Simon.meditate()