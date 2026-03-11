# 1.1.
#
#     Пример 1 - Мессенджер
#     Может содержать классы:
#      - User - хранит данные пользователя: id, никнейм, аватарка, статус онлайн, дата регистрации.
#      - ChatList - список всех чатов пользователя, наверное просто массив объектов Chat.
#      - Chat - чата, список участников, название, тип (личный или групповой), и список сообщений.
#      - Message - хранит текст сообщения, id отправителя, время отправки, тип (текст, картинка, файл) и статус (доставлено, прочитано).
#     
#     Пример 2 - игра про танки, самолёты и корабли.
#      - Vehicle - хранит основные данные о технике:название, тип (танк/самолёт/корабль), уровень, текущее HP.
#      - Hull/Airframe - корпус конкретного типа техники, отвечает за бронирование и прочность.
#      - Engine - мотор, хранит мощность и влияет на ходовые или лётные качества.
#      - Weapon - вооружение, содержит урон, скорострельность, дальность.
#      - PlayerProfile - профиль игрока: никнейм, статистика боёв, список техники в ангаре, валюта.
#      - Lobby - собирает игроков в команды по уровню техники и региону, хранит список участников и статус готовности.
#      - GameSession - описывает активный бой: карта, позиции техники, текущий счёт, оставшееся время.
#


# 1.2.
    
class Engine:
    power = 0 # л/с
    max_thrust = 100 # %
    is_afterburner_available = False 
    current_thrust = 0 # %
    engine_service_life = 0.0 # Моточасы
    
    
class FuelTank:
    fuel_amount = 0.0 # %
    weight = 0.0 # кг
    has_fire_protection = True
    fuel_type = 'Авиационный керосин'
    current_fuel_type = ''
    
class Plane:
    max_takeoff_weight = 0.0 # кг
    max_landing_weight = 0.0 # кг
    plain_weight = 0.0 # кг
    fuel_tank = FuelTank()
    engine = Engine()
    
engine = Engine()
engine.power = 200
engine.max_thrust = 100
engine.is_afterburner_available = False
engine.current_thrust = 0
engine.engine_service_life = 1500.0

fuel_tank = FuelTank()
fuel_tank.fuel_amount = 100.0
fuel_tank.weight = 150.0
fuel_tank.has_fire_protection = True
fuel_tank.fuel_type = 'Авиационный керосин'
fuel_tank.current_fuel_type = 'Авиационный керосин'

plane = Plane()
plane.max_takeoff_weight = 1200.0
plane.max_landing_weight = 1100.0
plane.plain_weight = 800.0
plane.fuel_tank = fuel_tank
plane.engine = engine

print("Параметры самолёта")
print("Масса пустого:", plane.plain_weight, "кг")
print("Макс. взлётная масса:", plane.max_takeoff_weight, "кг")
print("Макс. посадочная масса:", plane.max_landing_weight, "кг")

print("Двигатель")
print("Мощность:", plane.engine.power, "л/с")
print("Макс. тяга:", plane.engine.max_thrust, "%")
print("Текущая тяга:", plane.engine.current_thrust, "%")
print("форсаж:", plane.engine.is_afterburner_available)
print("Ресурс:", plane.engine.engine_service_life, "моточасов")

print("Топливный бак")
print("Топливо:", plane.fuel_tank.fuel_type)
print("Заполненность:", plane.fuel_tank.fuel_amount, "%")
print("Масса топлива:", plane.fuel_tank.weight, "кг")
print("Пожарная защита:", plane.fuel_tank.has_fire_protection)  
    
# 1.3.
first_engine = Engine()

first_plane = Plane()
first_plane.engine = first_engine

secont_plane = Plane()
first_plane.engine = first_engine # Побочный эффект! Самолёты будут ссылаться на один и тот же объект двигателя.