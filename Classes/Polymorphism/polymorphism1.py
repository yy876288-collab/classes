class Payment:
    def pay(self):
        print("Processing Payment")
    
class UPI(Payment):
    def pay(self):
        print("Paid using UPI ")

class Cash(Payment):
    def pay(self):
        print("Paid using cash")   

p1=UPI()
p1.pay()

p2=Cash()
p2.pay()

p3=Payment()
p3.pay()
          


    
