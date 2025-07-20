#include<stdio.h>
#include<math.h>
double f(double y,double t)
{
    return 1+y/t+pow(y/t,2);
    // return y/t-pow(y/t,2);
}
int main()
{
    // double a=1,b=2,h=0.1;
    double a=1,b=3,h=0.2;
    int n=(b-a)/h+1;
    double w[n];
    // w[0]=1;
    w[0]=0;
    for(int i=1;i<n;i++)
    {
        w[i]=w[i-1]+h*f(w[i-1],a+(i-1)*h);
        printf("ti=%f,  %f\n",a+(i-1)*h,w[i]);
    }
    printf("The result is %f",w[n-1]);
}