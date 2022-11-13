class Prime(object):
    
    def __init__(self,num:int):
        """Prime Class Constructor. 

        Args:
            num (int): The num whic will check.
        """
        self.num = num #The num whic will check.
        self.result : bool #The instance variable $result uses for checking count num.
        self.count: int = 0 #The instance variable $count uses for counting number of divisiors for self.num
        self.check_prime() 
        print(self.return_check())
        
    def check_prime(self):
        """The method counts number of divisiors.
        """
        for num in range(2,self.num+1):
            if self.num % num == 0:
                self.count += 1
    
    def return_check(self):
        """The method checks $self.count value. If the value is less then 2 (self.count < 2) returns True for $self.result.
        Else, returns False for $self.result.
        
        Returns:
            _true_: The Num: {self.num} is not prime.
            _false_: "The Num: {self.num} is prime."
        """
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

#HasanBarisGOK @ linkedin: linkedin/in/hasanbarisgok
