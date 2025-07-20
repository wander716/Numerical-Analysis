#include <stdio.h>
#include <math.h>

double gx(double x)
{
    double result;
    result=exp(x)/(3*x);
    return result;
}

int main()
{
    int N0=100,i=1;
    double p0=0.5,p;
    printf("error     p         p0\n");
    while (i<=N0)
    {
        p=gx(p0);
        printf("%f  %f  %f\n",fabs(p-p0),p,p0);
        if(fabs(p-p0)<0.01)
        {
            printf("solution is %f  ",p);
            printf("end.\n");
            break;
        }
        i++;
        p0=p;
        if(i==N0)
        {
            printf("can not find the solution.");
        }
    }
    
    return 0;
}
