#A simple calculator function that takes two numbers and an operation as parameters
#The calculator then conducts the operation on the two numbers and returns the result

def calcfunc(num1, op, num2):
    #multiplaction func
    if op == "*":
        return num1*num2
    #add func
    elif op == "+":
        return num1+num2
    #sub func
    elif op=="-":
        return num1-num2
    #division func
    elif op == "/":
        return float(num1/num2)
    
#test cases
print(calcfunc(2,"*",5))
print(calcfunc(3,"/",7))
print(calcfunc(176,"-",53))
print(calcfunc(2,"*",5))



