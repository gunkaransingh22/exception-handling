try :
    age = int(input("enter a number : "))
    print(age)
except ValueError as ex:
    print("Exception: ",ex)
print("I am outside the try block")