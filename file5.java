import java.util.Scanner;

public class ComplexityExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a number (0 to 100): ");
        int number = scanner.nextInt();
        String result = checkNumber(number);
        System.out.println(result);
        scanner.close();
    }

    public static String checkNumber(int number) {
        if (number < 0) {
            return "Input is negative.";
        } else if (number == 0) {
            return "Input is zero.";
        } else if (number > 100) {
            return "Input is greater than 100.";
        } else if (number % 2 == 0) {
            return "Input is an even number.";
        } else {
            return "Input is an odd number.";
        }
    }
}
