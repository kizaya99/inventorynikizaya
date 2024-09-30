#KEZIAH MANDADO     FC1 BSIT 2-2    ITE-300
class Calculator:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
    def add(self, num1, num2):
        print("The brand of my calculator is: " + self.brand)
        print("The Color of my calculator is: " + self.color)
        print("The sum is:", + num1 + num2) 
    
    def subtract(self, num1, num2):
        print("The brand of my calculator is: " + self.brand)
        print("The Color of my calculator is: " + self.color)
        print("The difference is:", + num1 - num2)
        
    def Multiply(self, num1, num2):
        print("The brand of my calculator is: " + self.brand)
        print("The Color of my calculator is: " + self.color)
        print("The Multiply is:", + num1 * num2)
     
    def Divide(self, num1, num2):
        print("The brand of my calculator is: " + self.brand)
        print("The Color of my calculator is: " + self.color)
        print("The Divide is:", + num1 // num2)
        
        

my_calc = Calculator("sharp", "Black")
my_calc.add(10, 20)

CalculatorA = Calculator("sharp","pink")
CalculatorA.subtract(10,20)

CalculatorB = Calculator("sharp","purple")
CalculatorB.Multiply(10,20)

CalculatorC = Calculator("sharp","green")
CalculatorC.Divide(10,20)