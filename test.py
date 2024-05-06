# # # # # # # # # import logging

# # # # # # # # # if not logging.getLogger().hasHandlers():
# # # # # # # # #         logging.basicConfig(filename='lasjldkfjlksja.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
      
# # # # # # # # # def logInfo(action, option, level):
# # # # # # # # #     levelDic = {10: "debug", 20: "info",30:"warning",40:"error", 50:"critical"}
# # # # # # # # #     funcName = levelDic.get(level)
# # # # # # # # #     if funcName:
# # # # # # # # #         logging_function = getattr(logging, funcName)
# # # # # # # #         logging_function(f"Action: ({action}) for option: ({option})")
# # # # # # # # #     else:
# # # # # # # # #         print("\033[31mERROR 202\033[0m: INVALID LOG LEVEL")
    
# # # # # # # # # logInfo("Added Password",2,40)
    
# # # # # # # # # logInfo("Fix Deforestation",4,50)

# # # # # # # # def checkCommonWords(pwd):
# # # # # # # #     commonWords = open("passwordGeneration/data/commonword.txt","r").read()
# # # # # # # #     wordsSplit = commonWords.split("\n")
    
# # # # # # # #     if pwd in wordsSplit:
# # # # # # # #         print("True")
        
# # # # # # # # checkCommonWords("peng")
# # # # # # # import math
# # # # # # # def calculatePasswordEntropy(pwd):
# # # # # # #     charamt = 0
# # # # # # #     charPrices = [26,26,9]
# # # # # # #     charCheck = [False,False,False]
# # # # # # #     for i in pwd:
# # # # # # #         if i.islower():
# # # # # # #             charCheck[0] = True
# # # # # # #         elif i.isupper():
# # # # # # #             charCheck[1] = True
# # # # # # #         elif i.isdigit():
# # # # # # #             charCheck[2] = True
# # # # # # #     for a in range(3):
# # # # # # #         if charCheck[a]:
# # # # # # #             charamt+=charPrices[a]        
# # # # # # #     entropy = math.log2(charamt)*len(pwd)
# # # # # # #     return entropy

# # # # # # # print(calculatePasswordEntropy("proseCutter"))

# # # # # # list = ["password1","alksjdflk","alksjkdflkjlkaj2i2"]
# # # # # # password = "password12"
# # # # # # for i in list:
# # # # # #     if i in password:
# # # # # #         print("yes")


# # # # # import time
# # # # # from rich import print
# # # # # print("[italic red]Hello[/italic red] World!", locals())

# # # # # # for i in p(range(20), description="Processing..."):
# # # # from rich import pretty
# # # # pretty.install()
# # # # ["Rich and pretty", True]
# # # # # #     time.sleep(1)  # Simulate work being done 


# # # #creates the dictionary into a list of dictionaries and then order the dictionaries based on their keys
# # # testDict = {"b":1,"a":2,"d":3,"c":4}
# # # print(testDict.items())
# # # list=[]
# # # for key,value in testDict.items():
# # #     list.append((key,value))
# # # print(dict(sorted(list)))
    
# # # import sys

# # # if args == "baby":
# # #     print("hello")

# # import sys
# # import time
# # args = sys.argv[1:] 

# # def print_slow(str):
# #     for letter in str:
# #         sys.stdout.write(letter)
# #         sys.stdout.flush()
# #         time.sleep(0.01)
# #     print(sys.getsizeof(args))

# # print_slow("Type whatever you want here")
# # # # keys = sorted.keys()
# # # # print(keys)

# # import numpy as np
# # import math
# # import matplotlib.pyplot as plt 
# # from numpy.polynomial import Polynomial 
# # def f(x):
# #     try:
# #         return round(abs(np.sqrt(x+ 0.3 * np.log(x+0.01)) -0.308),2) 
# #     except RuntimeWarning: 
# #         pass

# # def s(x):
# #     if x==150:
# #         return 10
# #     return round((f(x)-2.96)*(125/113),5)

# # print(f"Min: {f(10)} Max: {f(150)}")
# # print(f"Min: {s(10)} Max: {s(150)}")
# # with open("passwordGeneration/data/commonWords.txt") as file:
# #     lista = [str(x) for x in file]
# # print(len("Penguins1352"))
# # l = {}
# # count={}
# # for i in range(0,1000):
# #     l[i] = s(i)
    
# # print(l)# for i in range(len(l)-1):
# #     if l[i+1] == l[i]:
# #         count[l[i]]+=1
# #         print(f"Count of {l[i]}: {count}")

# # np.linspace(0,150,10)
# # plt.plot(l.keys(), l.values())
# # plt.show()

# import subprocess

# # Compile the Java file
# compile_command = ["javac", "passwordGeneration/JAVA/ScoringPWD.java"]
# subprocess.run(compile_command, check=True)
# pwd = input("Enter a password: ")
# # Define the command to run the Java program
# run_command = ["java", "ScoringPWD", pwd]
# subprocess.run(run_command, check=True)

# # Read the output from the file
# with open("passwordGeneration/data/statisticsPWD.txt") as file:
#     for line in file:
#         pass
#     lf = line
# print(lf)


