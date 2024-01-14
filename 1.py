class Calculator:
    def __init__(self,n:int):
        self.n=n
    def plus(self,plus=1):
        self.n+=plus
    def mod(self,mod=1):
        self.n%=mod
    def multiply(self,multiply=2):
        self.n*=multiply
    def minus(self,minus=1):
        self.n-=minus
    def divide(self,divide=1):
        self.n//=divide
    def get_answer(self):
        print(f"N ning qiymati {calc.n}")
calc = Calculator(10)
calc.plus(5)
print(f"N={calc.n}")            
calc.plus()	
print(f"N={calc.n}")          
calc.mod(2)
print(f"N={calc.n}")          
calc.plus() 
print(f"N={calc.n}")           
calc.multiply(100) 
print(f"N={calc.n}")  
calc.multiply() 
print(f"N={calc.n}")    
calc.minus(40) 
print(f"N={calc.n}")      
calc.minus()  
print(f"N={calc.n}")          
calc.get_answer() 
  
