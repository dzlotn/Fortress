# Compiles and runs the Java file and returns the password data results

import subprocess

def javaProgram(pwd):
    compile_command = ["javac", "scoringPWD.java"]
    subprocess.run(compile_command, check=True)

    # Define the command to run the Java program and passes pwd as an argument
    run_command = ["java", "ScoringPWD", pwd]
    
    subprocess.run(run_command, check=True)
    
    # Read the output from the file
    with open("passwordGeneration/data/statisticsPWD.txt") as file:
        for line in file:
            pass
        lf = line
        
    #calculates password data from statisticsPWD.txt
    diC = int(lf[1 : lf.find("U")])
    upC = int(lf[lf.find("U") + 1 : lf.find("L")])
    lcC = int(lf[lf.find("L") + 1 :])
    
    return diC,upC,lcC

