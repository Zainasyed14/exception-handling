try:
    num1=int(input("Enter your first number : "))
    num2=int(input("Enter your second number : "))
    result=num1/num2
    print("The end result is : " , result)
    print("The second result is : " , result1)
except ZeroDivisionError:
    print("Division by zero is not possible")
except ValueError:
    print("Enter a numerical value in order to execute the answer")
except NameError as ex:
    print("The exception is " , ex)
except:
    print("Some error occured")
finally:
    print("I will always be there")