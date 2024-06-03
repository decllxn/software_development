public class Breakandcontinue {
    public static void main (String[] args) {
        //Break helps you jump out of a loop
        // the code below will break when x = 4
        for (int i = 0; i < 10; i++) {
            if (i == 4) {
                break;
            }
            System.out.println(i);
        }

        // continue breaks one iteration in the loop when a condition occurs
        // and continues to the next

        for (int i = 0; i < 10; i++) {
            if (i == 4) {
                continue;
            }
            System.out.println(i);
        }
    }
}