#Defining a function to check if given numbers are odd or even , Since we know even numbers are always divisible by 2, 
#remainder must be 0 if number is even
def is_even(num):
    result=num%2
    return result

num=int(input("Enter your number: "))
result=is_even(num)
if result==0:
    print("Your number is even")
else:
    print("Your number is odd")

