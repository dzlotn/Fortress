#returns a password with a random prime number length between 0 and 100. Conducts divisibility tests on random numbers
# until prime is found. Password checks if there are two of the same characters next to it and generates a new pwd if so.
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
        if pwdCheck(pwd,num):
            break
        
            
    pwdf = "".join(pwd)
    print(f'\nFinal Password Generated: {pwdf}')

def pwdCheck(pwd,num):
    pwdJoined = "".join(pwd)
    print(f"\nChecking Password for Duplicates: {pwdJoined}")
    for i in range(0,num-1):
        if pwd[i]== pwd[i+1]:
            print(f"Duplicate Char Found: {pwd[i]}\nPassword Status: FAILED\nGenerating New Password...")
            return False
        
        
    print("Password Status: APPROVED")
    return True 

len = rdmt1()
rdmt2(len)
