import java.util.Scanner;
import java.util.ArrayList;

public class Pyramid {
    static String pyramidGenerator(int currentRow, int maxRows, String myChar) {
        int spacesCount = maxRows - currentRow;
        int symbolsCount = 2 * currentRow - 1;

        String spaces = " ".repeat(spacesCount);
        String symbols = myChar.repeat(symbolsCount);

        return spaces + symbols + spaces;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your desired character: ");
        String myChar = scanner.nextLine();

        System.out.print("Enter the number of rows: ");
        int rowNumber = scanner.nextInt();
        scanner.nextLine(); // Prevents input skipping

        System.out.print("Normal or Inverted? ");
        String padOrientation = scanner.nextLine();

        ArrayList<String> padRows = new ArrayList<String>();

        String lowerCasetext = padOrientation.toLowerCase();

        if (lowerCasetext.equals("normal")) {
            for (int row = 1; row <= rowNumber; row++) {
                String pyramidRow = pyramidGenerator(row, rowNumber, myChar);
                padRows.add(pyramidRow);
            }
        }

        else {
            for (int row = rowNumber; row > 0; row--) {
                String pyramidRow = pyramidGenerator(row, rowNumber, myChar);
                padRows.add(pyramidRow);
            }
        }
        
        String pyramidOutput = "";

        for (String row : padRows) {
            pyramidOutput += "\n" + row;
        }

        System.out.println(pyramidOutput);
    }
}
