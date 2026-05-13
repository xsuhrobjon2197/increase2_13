#2-m
class Phone:
    factory = "China"
    charger_type = "Type-C"
    
    def __init__(self, brand, model, memory, price):
        self.brand = brand
        self.model = model
        self.memory = memory
        self.price = price
        
    def show_phone(self):
        print(f"Yangi Narx: {self.price}")
        
    def change(self, new_price):
        print(f"{self.brand} telefoni object yarating:")
        
    def upgrade_memory(self, new_memory):
        print(f"{self.price} va {self.memory} o'zgartirib chiqaring:")
        
c1 = Phone("iphone", "Iphone11", "256gb", "11million")
c1.show_phone()
c1.change("12million")
c1.upgrade_memory("512gb")
