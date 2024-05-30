public class Conditionals {
    public static void main (String[] args) {
        // Comditional statements such as if loops
        if (20 > 18) {
            System.out.println("20 is greater than 18");
        }
    // Introduction of else to specify a block of code to be executes if conditions is false 
        int time = 20;
        if (time < 18) {
            System.out.println("Good day.");
        }
        else {
            System.out.println("Good Evening");
        }
        // else if condition statement to specify a new condition if the first condition is false

        int num = 22;
        if (num < 10) {
            System.out.println("Good morning");
        }
        else if (num < 18) {
            System.out.println("Good day.");
        }
        else {
            System.out.println("Good Evening;");
        }

        // short hand if...else
        // variable = (condition) ? expressioniftrue : expressioniffalse

        // example
        int number = 20;
        if (number < 18) {
            System.out.println("Good day.");
        }
        else {
            System.out.println("Good evening");
        }

        // can also be written as 
        int number2 = 20;
        String result = (number2 < 18) ? "Good day" : "Good evening";
        System.out.println(result);
    }
}