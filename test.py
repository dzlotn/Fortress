
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
            
            
        
    
pwdCheckKeyboard("qndoasd")