#returns a password with a random prime number length between 0 and 100. Conducts divisibility tests on random numbers
# until prime is found. Password checks if there are two of the same characters next to it and generates a new pwd if so.
#also checks if any two consecutive characters are consecutive in ASCII using the ord command.  As a result, no password can have ex abc
#4/8/24

import random
import secrets
import json
import os 
#finds random prime number for len
def newprintLn():
    print("\n----------------------\n")
    
def rdmt1():
    check = True
    while True:
        num = random.randint(10,100)
        print(f'\n\033[34mTrying Number: {num}\033[0m')
        for j in range(2,num//2+1):
            if num%j == 0:
                print(f"\033[31mNumber fails divisibility test of {j}\033[0m")
                check=False
                break
        if check:
            print(f"\033[32mPrime Number Found: {num}\033[33m")
            print(f"Generating Password of length {num}...\033[0m")
            newprintLn()
            return num
        else:
            check=True
#creates password using sets of characters and pwd length found by rdmt1                
def rdmt2(num):
    #global variables
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    statusDict = {
        True:"\033[32mAPPROVED\033[0m",
        False: "\033[31mFAILED\033[0m"
    }
    while True:
        pwd = []  
        prev_type = None
        consecutive_count=0
        for i in range(num):
            while True:
                case = secrets.randbelow(3)
                if  case == 0 and (prev_type != 0 or consecutive_count < 3):  # Check if the previous character was not a number or consecutive count is less than 3
                    pwd.append(numbers[random.randint(0, 9)])
                    prev_type = 0
                    consecutive_count = 0 if prev_type != 0 else consecutive_count + 1
                    break
                elif case == 1 and (prev_type != 1 or consecutive_count < 3):  # Check if the previous character was not a lowercase letter or consecutive count is less than 3
                    pwd.append(letters[random.randint(0, 25)])
                    prev_type = 1
                    consecutive_count = 0 if prev_type != 1 else consecutive_count + 1
                    break
                elif case == 2 and (prev_type != 2 or consecutive_count < 3):  # Check if the previous character was not an uppercase letter or consecutive count is less than 3
                    pwd.append(letters[random.randint(0, 25)].upper())
                    prev_type = 2
                    consecutive_count = 0 if prev_type != 2 else consecutive_count + 1
                    break
                
        if pwdCheckCons(pwd,num,statusDict):
            break
            
    pwdf = "".join(pwd)
    
    ans = input(f"\nComputer has created a secure password. Would you like to use: \"{pwdf}\" as one of your passwords? (yes or no)\n").upper()
    if ans == "YES":
        # passwordlist.append(pwdf)
        # print(f'\n-------------\nFinal Password Generated:')
        # print(f"\033[32m{pwdf}\033[0m")
        pwdAppend1(pwdf)
    elif ans=="NO":
        rdmt2(rdmt1())
    
    else:
        print("Invalid Response. \033[033m Generating new password... \033[0m")
        rdmt2(rdmt1())   
               
    return pwdf

def pwdAppend1(pwdf):
    prog = input("\nWhat program would you like to assign the password to? " )
    passwordManager[prog] = pwdf
    print(f"\033[32mPassword({pwdf}) added to password manager under program ({prog})\033[0m")
    
def pwdAppend2():
    prog = input("\nWhat program would you like to assign the password to? " )
    pwd = input("Type in the password to be added: ")
    passwordManager[prog] = pwd
    print(f"\033[32mPassword({pwd}) added to password manager under program ({prog})\033[0m")

    
    
#checks for errors in password
def pwdCheckCons(pwd,num,statusDict): 
   
    pwdJoined = "".join(pwd)
    print(f"\nChecking Password for Errors: {pwdJoined}")
    for i in range(0,num-1):
        if pwd[i]== pwd[i+1]:
            print(f"\033[31mDuplicate Char Found: {pwd[i]}\n\033[0mPassword Status: {statusDict[False]}\033[33m\nGenerating New Password...\033[0m")
            return False
        if ord(pwd[i]) +1 == ord(pwd[i+1]) or ord(pwd[i]) -1 == ord(pwd[i+1]):
            print(f"\033[31mConsecutive Characters in ASCII Found: {pwd[i]} and {pwd[i+1]}\n\033[0mPassword Status:{statusDict[False]}\033[33m\nGenerating New Password...\033[0m")
            return False
    
    if pwdCheckKeyboardRows(pwd,num,statusDict) == False:
        return False
    
    print(f"Password Status: {statusDict[True]}")
    return True 

#checks if consecutive characters in the password are next to eachother on the keyboard
def pwdCheckKeyboardRows(pwd,num,statusDict):
    pwdString = "".join(pwd)
    keyboardLayoutRow = {
        "r1": "qwertyuiop",
        "r2": "asdfghjkl",
        "r3": "zxcvbnm"
        
    } 
    keyboardLayoutCol = {
        "1":"1qaz",
        "2":"2wsx",
        "3":"3edc",
        "4":"4rfv",
        "5":"5tgb",
        "6":"6yhn",
        "7":"7ujm",
        "8":"8ik",
        "9":"9ol",
        "0":"0p"
    }
    
    for i in range(0,num-1):
        charFst = pwdString[i]
        charNxt = pwdString[i+1]
        for row in keyboardLayoutRow.values():
            if charFst in row and charNxt in row:
                if abs(row.index(charFst) -row.index(charNxt)) ==1:
                    print(f"\033[31mClose Characters on Keyboard Found (row wise): {charFst} and {charNxt}\n\033[0mPassword Status: {statusDict[False]}\033[33m\nGenerating New Password...\033[0m")
                    return False
    for i in range(0,num-1):
        charFst = pwdString[i]
        charNxt = pwdString[i+1]
        for row in keyboardLayoutCol.values():
            if charFst in row and charNxt in row:
                if abs(row.index(charFst)- row.index(charNxt))==1:
                    print(f"\033[31mClose Characters on Keyboard Found (column wise): {charFst} and {charNxt}\n\033[0mPassword Status: {statusDict[False]}\033[33m\nGenerating New Password...\033[0m")
                    return False 
            
 
#prints passwords in nice table format           
def printPasswords(passwordManager):
    print("\033[34m  {:<20}   {:<20}\033[0m".format("Program", "Password"))
    for program, password in passwordManager.items():
        print("  {:<20} | {:<15}".format(program,password))
        
#saves the passwords in a data.json file
def savePasswords(passwordManager):
    with open('data.json','w') as f:
        json.dump(passwordManager,f) 
        
if __name__ == "__main__":
    if os.path.exists("data.json"):
        with open("data.json", "r") as p:
            passwordManager = json.load(p)
            
    else:
        passwordManager = {}
    while True:
        options = input("\nWhat would you like to do? Type the number command. \n 1: Allow computer to create secure password \n 2: Store username and password \n 3: Delete an existing password from the manager \n 4: Change a password \n 5: Print all passwords \n 6: Delete Password File (PERMANNENT) \n 7: End Program\n Choice: ")
        newprintLn()
        
        #lets computer create new password
        if options =="1":
            rdmt2(rdmt1())
            savePasswords(passwordManager)
        
        #adds new password to manager  
        elif options == "2":
            pwdAppend2()
            
        #runs delete password code
        elif options == "3":
            print("Here are the current passwords in the password manager: \n")
            printPasswords(passwordManager)
            deletedSet = input("Which password would you like to delete. Type in the program that the password refers to: ") 
            if deletedSet in passwordManager: 
                del passwordManager[deletedSet]
                print(f"\033[31mPassword Deleted \033[0m")
                savePasswords(passwordManager)

            else:
                print(f"\033[31m\nPassword not found under written program\033[0m")
        
        #allows for password reasignment     
        elif options =="4":
            print("\nHere are the current passwords in the password manager: ")
            printPasswords(passwordManager)
            reasignedSet = input("Which password would you like to Update. Type in the program that the password refers to: ")  
            if reasignedSet in passwordManager: 
                newPwd = input("\nType in the new password: ")
                passwordManager[reasignedSet] = newPwd
                print(f"\033[33mPassword Update \033[0m")
                savePasswords(passwordManager)


            else:
                print(f"\033[31mPassword not found under written program\033[0m")
             
        elif options=="5":
            print("\nHere are the current passwords in the password manager: ")
            printPasswords(passwordManager)
        
        #deletes password file
        elif options =="6":
            check = input("Are you want to delete the password file. This is a permament action! (YES or NO)\n").upper()
            if check == "YES":
                print(f"\033[31mPassword Data Removed\033[0m")
                passwordManager = {}
                os.remove("data.json")
                
        elif options == "7":
            print(f"\033[032mCode Completion - Passwords added to data.json file\033[0m")
            break
        else:
            print("Invalid Command. Please try again")
