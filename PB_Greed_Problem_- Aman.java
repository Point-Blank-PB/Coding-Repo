package com.pointblank;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        final int n = scan.nextInt();

        if(n>=2) {

            int a[] = new int[n];
            int b[] = new int[n];

            for (int i = 0; i < n; i++)
                a[i] = scan.nextInt();

            //Total Volume
            for (int i = 0; i < n; i++)
                b[i] = scan.nextInt();


            //Max Volume that can be stored
            int largest1, largest2, temp;

            largest1 = b[0];
            largest2 = b[1];

            if (largest1 < largest2) {
                temp = largest1;
                largest1 = largest2;
                largest2 = temp;
            }

            for (int i = 2; i < b.length; i++) {
                if (b[i] > largest1) {
                    largest2 = largest1;
                    largest1 = b[i];
                } else if (b[i] > largest2 && b[i] != largest1) {
                    largest2 = b[i];
                }
            }
            int max = largest1 + largest2;

            //Remaining Volume
            int sum = 0;
            for (int i = 0; i < n; i++) {

                sum = sum + a[i];

                if(sum>max){
                    System.out.println("NO");
                    System.exit(0);
                }
            }

            System.out.println("YES");
        }
    }
}
