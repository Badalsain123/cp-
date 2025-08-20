import java.util.Scanner;
class read{
    public static void main(String[] args) {
        int a,b,c;
        Scanner sc = new Scanner(System.in);
        System.out.println("enter first number");
        a = sc.nextInt();
        System.out.println("enter second number");
        b = sc.nextInt();
        System.out.println("enter third number");
        c = sc.nextInt();
        if(a<b && a<c){
            System.out.println("minimum number is "+a);
        }
        else{
            if(b<c && b>a){
                System.out.println("minimum number is "+b);
            }
            else{
                System.out.println("minimum number is "+c);
            }
        }
        sc.close();



    }    
}
