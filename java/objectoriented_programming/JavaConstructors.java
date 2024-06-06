public class JavaConstructors {
    // A constructor is a SPECIAL METHOD used to initialize objects
    int x; // create a class attribute

    // Create a CLASS CONSTRUCTOR for the main class
    public JavaConstructors() {
        x = 5; // set the initial value for the class attributr x
    }

    public static void main(String[] args) {
        JavaConstructors myObject = new JavaConstructors(); // Create object of the main class
        System.out.println(myObject.x); //Print the value of x
        // outputs 5
        // Constructor must match the class name
        // It cannot have a return value
    }
}

