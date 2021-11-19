class Car:
    def __init__(self, make, mode, year):
        self.make = make
        self.mode = mode
        self.year = year
        self.o = 0
        self.gas = 0

    def get_descript(self):
        long_name = f"{self.year} {self.mode} {self.make}"
        return long_name

    def get_o(self):
        print(f"现在累计开了{self.o}公里")

    def update_o(self, m):
        if m >= self.o:
            self.o = m
        else:
            print("禁止回调")

    def incr_o(self, inc):
        self.o += inc

    def show_gas(self, g):
        self.gas = g
        print(f"当前添加了{self.gas}升汽油")


class Battery:
    def __init__(self, size=100):
        self.size = size

    def show_b(self):
        print(f"当前电量为{self.size}")

    def show_m(self):
        if self.size == 70:
            range = 200
        elif self.size == 100:
            range = 260
        print(f"还可以行驶{range}公里")


class E_car(Car):
    def __init__(self, make, mode, year):
        super().__init__(make, mode, year)
        self.battery = Battery()

    def show_gas(self, g):
        try:
            print(5/0)
        except ZeroDivisionError:
            print("纯电汽车没有油箱")


my_qin = E_car('BYD', 'qin', '2021')
print(my_qin.get_descript())
my_qin.battery.show_b()
my_qin.show_gas(1000)


"""
mycar = Car('volvo', 'XC90', '2020')
print(mycar.get_descript())
mycar.update_o(21_300)
mycar.get_o()
mycar.incr_o(100)
mycar.get_o()
"""
