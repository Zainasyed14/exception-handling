try:
    print("Enter your age :")
    age=int(input())
    if(age>18):
        raise ValueError
    print("Your age is : " , age)
except ValueError:
    print("An exception has occured")
finally:
    print("The program is running")