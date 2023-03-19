# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)

x_coord = 4
y_coord = 5
direction = "UP"
speed = 1
def direction_all(x_coord= x_coord, y_coord=y_coord, direction=direction, speed=1):

    if direction == 'UP':
        new_y = y_coord + speed
        new_x = x_coord
    elif direction == 'DOWN':
        new_y = y_coord - speed
        new_x = x_coord
    elif direction == 'LEFT':
        new_y = y_coord
        new_x = x_coord - speed
    elif direction == 'RIGTH':
        new_y = y_coord
        new_x = x_coord + speed
    return new_x, new_y


#print(direction_all(2,5, "UP", 10))


class Unit:
    def move(self, field, is_fly, crawl, speed=1):

        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            x = direction_all(speed=speed)[0]
            y = direction_all(speed=speed)[1]

        if crawl:
            speed *= 0.5
            x = direction_all(speed=speed)[0]
            y = direction_all(speed=speed)[1]

        field = (x,y)
        return field
is_fly = True
crawl = False
field = []

unit = Unit()
print(unit.move(field, is_fly, crawl, speed=10))

#     ...
