import subprocess

# Compile the Java file
compile_command = ["javac", "ScoringPWD.java"]
subprocess.run(compile_command, check=True)
pwd = input("Enter a password: ")
# Define the command to run the Java program
run_command = ["java", "ScoringPWD", pwd]
subprocess.run(run_command, check=True)

# Read the output from the file
with open("passwordGeneration/data/statisticsPWD.txt") as file:
    for line in file:
        pass
    lf = line
print(lf)

