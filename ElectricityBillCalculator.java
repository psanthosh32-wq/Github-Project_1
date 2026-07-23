package githubemc2;
import java.util.Scanner;

public class ElectricityBillCalculator {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        // Input
        System.out.print("Enter Consumer Name: ");
        String name = scan.nextLine();

        System.out.print("Enter Consumer ID: ");
        int id = scan.nextInt();

        System.out.print("Enter Units Consumed: ");
        int units = scan.nextInt();

        double bill = 0;

        // Calculate Bill
        if (units <= 100) {
            bill = units * 1.5;
        } else if (units <= 200) {
            bill = (100 * 1.5) + ((units - 100) * 2.5);
        } else {
            bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4.0);
        }

        // Output
        System.out.println("\n----- Electricity Bill -----");
        System.out.println("Consumer Name : " + name);
        System.out.println("Consumer ID   : " + id);
        System.out.println("Units Consumed: " + units);
        System.out.println("Bill Amount   : Rs. " + bill);

        // scan.close();
    }
}