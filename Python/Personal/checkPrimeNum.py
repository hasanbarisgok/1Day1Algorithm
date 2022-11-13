class Prime(object):
    
    def __init__(self,num:int):
        self.num = num
        self.result : bool
        self.count: int = 0
        self.check_prime()
        print(self.return_check())
        
    def check_prime(self):
        for num in range(2,self.num+1):
            if self.num % num == 0:
                self.count += 1
    
    def return_check(self):
        if self.count < 2 or self.num == 2:
                self.result = True
        else:
                self.result = False
                
        if self.result == False:
            return f"The Num: {self.num} is not prime."
        else:
            return f"The Num: {self.num} is prime."
        
        
            
for new in range(0,101):
    new = Prime(new)
    print(30*"*")
