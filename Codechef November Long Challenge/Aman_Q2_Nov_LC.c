#include<stdio.h>


int main()
{
    int i,j,n, test, l, k, count=0,arr[129],x;


    arr[1]=0;
    arr[2]=0;
    arr[3]=1;
    arr[4]=0;
    l=4;


    while(l<=128)
    {
        x=arr[l];

        for(i=l-1; i>0; i--)
        {
            if(arr[i]==x)
            {
                k=i;
                break;
            }
            else
                k=l;
        }

        arr[l+1]=l-k;
        l++;
    }

    scanf("%d",&test);

    for(i=0; i<test; i++)
    {
        scanf("%d",&n);

        x=arr[n];
        count=0;

        for(j=0; j<=n; j++)
        {
            if(arr[j]==x)
                count++;
        }

        printf("%d\n",count);
    }

}
