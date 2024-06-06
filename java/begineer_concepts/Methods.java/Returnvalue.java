package Methods.java;

public class Returnvalue {
    // A return value is what a function gives back
    // Use primitive data types if you want a function to return a value

    // int return value
    static int myMethod(int x) {
        return 5 + x;
    }

    // method with two parameters

    static int myAdding(int x, int y) {
        return x + y;
    }
    public static void main(String[] args) {
        System.out.println(myMethod(3));

        System.out.println(myAdding(5, 3));
    }
}
