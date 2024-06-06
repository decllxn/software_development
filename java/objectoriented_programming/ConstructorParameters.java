public class ConstructorParameters {
    // constructor can also take parameters
    // example
    int modelYear;
    String modelName; // Attributes of the class

    // Creating the constructor
    public ConstructorParameters(int year, String name) { // Takes parameters
        modelYear = year;
        modelName = name;
    }
    
    public static void main(String[] args) {
        ConstructorParameters myCar = new ConstructorParameters(1969, "Mustang");
        System.out.println(myCar.modelYear + " " + myCar.modelName);
    }
}
