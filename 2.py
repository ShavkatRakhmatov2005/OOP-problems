class Car:
    def __init__(self,name:str,turi:str,narxi,ishlab_chiqarilgan_yili:int):
        self.name=name
        self.turi=turi
        self.narxi=narxi
        self.ishlab_chiqarilgan_yili=ishlab_chiqarilgan_yili
    def info(self):
        print(f'''
Name:{self.name}
Turi:{self.turi}
Narxi:{self.narxi}$
Ishlab chiqarilgan yili:{self.ishlab_chiqarilgan_yili}
''')
cars=[]
for i in range(1,int(input())+1):
    name=input("\nName: ")
    turi=input("turi: ")
    narxi=int(input("Narxi: ") or 4000)
    ishlab_chiqarilgan_yili=input("Ishlab chiqarilgan yili: ")
    car=Car(name,turi,narxi,ishlab_chiqarilgan_yili)
    cars.append(car)
    #narxlarini sortlash
    sorted_cars=sorted(cars,key=lambda x:x.narxi)
for car in sorted_cars:
    car.info()

