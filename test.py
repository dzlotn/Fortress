# import logging

# if not logging.getLogger().hasHandlers():
#         logging.basicConfig(filename='lasjldkfjlksja.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
      
# def logInfo(action, option, level):
#     levelDic = {10: "debug", 20: "info",30:"warning",40:"error", 50:"critical"}
#     funcName = levelDic.get(level)
#     if funcName:
#         logging_function = getattr(logging, funcName)
#         logging_function(f"Action: ({action}) for option: ({option})")
#     else:
#         print("\033[31mERROR 202\033[0m: INVALID LOG LEVEL")
    
# logInfo("Added Password",2,40)
    
# logInfo("Fix Deforestation",4,50)

def checkCommonWords(pwd):
    commonWords = open("passwordGeneration/data/commonword.txt","r").read()
    wordsSplit = commonWords.split("\n")
    
    if pwd in wordsSplit:
        print("True")
        
checkCommonWords("peng")