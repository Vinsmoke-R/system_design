class Character():
    def __init__(self):
        self.element = None
        self.health = None
        self.attack = None
        self.defense = None
        self.elemental_mastery = None
        self.crit_rate = None
        self.crit_damage = None
        self.energy_recharge = None
        self.constellation = None


    def use_ability(self):
        pass

    def use_burst(self):
        pass

    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense // 2)
        self.health -= actual_damage
        print(f"{self.name} took {actual_damage} damage. HP: {self.health}")
    
    def attack(self, opponent):
        damage = self.attack 
        opponent.take_damage(damage)
    
    def is_alive(self):
        return self.health > 0