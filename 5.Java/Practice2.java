import java.util.Arrays;
import java.util.Date;
import java.util.Scanner;

public class Practice2 {

    public static void main(String[] args) {
        System.out.println("THIS IS TASK NUMBER 1");
        Scanner scanner = new Scanner(System.in);
        System.out.print("Please enter first num : ");
        int num1 = scanner.nextByte();
        System.out.print("Please enter second num : ");
        int num2 = scanner.nextByte();
        System.out.print("Please enter third num : ");
        int num3 = scanner.nextByte();
        int total = num1+num2+num3;
        int product = num1*num2*num3;
        float avg = total/3;
        System.out.println("Sum is " + total);
        System.out.println("The product is :" + product);
        System.out.println("The average is " + avg);

        //large number checker
        if (num1 > num2 && num1 > num3)
            System.out.println(num1 +  "  is the biggest");
        else if (num2 > num1 && num2 > num3)
            System.out.println(num2 + " is the biggest");
        else if (num3 > num1 && num3 > num2)
            System.out.println(num3 + " is the biggest");
        //small number checker
        if (num1 < num2 && num1 < num3)
            System.out.println(num1 +  "  is the Smallest");
        else if (num2 < num1 && num2 < num3)
            System.out.println(num2 + " is the Smallest");
        else if (num3 < num1 && num3 < num2)
            System.out.println(num3 + " is the smallest");

    }
}
