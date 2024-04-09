#returns a password with a random prime number length between 0 and 100. Conducts divisibility tests on random numbers
# until prime is found. Password checks if there are two of the same characters next to it and generates a new pwd if so.
#also checks if any two consecutive characters are consecutive in ASCII using the ord command.  As a result, no password can have ex abc
#4/8/24

import random

def rdmt1():
    check = True
    while True:
        num = random.randint(10,100)
        print(f'Trying: {num}')
        for j in range(2,num//2+1):
            if num%j == 0:
                print(f"Number fails divisibility test of {j} \n ----------------------------- \n")
                check=False
                break
        if check:
            print(f"Prime Number Found: {num}")
            return num
        else:
            check=True
                       
def rdmt2(num):
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    while True:
        pwd = []  
        for i in range(num):
            case = random.randint(0,2)
            if case == 0:
                pwd.append(letters[random.randint(0,25)])
            elif case == 1:
                pwd.append(numbers[random.randint(0,9)]) 
            else:
                pwd.append(letters[random.randint(0,25)].upper())
        if pwdCheckCons(pwd,num):
            break
     
        
            
    pwdf = "".join(pwd)
    print(f'\nFinal Password Generated: {pwdf}')

def pwdCheckCons(pwd,num):
    statusDict = {
        True:"APPROVED",
        False: "FAILED"
    }
    pwdJoined = "".join(pwd)
    print(f"\nChecking Password for Duplicates: {pwdJoined}")
    for i in range(0,num-1):
        if pwd[i]== pwd[i+1]:
            print(f"Duplicate Char Found: {pwd[i]}\nPassword Status: {statusDict[False]}\nGenerating New Password...")
            return False
        if ord(pwd[i]) +1 == ord(pwd[i+1]) or ord(pwd[i]) -1 == ord(pwd[i+1]):
            print(f"Consecutive Characters in ASCII Found: {pwd[i]} and {pwd[i+1]}\nPassword Status:{statusDict[False]}\nGenerating New Password...")
            return False
        
    print(f"Password Status: {statusDict[True]}")
    return True 
    
def pwdCheckKeyboard(pwd):
    keyboardLayout = {
        "r1": "qwertyuiop",
        "r2": "asdfghjkl",
        "r3": "zxcvbnm"
    } 
    for i in range(len(pwd)-1):
        charFst = pwd[i]
        charNxt = pwd[i+1]
        for row in keyboardLayout.values():
            if charFst in row and charNxt in row:
                print("yes")
                if abs(row.index(charFst) -row.index(charNxt)) ==1:
                    print(f"keys found next to eachother: {charFst} and {charNxt} ")
            
            
        
    
    

    
len = rdmt1()
rdmt2(len)
