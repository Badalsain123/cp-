import java.util.Scanner;

class triangle{
    public static void main(String[] args) {
        int a,b,c;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first angle: ");
        a = sc.nextInt();
        System.out.println("enter second angle:");
        b = sc.nextInt();
        System.out.println("enter third angle:");
        c = sc.nextInt();
        if(a+b+c==180 && a>0 && b>0 && c>0 ){
            System.out.println("It is a valid triangle");
        }
        else{
            System.out.println("It is not a valid triangle");
        }
        sc.close();
        


    }    
}
