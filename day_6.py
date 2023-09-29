
while True:
    try:
        divident = float(input("Enter divident: "))
        divisor= float(input("Enter divisor: "))
        ans=divident/divisor      
    
    except ZeroDivisionError:
        print("Enter a non zero value: ")
        
    except ValueError as err:
        print("Enter numbers not words")
        
    else:
        print(ans)
        break



