public class Whileloop {
    public static void main (String[] args) {
        /*
         * while = loops through block of code as long as the specified condition is true
         * 
         */

        int i = 0;
        while (i < 5) {
            System.out.println(i);
            i++;
        }

        /*
         * do/while will execute a code once before checking if the condition is true
         * 
         */
        int j = 0;
        do {
            System.out.println(j);
            j++;
        }
        while (i < 5);

        // real life example
        int countdown = 3;

        while (countdown > 0) {
            System.out.println(countdown);
            countdown--;
        }

        System.out.println("Happy New Year!!");
    }
}
