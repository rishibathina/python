import random

class Pokemon:
    
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
    def __str__(self):
        return str(self.name) + '(' + str(self.health) + ')' + '\n' + 'Att: ' + str(self.attack_power) + ' ' + 'Def: ' + str(self.defense)
    
    def calculate_damage(self, other_poke):
        '''This method calculates damage done using aa specific fomula.'''
        r = random.uniform(0.85, 1)
        damage_done = (((12 * self.attack_power) / (5 * other_poke.defense)) + 2) * r
        return damage_done
    
    def attack(self, other_poke):
        '''Charmander.attack(Bulbasaur)
        This sets the new health bar and applies the damage.'''
        new_damage_done = int(round(self.calculate_damage(other_poke)))
        other_poke.health = other_poke.health - new_damage_done
        if other_poke.health <= 0:
            other_poke.health = 0
            print (str(self.name) + ' has done ' + str(new_damage_done) + ' damage!')
            print (str(other_poke.name) + ' has fainted!')
        else:
            print (str(self.name) + ' has done ' + str(new_damage_done) + ' damage!')
            return other_poke.health