public class MultipleClasse { // main class
    public void fullThrottle(){
        System.out.println("The car is going as fast as it can!");
    }

    public void speed(int maxSpeed) {
        System.out.println("Max speed is: " + maxSpeed);
    }

    // No need for a nested class here, move the main method to the outer class
    public static void main(String[] args) {
        MultipleClasse myCar = new MultipleClasse();
        myCar.fullThrottle(); // call the full throttle method
        myCar.speed(200); // call the speed method
    }
}

 

