import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
        Scanner scanner = new Scanner(System.in);

        int t= scanner.nextInt();
        while(t!=0){
            t--;
            int n=scanner.nextInt();
            Map<Integer,Integer> map = new HashMap<>();
            for (int i=0; i<n; i++) {
                int key = scanner.nextInt();
                int value = scanner.nextInt();

                if (key > 0 && key < 9) {
                    if (!map.containsKey(key))
                        map.put(key, value);
                    else
                    {
                        int oldValue = map.get(key);
                        if (oldValue<value)
                            map.put(key,value);
                    }
                }
            }
            int sum=0;
            for(int i : map.values())
                sum += i;
            System.out.println(sum);
        }
    }
}