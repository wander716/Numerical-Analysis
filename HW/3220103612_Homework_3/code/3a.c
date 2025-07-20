#include<stdio.h>
int main ()
{
    int i,j;
    double x1,x2;
    double a[2][3]={0.03,58.9,59.2,5.31,-6.10,47};
    for(j=0;j<=2;j++)
    {
        a[0][j]=a[0][j]-a[1][0]/a[0][0]*a[0][j];//用第二行消去第一行
    }
    x2=a[0][2]/a[0][1];
    x1=(a[1][2]-a[1][1]*x2)/a[1][0];
    printf("%f %f ",x1,x2);
}