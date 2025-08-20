import java.util.Scanner;

class LastDigitCheck {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();

        int lastDigit = Math.abs(number % 10); // in case number is negative

        if (lastDigit == 4) {
            System.out.println("The last digit is 4.");
        } else {
            System.out.println("The last digit is not 4.");
        }

        scanner.close();
    }
}

