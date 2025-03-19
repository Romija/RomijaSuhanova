from abc import ABC, abstractmethod
import random

# Abstrakta klase Robot
class Robot(ABC):
    def __init__(self, name):
        self.name = name
        self.battery = random.randint(0, 100)  # Simulē baterijas līmeni

    @abstractmethod
    def perform_task(self):
        pass

    def battery_status(self):
        return f"{self.name} baterijas līmenis: {self.battery}%"

#Tīrīšanas robots
class CleaningRobot(Robot):
    def perform_task(self):
        return f"{self.name} tīra telpu ar putekļsūcēju!"

#Apsardzes robots
class SecurityRobot(Robot):
    def perform_task(self):
        return f"{self.name} patrulē teritorijā un skenē apkārtni!"

#Gatavošanas robots
class CookingRobot(Robot):
    def perform_task(self):
        return f"{self.name} gatavo gardu ēdienu!"

#Roboti darbībā
robots = [
    CleaningRobot("RoboCleaner"),
    SecurityRobot("Sargs"),
    CookingRobot("PavārsBot")
]

#Izvadam katra robota statusu un uzdevumu
for robot in robots:
    print(robot.battery_status())
    print(robot.perform_task())
    print("-" * 30)