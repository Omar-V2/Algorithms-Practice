class I(): 
    num = 0 
    def __init__(self): 
        self.num = 0 
    def method(self): 
        return 
    def methodA(self): 
        I.num = 0 
    def methodB(self): 
        I.num = I.num + 1 
    def methodC(self): 
        self.num += 1         
    def methodD(cls): 
        I.num = I.num + 1 
    methodD = classmethod(methodD) 
    def methodE(cls): 
        return I.num 
    methodE = classmethod(methodE) 
    def methodF(): 
        return I.num 
    methodF = staticmethod(methodF) 
    def methodG(self): 
        self.num = self.num + 1 
    def methodH(self): 
        self.num = I.num 
        return self.num

I = I()
print(I.methodH())
print(I.methodE())