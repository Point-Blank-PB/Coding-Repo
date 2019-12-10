import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        while (t!=0){
            t--;
            int c0=0, c2=0;
            int n = scanner.nextInt();
            for (int i=0; i<n; i++)
            {
                int a = scanner.nextInt();
                if(a==0)
                    c0++;
                if(a==2)
                    c2++;
            }

            int pair= ((c0*(c0-1))/2)+((c2*(c2-1))/2);
            System.out.println(pair);
        }
    }
}