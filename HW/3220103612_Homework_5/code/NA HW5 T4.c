#include<stdio.h>
#include<math.h>
double f1(double x)
{
    return cos(x)*cos(x);
}
double f2(double x)
{
    return x*log(x+1);
}
double f3(double x)
{
    return (sin(x)*sin(x)-2*x*sin(x)+1);
}
double f4(double x)
{
    return 1/(x*log(x));
}
double trapezoidal(double l, double r,int n,int number)
{
    double h=(r-l)/n;
    double t=l+h;
    double sum1=0;
    switch (number)
    {
        case 1:
            while(t<r)
            {
                sum1+=2*f1(t);t+=h;
            }
            return (sum1+f1(l)+f1(r))*h/2;
            break;
        case 2:
            while(t<r)
            {
                sum1+=2*f2(t);t+=h;
            }
            return (sum1+f2(l)+f2(r))*h/2;
            break;
        case 3:
            while(t<r)
            {
                sum1+=2*f3(t);t+=h;
            }
            return (sum1+f3(l)+f3(r))*h/2;
            break;
        case 4:
            while(t<r)
            {
                sum1+=2*f4(t);t+=h;
            }
            return (sum1+f4(l)+f4(r))*h/2;
            break;
        default:
            break;
    }
    
}
double romberg(double l, double r,int number)
{
    double R11=trapezoidal(l,r,1,number),R21=trapezoidal(l,r,2,number),R31=trapezoidal(l,r,4,number);
    double R22=(4*R21-R11)/3,R32=(4*R31-R21)/3;
    double R33=(16*R32-R22)/15;
    return R33;
}
int main()
{
    double e=2.718281828459;
    double l1=-1,r1=1;
    double l2=-0.75,r2=0.75;
    double l3=1,r3=4;
    double l4=e,r4=2*e;
    printf("a.%f\n",romberg(l1,r1,1));
    printf("b.%f\n",romberg(l2,r2,2));
    printf("c.%f\n",romberg(l3,r3,3));
    printf("d.%f\n",romberg(l4,r4,4));
}