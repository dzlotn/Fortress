
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class ScoringPWD {

    public static characterCounts findStatistics(String password) {
        characterCounts counts = new characterCounts();

        for (int i = 0; i < password.length(); i++) {
            char ch = password.charAt(i);

            if (Character.isDigit(ch)) {
                counts.DIGITS++;
            }
            if (Character.isAlphabetic(ch)) {
                if (Character.isUpperCase(ch)) {
                    counts.UC++;
                } else if (Character.isLowerCase(ch)) {
                    counts.LC++;
                }
            }
        }
        return counts;
    }

    static class characterCounts {
        int DIGITS = 0;
        int UC = 0;
        int LC = 0;
    }

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: java ScoringPWD <password>");
            return;
        }

        String password = args[0];
        characterCounts counts = findStatistics(password);
        String output = "D" + counts.DIGITS +
                "U" + counts.UC +
                "L" + counts.LC;

        // Append the output to a new line in a text file
        try (BufferedWriter writer = new BufferedWriter(
                new FileWriter("passwordGeneration/data/statisticsPWD.txt", true))) {
            writer.write(output);
            writer.newLine(); // Add a new line
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
