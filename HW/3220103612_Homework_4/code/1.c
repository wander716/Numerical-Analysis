#include <stdio.h>
#include <stdlib.h>
#include <math.h>
double f1(double x)
{
    double result;
    result=exp(2*x)*cos(3*x);
    return result;
}
double f2(double x)
{
    double result;
    result=sin(log(x));
    return result;
}
void print1(double x0,double x1,double x2)
{
    double a1=1/(x0-x1)/(x0-x2);
    double a2=-(x1+x2)/(x0-x1)/(x0-x2);
    double a3=(x1*x2)/(x0-x1)/(x0-x2);

    double b1=1/(x1-x0)/(x1-x2);
    double b2=-(x0+x2)/(x1-x0)/(x1-x2);
    double b3=(x0*x0)/(x1-x0)/(x1-x2);

    double c1=1/(x2-x0)/(x2-x1);
    double c2=-(x0+x1)/(x2-x0)/(x2-x1);
    double c3=(x0*x1)/(x2-x0)/(x2-x1);
    
    printf("%.6f %.6f %.6f\n",a1*f1(x0)+b1*f1(x1)+c1*f1(x2),a2*f1(x0)+b2*f1(x1)+c2*f1(x2),a3*f1(x0)+b3*f1(x1)+c3*f1(x2));
}
void print2(double x0,double x1,double x2)
{
    double a1=1/(x0-x1)/(x0-x2);
    double a2=-(x1+x2)/(x0-x1)/(x0-x2);
    double a3=(x1*x2)/(x0-x1)/(x0-x2);

    double b1=1/(x1-x0)/(x1-x2);
    double b2=-(x0+x2)/(x1-x0)/(x1-x2);
    double b3=(x0*x0)/(x1-x0)/(x1-x2);

    double c1=1/(x2-x0)/(x2-x1);
    double c2=-(x0+x1)/(x2-x0)/(x2-x1);
    double c3=(x0*x1)/(x2-x0)/(x2-x1);
    
    printf("%.6f %.6f %.6f\n",a1*f2(x0)+b1*f2(x1)+c1*f2(x2),a2*f2(x0)+b2*f2(x1)+c2*f2(x2),a3*f2(x0)+b3*f2(x1)+c3*f2(x2));
}
int main()
{
    double x0=0,x1=0.3,x2=0.6;
    print1(x0,x1,x2);
    x0=2;x1=2.4;x2=2.6;
    print2(x0,x1,x2);
    
}
