#PRIME NUMBERS: This program will take a number from the user and it will say if it's a prime number or not.

print("Welcome. Enter a number and I'll tell you if it's a prime a number.")

#if the input is not positive integer, ask for it again
correct_input = False
while correct_input == False:
  num = input("Enter a positive whole number: ")
  if num.isdigit() == False:
    print("You didn't enter a positive whole number, please try again.")
  else:
    correct_input = True

#if num has divisors except for 1 and itself, add it to the divisors list
divisors = []
num = int(num)
for i in range(2,num):
  if num % i == 0:
    divisors.append(i)

#if the list of divisor is not empty or the number is 0 or 1, it's a prime number
if divisors or num in (0, 1):
  print(f"Number {num} is not a prime number.")
  exit()
else:
  print(f"Number {num} is a prime number.")
  exit()
