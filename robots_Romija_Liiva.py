
from abc import ABC, abstractmethod
import random #Lai ģenerētu nejaušu uzlādes līmeni

class Robot(ABC):
    def __init__(self, vards): #konstruktors
        self.vards = vards
        self.uzlades_lim = random.randint(1, 100)

    @abstractmethod
    def baterijas_limenis(self):
        pass

    @abstractmethod
    def perform_task(self):
        pass

class CleaningRobot(Robot):
    def baterijas_limenis(self):
        print(self.vards, ' baterija līmenis',self.uzlades_lim)

    def perform_task(self):
        print(self.vards, "tīra telpu ar putekļusūcēju!")

class SecurityRobot(Robot):
    def baterijas_limenis(self):
        print(self.vards, ' baterija līmenis',self.uzlades_lim)

    def perform_task(self):
        print(self.vards, "patrulē teritorijā un skenē apkārtni!")

class CookingRobot(Robot):
    def baterijas_limenis(self):
        print(self.vards, ' baterija līmenis',self.uzlades_lim)

    def perform_task(self):
        print(self.vards, "gatavo gardu ēdienu!")

vardi = [CleaningRobot("RoboCleaner"),SecurityRobot("RoboGuard") , CookingRobot("ChefBot")]

for i in vardi:
    print(i.baterijas_limenis())
    print(i.perform_task())
    print('-'*30)



