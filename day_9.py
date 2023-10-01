my_dict={'Name':'Virat','Age':34,'City':'Delhi'}
my_dict['Occupation']='Cricketer'#Adding new Key value pair
print(f"Updates Dict is : {my_dict}")

del my_dict['City']#Deleting a key value pair
print (my_dict)

#Updating the value of a specific key in the dictionary.
my_dict['Age']=36
print(my_dict['Age'])
#Checking if a key exists in the dictionary.
print(my_dict['Occupation']) #If key exists , it will return a value 
#Printing all the keys in the dictionary.
print(my_dict.keys())