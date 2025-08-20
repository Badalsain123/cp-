import java.util.Scanner;
class read {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int number;
        System.out.println("Enter a number");
        number = sc.nextInt();
        if(number%3==0 && number%10==4){
            System.out.println("The number is divisible by 3 and last digit is  4");
        }
        else{
            System.out.println("The number is not divisible by 3 and last digit is not 4");
        }
        sc.close();
    }
    
}
