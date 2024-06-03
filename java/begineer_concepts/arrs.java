public class arrs {
    public static void main(String[] args) {
        // Arrays are used to store multiple values in a single variable
        // Define the variable type with square brackets
        String[] cars = {"Volvo", "Mercedes", "BMW", "Ford"};
        int[] myNums = {10, 20, 30, 40, 70};
        // Accessing of elements/items using indices

        System.out.println(cars[0]); // outputs volvo

        // Changing an element
        cars[0] = "Pagani";
        System.out.println(cars[0]); // outputs pagani
        // .length to determine length of an array
        System.out.println(cars.length);
    }
}