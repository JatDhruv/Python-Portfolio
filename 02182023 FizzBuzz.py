# FizzBuzz should output FizzBuzz when a number is a multiple of 3 and 5
# Output Fizz when it's a multiple of 3
# Output Buzz when it's a multiple of 5
def FizzBuzz(n):
    for fizzbuzz in range(n):
        if fizzbuzz % 15 == 0:
            print("FizzBuzz")
        elif fizzbuzz % 3 == 0:
            print("Fizz")
        elif fizzbuzz % 5 == 0:
            print("Buzz")
        else:
            print(fizzbuzz)


number = int(input("FizzBuzz?\n"))
FizzBuzz(number)
