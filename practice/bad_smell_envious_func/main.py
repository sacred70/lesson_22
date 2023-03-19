# Вам не кажется, что CubeVolumeCalculator 
# чаще дергает методы класса Cube? Исправьте так, 
# чтобы избавиться от лишних обращений к классу Cube


class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_list(self):
        return [self.x, self.y, self.z]


cub = Cube(1, 2, 3)
print(cub.get_list())


class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube):
        return cub.get_list()[0] * cub.get_list()[1] * cub.get_list()[2]


if __name__ == "__main__":
    calc = CubeVolumeCalculator()
    print(calc.calc_cube_volume(cub))
