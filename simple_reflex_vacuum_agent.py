from vacuum_location import VacuumLocation
from location_condition import LocationCondition


class Environment():
    def __init__(self):
        self.locationCondition = {}
        self.locationCondition["A"] = LocationCondition.random()
        self.locationCondition["B"] = LocationCondition.random()


class Agent01(Environment):
    def __init__(self, Environment):
        print("========================")
        print("Environment Initialize")
        print(Environment.locationCondition)
        print("========================")
        
        score = 0
        vacuumLocation = VacuumLocation.random()

        if vacuumLocation == VacuumLocation.A:
            print("\nVacuum is randomly placed at Location A.")
            if Environment.locationCondition["A"] == LocationCondition.Dirty:
                print(">> Location A is Dirty.")  
            else: 
                print(">> Location A is Clean.")
            
            if Environment.locationCondition["A"] == LocationCondition.Dirty:
                # Do Cleaning
                print(">> Cleaning Location A.")
                Environment.locationCondition["A"] = LocationCondition.Clean
                score += 1
                print(">> Location A has been Cleaned.")

            print("\nMoving to Location B...")
            if Environment.locationCondition["B"] == LocationCondition.Dirty:
                print(">> Location B is Dirty.") 
            else: 
                print(">> Location B is Clean.")

            if Environment.locationCondition["B"] == LocationCondition.Dirty:
                print(">> Cleaning Location B.")
                Environment.locationCondition["B"] = LocationCondition.Clean
                score += 1
                print(">> Location B has been Cleaned.")

            print("\nEnvironment is Clean.")
                
        elif vacuumLocation == VacuumLocation.B:
            print("\nVacuum randomly placed at Location B.")
            if Environment.locationCondition["B"] == LocationCondition.Dirty:
                print(">> Location B is Dirty.")
            else: 
                print(">> Location B is Clean.")

            if Environment.locationCondition["B"] == LocationCondition.Dirty:
                Environment.locationCondition["B"] = LocationCondition.Clean
                score += 1
                print(">> Location B has been Cleaned.")
            
            print("\nMoving to Location A...")
            if Environment.locationCondition["A"] == LocationCondition.Dirty:
                print(">> Location A is Dirty.")
            else: 
                print(">> Location A is Clean.")
            if Environment.locationCondition["A"] == LocationCondition.Dirty:
                Environment.locationCondition["A"] = LocationCondition.Clean
                score += 1
                print(">> Location A has been Cleaned.")
            
            print("\nEnvironment is Clean.")

        else:
            print("\nVacuum randomly to Unknow Location!")
        
        print("")
        print("========================")
        print(Environment.locationCondition)
        print("Performance Measurement:", score)
        print("========================")


house1 = Environment()
robot01 = Agent01(house1)
