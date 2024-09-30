/*import java.util.ArrayList;
import java.util.Scanner;

public class Main1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> studentNames = new ArrayList<>();
        ArrayList<Double> studentGrades = new ArrayList<>();

        System.out.println("Enter student names (type 'q' or 'Q' to quit):");

        while (true) {
            System.out.print("Student name: ");
            String name = scanner.nextLine().trim();

            if (name.equalsIgnoreCase("q")) {
                break;
            }

            studentNames.add(name);

            System.out.print("Student grade: ");
            double grade;
            while (!scanner.hasNextDouble()) {
                System.out.print("Invalid input. Please enter a valid grade: ");
                scanner.next();
            }
            grade = scanner.nextDouble();
            scanner.nextLine();

            studentGrades.add(grade);
        }

        System.out.println("\nStudent Names and Grades:");

        for (int i = 0; i < studentNames.size(); i++) {
            System.out.printf("%s: %.2f%n", studentNames.get(i), studentGrades.get(i));
        }
    }
}
    */

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main1 {
    public static void main(String[] args) {
        // Create a queue to store the inventory items
        Queue<String> inventory = new LinkedList<>();
        // Create a scanner to read input from the user
        Scanner scanner = new Scanner(System.in);

        while (true) {
            // Print the menu
            display("***********************************");
            System.out.println("1. Add item to inventory");
            System.out.println("2. Remove item from inventory");
            System.out.println("3. Print inventory");
            System.out.println("4. Quit");
            System.out.print("Enter your choice: ");
            display("***********************************");

            // Read the user's choice
            int ask = scanner.nextInt();

            switch (ask) {
                case 1: // Add item to inventory
                    System.out.print("Enter item name: ");
                    String item = scanner.next();
                    inventory.add(item);
                    break;
                case 2: // Remove item from inventory
                    String removedItem = inventory.poll();
                    if (removedItem != null) {
                        System.out.println("Removed item: " + removedItem);
                    } else {
                        System.out.println("Inventory is empty");
                    }
                    break;
                case 3: // Print inventory
                    System.out.println("Inventory: " + inventory);
                    break;
                case 4: // Quit
                    display("Thank you for using this Queue Midget Inventory app");
                    System.exit(0);
                default:
                    display("Invalid choice, please choose a valid option");
            }
        }
    }

    static void display(String x) {
        System.out.println(x);
    }
}