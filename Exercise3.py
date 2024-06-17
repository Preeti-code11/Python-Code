n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while number_of_guesses,<=9
print("Guess the number")
num=int(input())
if num<n:
    print("increase the number")
    continue
if num>n:
    print("decrease the number")
    continue
if num==n:
    print("You guess the right number")
    break