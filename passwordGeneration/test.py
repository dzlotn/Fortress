# # # import random
# import subprocess
# # # import matplotlib.pyplot as plt

# # # amt = 50
# # # amt_history = [amt]

# # # hit = False
# # # while not hit:
# # #     rand = random.choice([0.33,0.5,0.5, 0.5, 0.5, 0.5,0.5,1, 1, 1,1.5, 1.5, 2, 2, 2,2,5]) 
# # #     amt *= rand
# # #     amt_history.append(amt)

# # #     print(f"Round Number: {len(amt_history)}. Current amt = {amt_history[-1]}")
# # #     if amt >= 100000:
# # #         print(f"Game won in {len(amt_history)} rounds")
# # #         hit = True
# # #     if amt ==0:
# # #         print("Failure")
# # #         break

# # # plt.plot(range(len(amt_history)), amt_history)
# # # plt.xlabel('Number of Rounds')
# # # plt.ylabel('Amount')
# # # plt.title('Amount over Time')
# # # plt.grid(True)
# # # plt.show()

# # code = "Here is a code that you should definitely make notes of "
# print("".join([chr(ord(i) + 1) for i in code]))

# # print("".join([chr(ord(i) - 1) for i in code]))

# # def copyToClipboard(txt):
# #     cmd='echo '+txt.strip()+'|clip'
# #     return subprocess.check_call(cmd, shell=True)
# # copyToClipboard("and then there were none")
def checkStrength(pwd):
    score,diC,upC,lcC=0,0,0,0
    threshold = int(len(pwd)/3)
    pwdList = list(pwd)
    for i in pwdList:
        if i.isdigit():
            diC +=1
        if i.isupper():
            upC +=1
        if i.islower():
            lcC +=1 
    differences = (abs(threshold -diC), abs(threshold-upC), abs(threshold-lcC))
    totalSub = sum(differences)
    print(f"diC: {diC/len(pwd)*100}%") 
    print(f"upC: {upC/len(pwd)*100}%") 
    print(f"dwC: {lcC/len(pwd)*100}%") 
    
    score = max(0, 100 - totalSub * 100 / (2 * threshold))
    print(score)

    return score
    
print(checkStrength("aaBB11"))





    
