#OOP OF PYTHON.
#class 
#constractor
#attributes
#objects



#class
class Human:
    #contractor 
    def __init__(self, name, money): #init is short for initiate
        self.name = name
        self.money = money
        
        #methods
    def speak(self):
        print("my name is", self.name)
        print('i have', self.money)
        
        
        
        
    def work(self, salary, kupit):
        self.money += salary - kupit
        print(self.name, "has earned", salary)
            
        
    
    
    
#object
h1 = Human("chow", 100000)
h1.speak()
h1.work(500, 2345)
h1.speak()
