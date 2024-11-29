'''Author: Anugrah Chandran
Date:29-11-24
Description:Recursive function to add two positive numbers.'''
def recursive_add(num1,num2):
    if num2 ==0:
        return num1
    else:
        return recursive_add(num1+1,num2-1)
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
recursive_add(number1,number2)
print("The sum of num1 and num2 is",recursive_add(number1,number2))
