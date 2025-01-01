class auto :
    def __init__(self, name, brand, model=1):
        self.name = name
        self.brand = brand
        self.model = model
        self.car_status = "Off"
    
    def encender(self):
        if self.car_status == "Off":
            self.car_status = "On"
            return f"{self.name} {self.brand} {self.model} se ha encendido"
        else:
            return f"{self.name} {self.brand} {self.model} ya encendido"
        
    def apagar(self):
        if self.car_status == "On":
            self.car_status = "Off"
            return f"{self.name} {self.brand} {self.model} se ha apagado"
        else:
            return f"{self.name} {self.brand} {self.model} ya apagado"
        
cybertruck = auto("Cybertruck", "Tesla", 2024)

print(f"name: {cybertruck.name}, brand: {cybertruck.brand}, model: {cybertruck.model}, status: {cybertruck.car_status}.")
print(cybertruck.encender())
print(f"name: {cybertruck.name}, brand: {cybertruck.brand}, model: {cybertruck.model}, status: {cybertruck.car_status}.")
print(cybertruck.apagar())
print(f"name: {cybertruck.name}, brand: {cybertruck.brand}, model: {cybertruck.model}, status: {cybertruck.car_status}.")