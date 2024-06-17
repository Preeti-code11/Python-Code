print("Enter your age:")
age=int(input())
if(age>18):
    print("You can drive")
elif(age<18):
    print("You cannot drive")
elif(age==18):
    print("We cannot decide")
else:
    print("Invalid entry")