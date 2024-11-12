#Basic Calculator Program
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation(+,-,*,/): ")
#Perform the operation based on the user's input
if operation == "+":
    result = num1 + num2
elif operation == "-":
 result = num1 - num2
elif operation == "*":
   result = num1 * num2
elif operation == "/":
 if num2 != 0:
   result = num1/num2
 else:
   result = "Error! Division by zero."
else:
  result = "Invalid operation!"
print(f"The result is: {result}")

