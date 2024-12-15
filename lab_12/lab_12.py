
class Rationum:    
    
    num = None  
    den = None
    
    def __init__(self, num, den):
        self.num = num
        self.den = den
    
    def add(self, r1, r2 = None):
        if r2 is None:
            r2 = Rationum(self.num, self.den)
        self.num = r1.den * r2.num + r1.num * r2.den        
        self.den = r1.den * r2.den
    
    def mult(self, r1, r2=None):
        if r2 is None:
            r2 = Rationum(self.num, self.den)
        self.num = r1.num * r2.num       
        self.den *= r1.den * r2.den
    
    def printme(self):
        print(f"{self.num}/{self.den}")
    
   
def main():
    rn1 = Rationum(3, 4)
    rn2 = Rationum(1, 4)
    rn3 = Rationum(1, 2)
    rn1.printme()
        rn2.printme()
    rn3.printme()
    rn1.add(rn2, rn3)
    rn1.printme()
    rn1.add(rn2)
    rn1.printme()
    
if __name__=="__main__":
    main()