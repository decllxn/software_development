public class ClassMethods {
    // Functions inside classes

    // STATIC VS PUBLIC
    // A static method can be accessed without creating an object of the class
    // A Public method can only be accessed by objects

    // Example
    // Static Method
    static void myStaticMethod() {
        System.out.println("Public methods can be called withoutcreating objects");
    }

    // Public Method
    public void myPublicMethod() {
        System.out.println("Public methods must be called by creating an object");
    }

    // Main method
    public static void main(String[] args) {
        myStaticMethod(); // Call the static method
        // myPublicMethod(); would compile an error
        
        ClassMethods myObject = new ClassMethods();
        myObject.myPublicMethod(); // Call the method on an object
    }
}
