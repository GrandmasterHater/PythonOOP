import random

# 4.1.

class FuelTank:
    
    def __init__(self, max_amount: float):
        self.__max_amount = max_amount # литры
        self.__current_amount = 0.0 # литры
        self.__weight = 0.0 # кг
        self.__has_fire_protection = True
        self.__fuel_type = 'Авиационный керосин'
        self.__current_fuel_type = ''
        
    def GetFuel(self, amount: float) -> float:
        
        result_amount = amount if self.__current_amount >= amount else self.__current_amount
        self.__current_amount -= result_amount
        
        return result_amount
        
    def Refuel(self, amount: float):
        new_amount = self.__current_amount + amount
        self.__current_amount = new_amount if new_amount <= self.__max_amount else self.__max_amount
        
    def GetFuelAmount(self) -> float: # В %
        return (self.__current_amount * 100.0) / self.__max_amount


class Engine:
    
    def __init__(self, fuel_tank: FuelTank):
        self.__power = 0 # л/с
        self.__max_thrust = 100 # %
        self.__current_thrust = 0 # %
        self.__engine_service_life = 0.0 # Моточасы
        self.__fuel_tank = fuel_tank
        self.__is_started = False
        
    def Start(self):
        if not self.__is_started and self.__current_thrust == 0 and self.fuel_tank.GetFuelAmount() > 0:
            self.is_started = True
            # Запуск процесса расхода топлива и моточасов.
        
    def Stop(self):
        if self.__is_started:
            self.__is_started = False
            # Остановка процесса расхода топлива и моточасов.
                
    def SetThrust(self, thrust: int):
        self.__current_thrust = thrust
            
    
class Plane:
    
    def __init__(self, engine: Engine, fuel_tank: FuelTank):
        self.__max_takeoff_weight = 0.0 # кг
        self.__max_landing_weight = 0.0 # кг
        self.__plain_weight = 0.0 # кг
        self.__fuel_tank = fuel_tank
        self.__engine = engine
        self.__roll = 0.0 # град
        self.__pitch = 0.0 # град
        self.__yaw = 0.0 # град
        
    def SetRudderPosition(self, roll: float, pitch: float, yaw: float):
        # Валидации углов
        self.__roll = roll 
        self.__pitch = pitch
        self.__yaw = yaw
        
    def Start(self):
        self.__engine.Start()
        
    def Stop(self):
        self.__engine.Stop()
    
    def SetThrottlePosition(self, position: int): # 0-100% 
        self.__engine.SetThrust(position)
    
    def Refuel(self, amount: float):
        self.__fuel_tank.Refuel(amount)


class JetEngine(Engine):

    def __init__(self, fuel_tank: FuelTank):
        super().__init__(fuel_tank)
    
    # Управление форсажной камерой, дополнительная подача топлива после турбины
    def SetAfterburner(self, is_enabled: bool):
        pass
    
    # Получить температуру компрессора
    def GetСompressorЕemperature(self) -> float:
        pass
    
class PistonEngine(Engine):
    
    def __init__(self, fuel_tank: FuelTank):
        super().__init__(fuel_tank)
        
    # Управление противообледенительной системой винта.
    def SetPropellerAntiIcing(self, enable: bool):
        pass
        
    # Рычаг шага винта, которым задаются нужные обороты винта.
    def SetPropellerPitch(self, rpm: float):
        pass

    # Рычаг управления топливо-воздушной смеси: регулирует соотношение топливо/воздух (экономия топлива или максимальная мощность).
    def SetMixture(self, ratio: float):
        pass
    
    # Температура масла двигателя
    def GetOilTemperature(self) -> float:
        pass
    
class TransportAircraft(Plane):
    
    def __init__(self, engine: Engine, fuel_tank: FuelTank):
        super().__init__(engine, fuel_tank)
        
    def LoadCargo(self, cargo: str):
        pass
    
    def UnloadCargo(self) -> str:
        pass
    
class MilitaryAircraft(Plane):
    
    def __init__(self, engine: Engine, fuel_tank: FuelTank, weapon: str):
        super().__init__(engine, fuel_tank)
        self.__weapon = weapon
        
    def Shoot(self):
        pass
    
    def ReloadWeapon(self) -> str:
        pass
    
fuel_tank_transport = FuelTank(10000)  
transport_engine = PistonEngine(fuel_tank_transport)
transpor_plane = TransportAircraft(transport_engine, fuel_tank_transport)

fuel_tank_military = FuelTank(5000)  
military_engine = JetEngine(fuel_tank_military)
military_plane = TransportAircraft(military_engine, fuel_tank_military)


# 4.2.

# В примере увидел полиморфизм подтипов поскольку метод do_something_with_animal принимает любой объект типа Animal
# и во время вызова уже опдбирается конкретная реализация foo переданного типа. Но вот насчёт параметрического 
# полиморфизма не понял - в методе ведь указано с каким типом может работать метод, значит мы уже зависим от 
# конкретного контракта и не можем работать с другими типами, поскольку нужно быть уверенным что у них есть foo.

# 4.3.

class Animal:
    def foo(self):
        pass

class Cat(Animal):
    def foo(self):
        print("Кошка мурлычет")

class Bird(Animal):
    def foo(self):
        print("Птица поет")
       
def do_something_with_animal_list(animals: list[Animal]) -> list[Animal]:
    animals.clear()
    
    animal_generators = [lambda: Cat(), lambda: Bird()]
    
    for index in range(500):
        animal = random.choice(animal_generators)()
        animals.append(animal)
    
    return animals
    
barsik = Cat()
galka = Bird()
ams = [barsik, galka]

ams = do_something_with_animal_list(ams)

for ani in ams:
    ani.foo()
    
# Результат достигается благодаря полиморфизму подтипов. 
# При вызове метода foo вы время выполнения выбирается версия метода соответсвующая конкретному типу.
