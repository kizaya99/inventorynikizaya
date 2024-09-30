class Calculator:
    #contractor 
    def __init__(self, brand, color): 
        self.brand = brand
        self.color = color
        
        #methods
    def add(self, a, b):
        print(self.brand, self.color, a + b)
        
    def multiply(self, c, d):
        print(self.brand, self.color, c * d)
        
    def divide(self, e, f):
        print(self.brand, self.color, e / f)
        
    def subtract(self, g, h):
        print(self.brand, self.color, g - h)
    
    
    
    
    
calcu = Calculator("sharp", "black")


calcu.add(2, 4)
calcu.multiply(10, 20)
calcu.divide(2, 10)
calcu.subtract(100, 50)
    
    
