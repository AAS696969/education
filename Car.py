class Car:  # Определяем новый класс с именем Car
    def __init__(self, model, year, engine, price, odometer, ):
        self.model = str(model)
        self.year = int(year)
        self.engine = int(engine)
        self.price = str(price)
        self.odometer = int(odometer)
        self.wheels = 4

    def descrition(self):
        descrition = (f" Модель: {self.model}, Год выпуска: {self.year}, Двигатель: {self.engine}, Цена: {self.price},"
                      f" Пробег: {self.odometer}, Количество колес: {self.wheels}")
        return descrition

avto1 = Car("KIA", 2015, 2000, "1 500 000 руб", 150000)
avto2 = Car("BMW", 2016, 3000, "3 500 000 руб", 100000)

avto1.descrition()
avto2.descrition()

class Truck(Car):  # Определяем новый класс с именем Truck
    def __init__(self,  model, year, engine, price, odometer, ):
        super().__init__(model, year, engine, price, odometer)
        self.truck_wheels = 8

    def descrition(self):
        descrition = (f" Модель: {self.model}, Год выпуска: {self.year}, Двигатель: {self.engine}, Цена: {self.price},"
                      f" Пробег: {self.odometer}, Количество колес: {self.truck_wheels}")
        return descrition

avtotruck1 = Truck( "Kamaz", 2010,4000,"3 000 000 руб", 300000 )
avtotruck1.descrition()

print(avto1.descrition())
print(avto2.descrition())
print(avtotruck1.descrition())