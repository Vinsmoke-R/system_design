class Character():
    def __init__(self, name, element, lvl, health, attack, defense, elemental_mastery, crit_rate, crit_damage, energy_recharge, constellation):
        self.name = name
        self.element = element
        self.lvl = lvl
        self.health = health
        self.attack = attack
        self.defense = defense
        self.elemental_mastery = elemental_mastery
        self.crit_rate = crit_rate
        self.crit_damage = crit_damage
        self.energy_recharge = energy_recharge
        self.constellation = constellation


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