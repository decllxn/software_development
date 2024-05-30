public class Operators {
    public static void main (String[] args) {
        // operators
        /*
         * Arithmetic
         * Assignment
         * Comparison
         * Logical
         * Bitwise
         */

         // Assignment operators 
         /*
          * x = 5 (Assigns 5 to x)   
        */
        int x = 35;
        System.out.println(x);

        // x += 3 (Assigns  x as the new value ot current value plus 3)
        x += 3;
        System.out.println(x);
        // value of x now is 38

        // x-= 8
        // x = x - 8

        x -= 8;
        System.out.println(x);
        // others 
        /*
         * *=
         * /=
         * %=
         */

        x &= 3;
        System.out.println(x);
        // & is a bitwise operator
        // Converts number to binary and checks the results like a truth table
        int a = 5; // Binary: 0101
        int b = 3; // Binary: 0011

        System.out.println(a & b); // Equivalent to: a = a & b
        // Another bitwise operator |
        // Bitwise assignmet operator |*
        // ^ XOR operator, returns true if and only if one operator is true

    }
}