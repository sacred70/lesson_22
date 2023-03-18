# в задании представлен один класс который нужно разбить на 4
# Воин      - Warrior
# Лекарь    - Healer
# Дерево    - Tree
# Ловушка   - Trap

# Воин в состоянии защищаться от врагов, атаковать и передвигаться по полю
# Лекарь может защищаться, лечить воина и панически спасаться бегством
# Дерево может защищаться (попробуй разруби сходу) и гореть в огне
# Ловушка не может ничего кроме как атаковать того, кто на нее наступит
# Для решения этой задачи не используйте наследование

class Warrior:
    # Воин
    def attack(self):
        pass
    def defense(self):
        # защита
        pass
    def move(self):
        # двигаться
        pass
class Healer:
class Tree:
class Trap:

    ##
    # тут представлено поведение четырех различных игровых объектов:
    # - воина
    # - лекаря
    # - дерева
    # - ловушки

    def attack(self):
        pass

    def defense(self):
        # защита
        pass

    def move(self):
        # двигаться
        pass

    def healer_defense(self):
        pass

    def healer_move(self):
        pass

    def heal(self):
        # лечить
        pass

    def tree_defense(self):
        pass

    def on_fire(self):
        # нет огоня
        pass

    def trap_attack(self):
        print("It's a trap!")

if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()