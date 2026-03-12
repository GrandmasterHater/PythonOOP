class FuelTank:
    
    def __init__(self, max_amount: float):
        self.max_amount = max_amount # литры
        self.current_amount = 0.0 # литры
        self.weight = 0.0 # кг
        self.has_fire_protection = True
        self.fuel_type = 'Авиационный керосин'
        self.current_fuel_type = ''
        
    def GetFuel(self, amount: float) -> float:
        
        result_amount = amount if self.current_amount >= amount else self.current_amount
        self.current_amount -= result_amount
        
        return result_amount
        
    def Refuel(self, amount: float):
        new_amount = self.current_amount + amount
        self.current_amount = new_amount if new_amount <= self.max_amount else self.max_amount
        
    def GetFuelAmount(self) -> float: # В %
        return (self.current_amount * 100.0) / self.max_amount


class Engine:
    
    def __init__(self, fuel_tank: FuelTank):
        self.power = 0 # л/с
        self.max_thrust = 100 # %
        self.is_afterburner_available = False 
        self.current_thrust = 0 # %
        self.engine_service_life = 0.0 # Моточасы
        self.fuel_tank = fuel_tank
        self.is_started = False
        
    def Start(self):
        if not self.is_started and self.current_thrust == 0:
            self.is_started = True
            # Запуск процесса расхода топлива и моточасов.
        
    def Stop(self):
        if self.is_started:
            self.is_started = False
            # Остановка процесса расхода топлива и моточасов.
                
    def SetThrust(self, thrust: int):
        self.current_thrust = thrust
            
    
class Plane:
    
    def __init__(self, engine: Engine, fuel_tank: FuelTank):
        self.max_takeoff_weight = 0.0 # кг
        self.max_landing_weight = 0.0 # кг
        self.plain_weight = 0.0 # кг
        self.fuel_tank = fuel_tank
        self.engine = engine
        self.roll = 0.0 # град
        self.pitch = 0.0 # град
        self.yaw = 0.0 # град
        
    def SetRudderPosition(self, roll: float, pitch: float, yaw: float):
        # Валидации углов
        self.roll = roll 
        self.pitch = pitch
        self.yaw = yaw
        
    def Start(self):
        self.engine.Start()
        
    def Stop(self):
        self.engine.Stop()
    
    def SetThrottlePosition(self, position: int): # 0-100% 
        self.engine.SetThrust(position)
    
    def Refuel(self, amount: float):
        self.fuel_tank.Refuel(amount)


tank = FuelTank(5000)
engine = Engine(tank)
 
plane = Plane(engine, tank)
plane.max_takeoff_weight = 10000
plane.Refuel(5000)
plane.Start()
print('Engine is started: ' + str(plane.engine.is_started)) # False
plane.SetRudderPosition(15, 5, -10)
print(f'Roll:{plane.roll} Pitch:{plane.pitch} Yaw:{plane.yaw}') # 15 5 -10
 
plane.SetThrottlePosition(50)
print('Current thrust: ' + str(plane.engine.current_thrust)) # 50
 
plane.Stop()
print('Engine is started: ' + str(plane.engine.is_started)) # False
