package com.pointblank;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scan = new Scanner (System.in);
        int n = scan.nextInt();

        if (n%2==0)
            System.out.println((int)Math.pow(2,n/2));
        else
            System.out.println(0);

    }
}
