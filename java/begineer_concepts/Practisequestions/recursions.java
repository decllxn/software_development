package Practisequestions;


public class recursions {

    public static int numFactorial (int number) {
        if (number == 1) {
            return number;
        }
        else {
            return number * numFactorial(number - 1);
        }
    }
    public static void main(String [] args){
        System.out.println(numFactorial(9));
    }

    
}
