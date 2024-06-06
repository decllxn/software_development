package Methods.java;

import java.util.Scanner;

public class ParametersandArguments {
    // information passed to a method is known as a parameter
    // Parameters act as variables inside the method

    static void myMethod(String fname) {
        System.out.println(fname + " loves " + "Stacy");
    }

    static void checkAge(int age) {

        // If age is less than 18, print "access denied"
        if (age < 18) {
          System.out.println("Access denied - You are not old enough!");
    
        // If age is greater than, or equal to, 18, print "access granted"
        } else {
          System.out.println("Access granted - You are old enough!");
        }
    
      }    

    // You can have multiple parameters as you like

    public static void main(String[] args) {
        myMethod("Declan");

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your Age: ");
        int myAge = scanner.nextInt();

        checkAge(myAge);
    }
}
