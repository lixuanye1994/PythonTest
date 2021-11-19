class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def sit(self):
        print(f"{self.name}坐下了")
  
    def roll_over(self):
        print(f"{self.name}翻滚了")


mydog = Dog('wangawng', 2)

print(f"小狗名字是{mydog.name}，它今年{mydog.age}岁了")

mydog.sit()
mydog.roll_over()
