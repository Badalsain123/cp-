import java.util.Scanner;

class Solution{
    public static void main(String[] args) {
        int n ;
        Scanner os = new Scanner(System.in);
        System.out.println("enter a number");
        n = os.nextInt();
        if(n%7==0){
            System.out.println("number is divisible by seven");
        }else{
            System.out.println("number is not divisible by seven");
        }
        os.close();

    



    }
}