print("Enter First Number: ")
num1=int(input())
print("Enter Second Number: ")
num2=int(input())
print("Enter the operator: ")
operator=input()
if(num1==45 and num2==3 and operator=="*"):
    print("555")
elif(num1==56 and num2==9 and operator=="+"):
    print("77")
elif(num1==56 and num2==6 and operator=="/"):
    print("4")
else:
    if(operator=="+"):
        print(num1+num2)
    elif(operator=="-"):
        print(num1-num2)
    elif(operator=="*"):
        print(num1*num2)
    elif(operator=="/"):
        print(num1/num2)
    else:
        print("Invalid operator")