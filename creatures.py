import random


class Creature:
    N = 0
    M = 0

    def __init__(self, attack, defense, health, damage):
        self._attack = attack
        self._defense = defense
        self._health = health
        self._damage = damage
        self._alive = True
        self._number_of_healing = 0

    @property
    def attack(self):
        return self._attack

    @property
    def defense(self):
        return self._defense

    @property
    def health(self):
        return self._health

    @property
    def damage(self):
        return self._damage

    @health.setter
    def health(self, new_health):
        if new_health <= 0:
            self._health = 0
            self._alive = False
            print(self, "умер")
        self._health = new_health

    def healing(self):
        if self._alive and self._number_of_healing < 3:
            self._health += 0.5 * Creature.N
            self._number_of_healing += 1

    def hit(self, victim):
        successful_hit = False
        attack_modifier = self._attack - victim.defense + 1
        if attack_modifier < 1:
            attack_modifier = 1
        for _ in range(attack_modifier):
            dice_roll_result = random.randint(1, 6)
            if dice_roll_result in [5, 6]:
                successful_hit = True
                break
        if successful_hit:
            victim.health -= random.choice(self._damage)


class Gamer(Creature):
    def __init__(self, attack, defense, health, damage):
        super().__init__(attack, defense, health, damage)


class Monster(Creature):
    def __init__(self, attack, defense, health, damage):
        super().__init__(attack, defense, health, damage)
