def uppercaseFirstHalf(input_string):
    # Calculate the midpoint of the string
    midpoint = len(input_string) // 2

    # Convert the first half of the string to uppercase
    modified_string = input_string[:midpoint].upper() + input_string[midpoint:]

    return modified_string

def bionicSentence(inputsentence):
    modifiedSentence = ""
    #Splits the sentence into indivudal words that can then be modified
    tokens = inputsentence.split(" ")
    #Iterates through the token list and applies the uppercaseFirstHalf function to each word,
    # appending them to a modified sentence variable
    for i in range(len(tokens)):
        modifiedSentence = modifiedSentence+uppercaseFirstHalf(tokens[i]) + " "
    return modifiedSentence

##TEST CASES
inputsent = input("Enter a sentence ")
print("Your modified sentence is: ", bionicSentence(inputsent))