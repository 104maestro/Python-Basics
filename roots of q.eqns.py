# WAP to find roots of a quadratic equation 
import cmath;
import math;

a= float(input("Enter a: "))
b= float(input("Enter b: "))
c= float(input("Enter c: "))
#finding discriminant
d= b**2-(4*a*c)
# formula for finding roots of a quadratic equation
root1= (-b + cmath.sqrt(d))/(2*a)
root2= (-b - cmath.sqrt(d))/(2*a)
print("The quadratic equation is: (",a,").x**2 + (",b,").x + (",c,")") 
print("The roots of  quadratic equation are:",root1,"and",root2)
