import subprocess

# Compile the Java file
compile_command = ["javac", "ScoringPWD.java"]
subprocess.run(compile_command, check=True)

# Define the command to run the Java program
run_command = ["java", "ScoringPWD", "lsahdfljalskdjfAAA"]
subprocess.run(run_command, check=True)

# Read the output from the file
with open("passwordGeneration/data/statisticsPWD.txt", "r") as file:
    output = file.read()

