public class Variables {
    public static void main(String[] args) {
        int age = 25;
        System.out.println(age);

        // Float variable
        float salary = 10.57f; // required f at the end to denote it's a float
        System.out.println(salary);

        // Double variable
        double salary2 = 3005.7;
        System.out.println(salary2);

        // String Variables
        String firstName = "Stacy";
        String lastName = "June";
        String fullName = firstName + lastName;
        System.out.println(fullName);

        // many Integer variables
        int x = 5, y = 6, z = 7;
        System.out.println(x + y + z);

        // char data type
        // declaring it with a variable must have single quotes

        char startingLetter = 'C';
        System.out.println(startingLetter);

        // Real life Example

        // Student data 
        String studentName = "John Doe";
        int studentID = 15;
        int studentAge  = 23;
        float studentFee = 75.25f;
        double studentLoan = 56.34;
        char studentGrade = 'D';

        // Printing the variables 
        System.out.println("Student name: " + studentName);
        System.out.println("Student name: " + studentName);
        System.out.println("Student id: " + studentID);
        System.out.println("Student age: " + studentAge);
        System.out.println("Student fee: " + studentFee);
        System.out.println("Student loan: " + studentLoan);
        System.out.println("Student grade: " + studentGrade);

        // Data types divided into two groups
        // Primitive data types and non-primitive data types
        // All data types except for strings, arrays and objects are primitive data types

        /*
         * NUMBER DATA TYPE:
         * byte, short, int, long (integer types)
         * float and double (Floating point type)
         */

        // Real life example

// Create variables of different data types
        int items = 50;
        byte items2 = 100;
        float costPerItem = 9.99f;
        double totalCost = items * costPerItem;
        char currency = '$';

// Print variables
        System.out.println("Number of items: " + items);
        System.out.println("Number of another item: " + items2);
        System.out.println("Cost per item: " + costPerItem + currency);
        System.out.println("Total cost = " + totalCost + currency);
    }

    // Non-primitive data types are called reference types
    // THey refer to objects
}