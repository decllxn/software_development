public class Typecasting {
    public static void main(String[] args) {
        // Type casting is when you assign one primitive data type to another
        // Widening the cast
        // Converting a smaller type to a larger type size
           /*byte > short > char > int > long > float > double */
        // Narrowing the cast
          /*double > float > long > int > char > short > byte */

        // Example: Widening Casting
        int myInt = 9;
        double myDouble = myInt;
        System.out.println(myInt);
        System.out.println(myDouble);

        // Example: Narrowing Casting
        double myDouble2 = 9.8849d;
        int myInt2 = (int) myDouble2; // I have to manual cast it with (int)
        System.out.println(myDouble2);
        System.out.println(myInt2);

        // Real life example
        // Set the maximu possible score in the game to 500
        
        int maxScore = 500;
        // The actual score 

        int userScore = 423;
        /*Calculate the percentage of the user's score in relation to the 
         * maximum available score
         * Convert userScore to float to make sure that the division is accurate
         */

         float percentage = (float) userScore / maxScore * 100.0f;

         System.out.println("User's percentage is " + percentage);
    }
}