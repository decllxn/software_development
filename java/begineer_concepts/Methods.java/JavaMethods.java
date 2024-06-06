package Methods.java;

public class JavaMethods {
    // A method is a block of code that runs only when it
    // is called.

    // You can pass data known as parameters into a method
    // Also known as functions
    // Methods go inside the main class
    static void myMethod() {
        // myMethod = name of method
        // static  = means method belongs to the main class
                     // and not an objest of the main since the whole of java is inside a class
        // void means it does not have a return valu
        System.out.println("I just got executed!");
    }
    public static void main(String[] args) {
        myMethod();
    }
}
