#Defining a function to check if given numbers are odd or even , Since we know even numbers are always divisible by 2, 
#remainder must be 0 if number is even
def  is_even(num):
    result=num%2
    return result
number=1
while number==True:
    try:
        num=int(input("Enter your number: "))
        result=is_even(num)
        if result == 0:
            print("The number is even")
        else:
            print("The number is odd")
        number = False
    except ValueError:
        print("Enter a number")



