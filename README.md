## Fortress: A Password Manager Program with Python and Java

## The Project
Fortress is a sophisticated suite designed for generating, analyzing, and securely storing passwords. This suite integrates a Python script for password generation and a Java program for detailed password analysis, ensuring comprehensive management and security of your credentials. The Python script generates passwords with specific security criteria, while the Java program analyzes the generated passwords for character statistics. The program also allows for encrypted password storage with options to update passwords/usernames/programs with new information. 

## Python Features
 * _Prime Number Length_: Generates passwords with lengths that are prime numbers.
 * _Character Checks_: Ensures no two identical or consecutive ASCII characters are next to each other.
 * _Password Validation:_ Checks the password for common words and keyboard proximity.
 * _Password Management_: Allows storing, retrieving, and managing passwords securely.
 * _Clipboard Integration_: Copies passwords to the clipboard for ease of use.
 * _Logging_: Logs various actions and errors for tracking purposes.


## Java Features
 * _Character Statistics_: Analyzes the generated passwords for the number of digits, uppercase letters, and lowercase letters.
 * _File Output_: Appends the analysis results to a text file for further review.

## Getting Started
1. Clone the entire repository and load it on VS Code
2. Make sure Python and Java are on their latest version
3. PIP install and update the following dependencies:
   * Numpy
   * Secrets
   * OS
   * JSON
   * Logging
   * Subprocess
   
4. Run the following command in the terminal (make sure you are on the outermost directory)
  ```sh
  python FORTRESS.py
  ```
5. Follow the prompts to manage your passwords!


## Java Installation

To compile and run the Java program, follow these steps:

1. Ensure you have [Java Development Kit (JDK)](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) installed.
2. Clone the repository:
    ```sh
    git clone https://github.com/your-username/password-strength-statistics.git
    ```
3. Navigate to the project directory:
    ```sh
    cd password-strength-statistics
    ```
4. Compile the Java program:
    ```sh
    javac ScoringPWD.java
    ```
