import java.util.Scanner;
class grade {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of students: ");
        int grade = sc.nextInt();
        if (grade >= 90) {
            System.out.println("Grade A");
        } 
        else{
            if (grade >= 80) {
                System.out.println("Grade B");
            }
            else{
                System.out.println("Grade C");
            }
        }
        sc.close();
            

    
    }
}