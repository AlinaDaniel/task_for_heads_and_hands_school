import random


class Creature:
    max_health = 100

    def __init__(self, attack, defense, health, damage):
        self._attack = Creature.__checked_attack(attack)
        self._defense = Creature.__checked_defense(defense)
        self._health = Creature.__checked_health(health)
        self._damage = damage
        self._alive = True
        self._number_of_healing = 0

    @staticmethod
    def __checked_attack(attack):
        if not isinstance(attack, int):
            print("Некорректный тип значения для параметра 'Атака'")
            raise TypeError
        if 1 <= attack <= 20:
            return attack
        else:
            print("Некорректное значение для параметра 'Атака'")
            raise ValueError

    @staticmethod
    def __checked_defense(defense):
        if not isinstance(defense, int):
            print("Некорректный тип значения для параметра 'Защита'")
            raise TypeError
        if 1 <= defense <= 20:
            return defense
        else:
            print("Некорректное значение для параметра 'Защита'")
            raise ValueError

    @staticmethod
    def __checked_health(health):
        if not isinstance(health, int):
            print("Некорректный тип значения для параметра 'Здоровье'")
            raise TypeError
        if 1 <= health <= Creature.max_health:
            return health
        elif health == 0:
            print("Попытка создать мертвую сущность")
            raise ValueError
        else:
            print("Некорректное значение для параметра 'Здоровье'")
            raise ValueError

    @staticmethod
    def __checked_damage(damage):
        if not isinstance(damage, range):
            print("Некорректный тип значения для параметра 'Урон'")
            raise TypeError
        if damage[-1] <= Creature.max_health and damage[0] >= 0:
            return damage
        else:
            print("Некорректное значение для параметра 'Урон'")
            raise ValueError

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
            new_health = self.health + 0.5 * Creature.max_health
            if new_health > Creature.max_health:
                self._health = Creature.max_health
            else:
                self._health = new_health
            self._number_of_healing += 1
        else:
            print("Исцеление недоступно")

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

    def __str__(self):
        return f"Сущность Игрок:\nАтака: {self.attack}\nЗащита:" \
               f"{self.defense}\nЗдоровье:{self.health}\nУрон:{self.damage}"


class Monster(Creature):
    def __init__(self, attack, defense, health, damage):
        super().__init__(attack, defense, health, damage)

    def __str__(self):
        return f"Сущность Монстр:\nАтака: {self.attack}\nЗащита:" \
               f"{self.defense}\nЗдоровье:{self.health}\nУрон:{self.damage}"


def game():
    g = Gamer(20, 10, 100, range(50))
    print(g)
    m = Monster(15, 5, 90, range(40))
    print(m)
    print("---")
    g.hit(m)
    print(g)
    print(m)
    print("---")
    m.healing()
    print(g)
    print(m)
