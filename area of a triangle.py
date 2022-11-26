# python prg to find area of a triangle
#beware that the sum of any two sides of a triangle is greater than the third side
# when you learn error handling then resolve the issue
import cmath as mt;
a= float(input("Enter first side "));
b= float(input("Enter second side "));       
c= float(input("Enter third side "));
s=(a+b+c)/2;
area= mt.sqrt(s*(s-a)*(s-b)*(s-c));
if(((a+b)<c) or ((b+c)<a) or ((a+c)<b)):
    print("These sides do not form a triangle. \nSORRY!!")
else:
    print("The area of triangle is:",area, "\nTHANKS");




        
