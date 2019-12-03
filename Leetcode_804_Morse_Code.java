package com.javalabprogram;

import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
	// write your code here
        String[] words = {"gin", "zen", "gig", "msg"};
        String[] str = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};

        String alpha[] = new String[128];
        for(int i=0; i<26; i++)
            alpha[i+'a']=str[i];


        String[] morse = new String[words.length];
        for (int i=0; i<morse.length; i++)
            morse[i]="";

        for (int i=0; i<words.length; i++)
        {
            for (int j=0; j<words[i].length(); j++)
            {
                morse[i]=morse[i]+alpha[words[i].charAt(j)];
            }
//            System.out.println(morse[i]);
        }

        Map<String, Integer> map = new HashMap<>();
        for(int i=0; i<morse.length;i++)
        {
            if(map.containsKey(morse[i]) == false)
                map.put(morse[i],1);
            else
            {
                int oldvalue = map.get(morse[i]);
                int newvalue = oldvalue+1;
                map.put(morse[i],newvalue);
            }
        }

        int size = map.size();
        System.out.println(size);

    }
}
