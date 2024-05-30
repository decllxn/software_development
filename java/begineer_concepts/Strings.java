public class Strings {
    public static void main (String[] args ){
        // String is a collection of characters
        // Surrounded bye double quotes

        String greeting = "Hello";
        System.out.println(greeting);

        // The .length helps you find the length of the string
        String txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        System.out.println("The length of the txt string is: " + txt.length());
        // More string methods
        /*
         * .toUpperCase() converts lower case text to upper case
         * .toLowerCase() converts to lower
         * .indexOf() locates first occurence of it
         */

        // String Concatenation
        String firstName = "John";
        String lastName = "Doe";
        System.out.println(firstName + " " + lastName);
        //.concat() joins two strings

        System.out.println(firstName.concat(lastName));
    }
}