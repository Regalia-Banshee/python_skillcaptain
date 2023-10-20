
import random
#creating a list of syllables for suitable character names
syllables=["rob","bob","lob","any","cry","try","pry","fry","mob","cat","dog","bog","all","lad","bad"]

while True:
    try:
        number_characters=int(input("Enter number of characters: "))#Taking user input as of how many characters are needed
        if 1<=number_characters<=15:
            names = random.sample(syllables, number_characters)
            print(names)
        else:
            raise IndexError("Enter a number less than 15!!")
        # this loop makes sure that the user does not enter a number higher than 15 since the size of the list is 15
        False
        break #breaks the loop
    except ValueError:
        print("Enter numbers")#gives customized error message if entered input is not an integer
    except IndexError as e:
        print(e)#gives customized error message if entered input is higher than total size of list

with open("character_names.txt","w") as file:
    file.write(f"{names}\n") #creating new files and writing the data to the new file

print(f"{number_characters} random character names have been generated and stored in file!")









