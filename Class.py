class laptops:
    def __init__(self):
        self.price=0
        self.ram=""
        self.processor=""
    def display(self):
        print("Price: ",self.price)
        print("Processor: ",self.processor)
hp=laptops()
hp.price=10000
hp.processor="i5"
dell=laptops()
dell.price=25000
dell.processor="i7"
# print("Price of HP laptop is: ",hp.price)
# print("The dell processor is:",dell.processor)
hp.display()
dell.display()