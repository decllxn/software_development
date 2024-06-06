public class ClassAttribute {
    int y = 8; // Attribute of the class
    int x; // Un initialized attribute
    final int z = 50; // Make attribute immutable

    public static void main(String[] args) {
        ClassAttribute myObj = new ClassAttribute();
        System.out.println(myObj.y);

        // We can also modify attributes
        ClassAttribute myObject = new ClassAttribute();
        myObject.x = 40; // modified the attribute x
        System.out.println(myObject.x);

        ClassAttribute myObject1 = new ClassAttribute();
        System.out.println(myObject1.z);

        // Multiple objects
        // When you create multiple objects of one class, you can change the attribute
        // values in one object without affecting th attribute values in the other

        ClassAttribute Object1 = new ClassAttribute();
        ClassAttribute Object2 = new ClassAttribute();

        Object2.y = 15;
        System.out.println(Object1.y); // outputs 8
        System.out.println(Object2.y); // outputs 15
    }
}
