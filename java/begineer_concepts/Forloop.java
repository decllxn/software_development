public class Forloop {
    // when you know how many times to loop through a code,
    // use for loop instead of while loop
    public static void main (String[] args) {
        /*
         * for (statement1; statement2; statement3){
         * }
         * Statement 1 = executed one time before execution of code block
         * Statement 2 = defines the condition for executing the code block
         * Statement 3 = executed everytime after the code block has been executed
         * 
         */

        for (int i = 0; i < 5; i++) {
            System.out.println(i);
        }
        // nested for loop
        // The "inner loop" will be executed one time for each iteration

        // Outer loop
        for (int i = 1; i <= 2; i++){
            System.out.println("Outer: " + i); // Executes 2 times

            // Inner loops
            for (int j = 1; j <= 3; j++) {
                System.out.println("Inner: " + j);
            }
        }

        // for......each loop
        // Exclusively to loop through an array

        String[] cars = {"Volvo", "BMW", "ford", "Mazda"};
        for (String k : cars) {
            System.out.println(k);
        }

        // Multiplication table of 2
        int number = 2;

        for (int g = 1; g <= 10; g++) {
            System.out.println(number + " x " + g + " = " + (number * g));
        }
    }
}
