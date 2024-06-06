package Methods.java;
import java.util.Scanner;

public class JavaRecursion {
    // recursion is the techniques of making a function call itself
    // Example, using recursion to add a range of numbers

    static int sum(int k) {
        if (k > 0) {
            return k + sum(k - 1); // function calling itself
        }

        else {
            return 0;
        }
        // Above recursion stack explained

        // 10 + sum(9)
        // 10 + (9 + sum(8))
        // 10 + (9 + (8 + sum(7)))
        // 10 + (9 + (8 + (7 + sum(6))))
    }

    // HALTING CONDITION

    // recursions are loop like 
    // hence you can have a a problem of infinite recursion
    // A halting condition or base case is required
    // used to stop the loop
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your Number: ");
        int x = scanner.nextInt();

        int result = sum(x);
        System.out.println(result);
    }
}
