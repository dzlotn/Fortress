# Compiles and runs the Java file and returns the password data results

import subprocess

def javaProgram(pwd):
    compile_command = ["javac", "scoringPWD.java"]
    subprocess.run(compile_command, check=True)
    print("compiled")
    # Define the command to run the Java program
    run_command = ["java", "ScoringPWD", pwd]
    
    subprocess.run(run_command, check=True)
    print("ran")
    # Read the output from the file
    with open("passwordGeneration/data/statisticsPWD.txt") as file:
        for line in file:
            pass
        lf = line
    return lf

