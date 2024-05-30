public class Maths {
    public static void main(String[] args) {
        // Some common math methods of java
        int num1 = 10;
        int num2 = 339;

        System.out.println(Math.max(num1, num2)); // returns maximum value between the two

        /*
         * Math.sqrt()
         * Math.abs() returns the absolute value of a number
         * Math.random returns a random number between 0.0 inclusive and 1.0 exclusive
         */

         int randomNum = (int) (Math.random() * 101); // 0 to 100
         System.out.println(randomNum);
    }
}