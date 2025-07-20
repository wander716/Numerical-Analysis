from sympy import symbols, diff

a,b,c = symbols('a b c')
alpha=0.001
g=(15*a+b*b-4*c-13)**2+(a*a+10*b-c-11)**2+(b*b*b-25*c+22)**2
dgda=diff(g,a)
dgdb=diff(g,b)
dgdc=diff(g,c)

# gradient = [dgda,dgdb,dgdc]
# print(gradient)
a_value=1
b_value=1
c_value=1
g_value = g.subs([(a, a_value), (b, b_value), (c, c_value)])
print(a_value,b_value,c_value,g_value)
for i in range (0,10):
    an = a_value - alpha * dgda.subs([(a, a_value), (b, b_value), (c, c_value)])
    bn = b_value - alpha * dgdb.subs([(a, a_value), (b, b_value), (c, c_value)])
    cn = c_value - alpha * dgdc.subs([(a, a_value), (b, b_value), (c, c_value)])
    gn = g.subs([(a, an),(b, bn), (c, cn)])
    print([an,bn,cn,gn])
    a_value = an
    b_value = bn
    c_value = cn
    if(abs(gn)<0.05):
        print("end")
        break
