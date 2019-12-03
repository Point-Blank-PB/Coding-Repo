class Solution {
    public int balancedStringSplit(String s) {
        int count=0, bal=0;
        if(s.length()%2!=0)
            return 0;
        else{
            for(int i=0; i<s.length();i++)
            {
                if(s.charAt(i)=='L')
                    bal++;
                else
                    bal--;
                if(bal==0)
                {
                    count++;
                    continue;
                }
            }
            return count;
        }
    }
}