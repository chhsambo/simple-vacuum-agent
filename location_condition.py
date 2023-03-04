import random
from enum import Enum

class LocationCondition(Enum):
    Clean = 0
    Dirty = 1
    Weed = 2

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def random():
        return LocationCondition(random.randint(0, 1))
    
#v = LocationCondition.random()
#print(v)
