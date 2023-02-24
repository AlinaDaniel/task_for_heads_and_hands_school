from creatures import Monster, Gamer


# Пример использования классов
def game():
    g = Gamer(attack=20, defense=10, health=100, damage=range(10, 50))
    print("Cоздана", g)
    print("---")
    m = Monster(attack=15, defense=5, health=90, damage=range(40))
    print("Cоздана", m)
    print("---")
    for round_number in range(1, 8):
        print(m.get_object_type(), "атаковал", g.get_object_type() + "a")
        m.hit(g)

        print(g.get_object_type(), "атаковал", m.get_object_type() + "a")
        g.hit(m)

        print(f"Результаты {round_number} раунда:")
        print(f"{g.get_object_type()} - Здоровье: {g.health}")
        print(f"{m.get_object_type()} - Здоровье: {m.health}")
        print("---")

        print(g.get_object_type(), "активирует исцеление")
        g.healing()
        print(f"{g.get_object_type()} - Здоровье: {g.health}")
        print("---")
        if not m.alive or not g.alive:
            break


if __name__ == '__main__':
    game()
