public class ClassesandObjects {

    int x = 5;
    public static void main(String[] args) {
        // OOP - object oriented programming
        // Procedural programming - Writing procedures or methods that perform operations
        // on the data
        // OOP - About creating objects that contain both data and methods
        // Classes and objects are two main aspects of OOP


        // Everything in java is associated with classes and objects, along with it's attributes
        // we use keyword class to create an object
        // In java there is already a class Main in which all the code goes into

        // so we are creating objects
        // using the new keyword
        // Example creating an object named myObj

        ClassesandObjects myObj = new ClassesandObjects();
        System.out.println(myObj.x);

        // Multiple objects
        ClassesandObjects myObj1 = new ClassesandObjects();
        ClassesandObjects myObj2 = new ClassesandObjects();

        System.out.println(myObj1.x);
        System.out.println(myObj2.x);

        // Java is an object-oriented programming language
        // Everything in java is asssociated with classes and objects
        
    }
}