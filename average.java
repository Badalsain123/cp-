import java.util.Scanner;
class average {
    public static void main(String[] args){
        int a,b,c,d,e;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first number");
        a = sc.nextInt();
        System.out.println("Enter the second number");
        b = sc.nextInt();
        System.out.println("Enter the third number");
        c = sc.nextInt();
        System.out.println("Enter the fourth number");
        d = sc.nextInt();
        System.out.println("Enter the fifth number");
        e = sc.nextInt();
        int average = (a+b+c+d+e)/5;
        System.out.println("The average of the numbers is "+average);
        sc.close();


    }

    
}
