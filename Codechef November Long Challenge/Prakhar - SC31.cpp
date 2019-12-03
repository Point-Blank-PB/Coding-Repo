#include <iostream>
#include<iomanip>

using namespace std;

int main() {
 int t;
 cin>>t;
 while(t--)
 {
    long long n,i,j,q=10;
    cin>>n;
    char A[n][q],B[q]={0};
    for(i=0;i<n;i++)
        for(j=0;j<q;j++)
            cin>>A[i][j];
    int c=0;
    for(j=0;j<q;j++)
    {
        int b=0;
        for(i=0;i<n;i++)
            b+=A[i][j];
        if(b%2!=0)
            c++;
    }
    cout<<c<<endl;
 }
}
