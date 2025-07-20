#include <stdio.h>
#include <math.h>

const double e = 2.718281828459;
const double EPS = 1e-5;

double fx(double x)
{
    double result;
    result=x*cos(x)-2*x*x+3*x-1;
    return result;
}

int main()
{
    double l=1.2,r=1.3,mid;
    int cnt;
    while(1)
    {
        mid=(l+r)/2;
        cnt++;
        printf("%d : %f\n",cnt,mid);
        if(fabs(fx(mid)) < EPS) break;
        if(fx(mid)>0) r=mid;
        else l=mid;
        if(cnt>=20)
        {
            printf("can not find the solution.");
            break;
        }
    }
    return 0;
}