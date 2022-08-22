#PRIME NUMBERS: This program will take a number from the user and it will say if it's a prime number or not.

print("Welcome. Enter a number and I'll tell you if it's a prime a number.")

#if the input is not a positive integer, ask for it again
correct_input = False

while correct_input == False:
  num = input("Enter a positive whole number: ")
  if num.isdigit() == False:
    print("You didn't enter a positive whole number, please try again.")
  else:
    correct_input = True


#find out if the entered number is a prime number
def prime_numbers(num):
  num = int(num)
  is_prime_number = True

  for i in range(2,num):
    if num % i == 0:
      is_prime_number = False
      break

  if is_prime_number:
    return (f"The number {num} is a prime number.")
  else:
    return (f"The number {num} is not a prime number.")

result = prime_numbers(num)

print(result)

