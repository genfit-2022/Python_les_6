#   4. Реализуйте базовый класс Car.
#
#   у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы:
#   go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);

#   опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;

#   добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;

#   для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
#   40 (WorkCar) должно выводиться сообщение о превышении скорости.

#   Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
#   Вызовите методы и покажите результат.
class Car:


    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police



    def go(self):
        return f'{self.name} осуществляет начало движения.'

    def stop(self):
        return f'{self.name} выполняет остановку.'

    def turn_right(self):
        return f'{self.name} выполняет поворот налево.'

    def turn_left(self):
        return f'{self.name} выполняет поворот налево.'

    def rev(self):
        return f'{self.name} осуществляет движение задним ходом.'

    def m_speed(self):
        return f'Текущая скорость {self.name} - {self.speed} км/ч.'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость в городе {self.name} - {self.speed} км/ч.')

        if self.speed > 40:
            return f'Скорость {self.name} больше разрешенной для городского автомобиля.'
        else:
            return f'Скорость {self.name} в допустимых пределах.'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля - {self.name} - {self.speed} км/ч.')

        if self.speed > 60:
            return f'Скорость {self.name} выше, чем разрешено для данного автомобиля.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейский автомобиль.'
        else:
            return f'{self.name} не полицейский автомобиль.'


audi = SportCar(100, 'черный', 'Audi TT', False)
vw = TownCar(30, 'красный', 'Volkswagen Golf', False)
opel = WorkCar(70, 'зелёный', 'Opel Zafira', False)
ford = PoliceCar(110, 'белый',  'Ford Fusion Hybrid', True)

print(f'{opel.name} - {opel.color}')
print(f'{vw.name} - {vw.color}')
print(opel.turn_left())
print(vw.rev())
print(f'Если {vw.rev()} - {audi.stop()} - {ford.go()}')
print(vw.show_speed())
print(ford.police())
print(ford.m_speed())
print(f'{opel.go()} - {opel.show_speed()}')
print(f'{ford.go()} - {ford.m_speed()}')
print(f'Is {audi.name} - полицейский автомобиль? {audi.is_police}')
print(f'Is {ford.name} - полицейский автомобиль? {ford.is_police}')
