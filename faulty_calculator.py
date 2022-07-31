print("enter the first number")
firstnumber=int(input())
print("enter the sencond number")
secondnumber=int(input())
print("enter the oprators +,-,/,*")
operatr=input()
if firstnumber==45 and secondnumber==3 and operatr=='*':
    print("555")
elif firstnumber==56 and secondnumber==9 and operatr=='+':
    print("77")
elif firstnumber==56 and secondnumber==6 and operatr=='/':
    print("4")
elif operatr=='+':
    print("plus = ",firstnumber+secondnumber)
elif operatr=='*':
    print("Multiplication = ",firstnumber*secondnumber)
elif operatr=='-':
    print("subtraction = ",firstnumber-secondnumber)
elif operatr=='/':
    print("division = ",firstnumber/secondnumber)
else:
    print("invalid input")