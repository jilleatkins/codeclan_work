from classes.vehicle import Vehicle

class Motorbike:
    
    def start_engine(self):
        supers_start_val = super().start_engine()
        print(supers_start_val)
        return "Meow"