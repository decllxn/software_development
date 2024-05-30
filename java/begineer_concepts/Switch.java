public class Switch {
    public static void main(String[] args) {
        // instead of writing many switch statements
        // use switch statements

        /*
         * Switch = expression is evaluated once
         * break = breaks out of the switcht block
         * default = specifies code to run if there's no match
         * 
         */

         // Example
        int day = 4;
        switch(day) {
            case 1:
               System.out.println("Monday");
               break;
            case 2:
               System.out.println("Tuesday");
               break;
            case 3:
               System.out.println("Wednesday");
               break;
            case 4:
               System.out.println("Thursday");
               break;
            case 5:
               System.out.println("Friday");
               break;
            case 6:
               System.out.println("Sartuday");
               break;
            case 7:
               System.out.println("Sunday");
               break;
        }
    }
}