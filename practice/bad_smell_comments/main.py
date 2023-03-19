# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    # ...
    def moving_user_on_field(self, field,
                             x_coordin,
                             y_coordin,
                             direction,
                             fly_user,
                             crawling_user,
                             speed_default=1):
        """
        Функция реализует перемещение юнита по полю.
        """
        # Проверка состояния пользователя, летит/ползет
        if fly_user and crawling_user:
            raise ValueError('Рожденный ползать летать не должен!')

        # логика в режиме полета
        if fly_user:
            speed_default *= 1.2  # в полете скорость выше
            if direction == 'UP':  # движение вверх
                new_y = y_coordin + speed_default  # увеличим нашу координату Y на нашу текущую скорость
                new_x = x_coordin  # Х без изменений
            elif direction == 'DOWN':  # движение вниз
                new_y = y_coordin - speed_default  # уменьшим нашу координату Y на нашу текущую скорость
                new_x = x_coordin  # Х без изменений
            elif direction == 'LEFT':  # движение влево
                new_y = y_coordin  # Y без изменений
                new_x = x_coordin - speed_default  # уменьшим нашу координату Х на нашу текущую скорость
            elif direction == 'RIGHT':  # движение вправо
                new_y = y_coordin  # Y без изменений
                new_x = x_coordin + speed_default  # увеличим нашу координату Х на нашу текущую скорость
        if crawling_user:
            speed_default *= 0.5  # ползком скорость ниже
            if direction == 'UP':  # движение вверх
                new_y = y_coordin + speed_default  # увеличим нашу координату Y на нашу текущую скорость
                new_x = x_coordin  # Х без изменений
            elif direction == 'DOWN':  # движение вниз
                new_y = y_coordin - speed_default  # уменьшим нашу координату Y на нашу текущую скорость
                new_x = x_coordin  # Х без изменений
            elif direction == 'LEFT':  # движение влево
                new_y = y_coordin  # Y без изменений
                new_x = x_coordin - speed_default  # уменьшим нашу координату Х на нашу текущую скорость
            elif direction == 'RIGHT':  # движение вправо
                new_y = y_coordin  # Y без изменений
                new_x = x_coordin + speed_default  # увеличим нашу координату Х на нашу текущую скорость

            field.set_unit(x=new_x, y=new_y, unit=self)  # новые координаты положения пользователя

#     ...
