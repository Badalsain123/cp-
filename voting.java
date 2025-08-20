import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        int age;
        Scanner obj = new Scanner(System.in);
        
        System.out.println("Enter your age: ");
        age = obj.nextInt();
        
        if (age >= 18) {
            System.out.println("You are eligible to vote.");
        } else {
            System.out.println("You are not eligible to vote.");
        }
        
        obj.close();
    }
}
