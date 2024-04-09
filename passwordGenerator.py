#returns a password with a random prime number length between 0 and 100. Conducts divisibility tests on random numbers
# until prime is found. Password checks if there are two of the same characters next to it and generates a new pwd if so.
#also checks if any two consecutive characters are consecutive in ASCII using the ord command.  As a result, no password can have ex abc
#4/8/24

import random
#finds random prime number for len
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
#creates password using sets of characters and pwd length found by rdmt1                
def rdmt2(num):
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    statusDict = {
        True:"APPROVED",
        False: "FAILED"
    }
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
        if pwdCheckCons(pwd,num,statusDict):
            break
            
    pwdf = "".join(pwd)
    print(f'\nFinal Password Generated: {pwdf}')

#checks for errors in password
def pwdCheckCons(pwd,num,statusDict):
   
    pwdJoined = "".join(pwd)
    print(f"\nChecking Password for Errors: {pwdJoined}")
    for i in range(0,num-1):
        if pwd[i]== pwd[i+1]:
            print(f"Duplicate Char Found: {pwd[i]}\nPassword Status: {statusDict[False]}\nGenerating New Password...")
            return False
        if ord(pwd[i]) +1 == ord(pwd[i+1]) or ord(pwd[i]) -1 == ord(pwd[i+1]):
            print(f"Consecutive Characters in ASCII Found: {pwd[i]} and {pwd[i+1]}\nPassword Status:{statusDict[False]}\nGenerating New Password...")
            return False
    
    
    if pwdCheckKeyboard(pwd,num,statusDict) == False:
        return False
    
    print(f"Password Status: {statusDict[True]}")
    return True 

#checks if consecutive characters in the password are next to eachother on the keyboard
def pwdCheckKeyboard(pwd,num,statusDict):
    pwdString = "".join(pwd)
    keyboardLayout = {
        "r1": "qwertyuiop",
        "r2": "asdfghjkl",
        "r3": "zxcvbnm"
    } 
    for i in range(0,num-1):
        charFst = pwdString[i]
        charNxt = pwdString[i+1]
        for row in keyboardLayout.values():
            if charFst in row and charNxt in row:
                if abs(row.index(charFst) -row.index(charNxt)) ==1:
                    print(f"Close Characters on Keyboard Found: {charFst} and {charNxt}\nPassword Status: {statusDict[False]}\nGenerating New Password...")
                    return False
            
            
    
len = rdmt1()
rdmt2(len)
