#We'll get a new number, with N value. The new number consists of numbers less than the Value.
#For 3 = 123, For 4 = 1234, etc.
numberValue = 9
b = 1
while b < numberValue+1:
    print(b, end="")
    b += 1

#Solution.long
n = 5
numberinN = []
for a in range(n):
    numberinN.append(a+1)
print(''.join(str(e) for e in numberinN))
    
