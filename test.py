# # # # # import logging

# # # # # if not logging.getLogger().hasHandlers():
# # # # #         logging.basicConfig(filename='lasjldkfjlksja.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
      
# # # # # def logInfo(action, option, level):
# # # # #     levelDic = {10: "debug", 20: "info",30:"warning",40:"error", 50:"critical"}
# # # # #     funcName = levelDic.get(level)
# # # # #     if funcName:
# # # # #         logging_function = getattr(logging, funcName)
# # # #         logging_function(f"Action: ({action}) for option: ({option})")
# # # # #     else:
# # # # #         print("\033[31mERROR 202\033[0m: INVALID LOG LEVEL")
    
# # # # # logInfo("Added Password",2,40)
    
# # # # # logInfo("Fix Deforestation",4,50)

# # # # def checkCommonWords(pwd):
# # # #     commonWords = open("passwordGeneration/data/commonword.txt","r").read()
# # # #     wordsSplit = commonWords.split("\n")
    
# # # #     if pwd in wordsSplit:
# # # #         print("True")
        
# # # # checkCommonWords("peng")
# # # import math
# # # def calculatePasswordEntropy(pwd):
# # #     charamt = 0
# # #     charPrices = [26,26,9]
# # #     charCheck = [False,False,False]
# # #     for i in pwd:
# # #         if i.islower():
# # #             charCheck[0] = True
# # #         elif i.isupper():
# # #             charCheck[1] = True
# # #         elif i.isdigit():
# # #             charCheck[2] = True
# # #     for a in range(3):
# # #         if charCheck[a]:
# # #             charamt+=charPrices[a]        
# # #     entropy = math.log2(charamt)*len(pwd)
# # #     return entropy

# # # print(calculatePasswordEntropy("proseCutter"))

# # list = ["password1","alksjdflk","alksjkdflkjlkaj2i2"]
# # password = "password12"
# # for i in list:
# #     if i in password:
# #         print("yes")


# import time
# from rich import print
# print("[italic red]Hello[/italic red] World!", locals())

# # for i in p(range(20), description="Processing..."):
from rich import pretty
pretty.install()
["Rich and pretty", True]
# #     time.sleep(1)  # Simulate work being done