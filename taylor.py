import math
def taylor(x):
    result = 1
    i = 1
    while math.pow(x, i)/math.factorial(i) >= math.e:
        result += math.pow(x, i)/math.factorial(i)
        i+=1
    return result
    
for i in range(11):
    print("Taylor(",i,")"," = ",taylor(i),", e^",i," = ", math.exp(i), sep="")
