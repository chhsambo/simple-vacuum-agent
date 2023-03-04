import random
from enum import Enum

class VacuumLocation(Enum):
    A = 0
    B = 1

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def random():
        return VacuumLocation(random.randint(0, 1))
    
# v = VacuumLocation.random()
# print(v)