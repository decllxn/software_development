public class Person {
    String fname;
    String lname;
    int age;
    String Occupation;

    public static void main (String[] args) {
        Person myPerson1 = new Person();
        Person myPerson2 = new Person();

        // Creating the first object
        myPerson1.fname = "Declan";
        myPerson1.lname = "Munene";
        myPerson1.age = 21;
        myPerson1.Occupation = "Engineer";

        // Creating the second object
        myPerson2.fname = "Stacy";
        myPerson2.lname = "June";
        myPerson2.age = 20;
        myPerson2.Occupation = "IT specialist";

        System.out.println(myPerson1.Occupation);
        System.out.println(myPerson2.Occupation);
    }
}
