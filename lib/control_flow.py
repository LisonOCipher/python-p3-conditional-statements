#!/usr/bin/env python3

def admin_login(username, password):
    admin_username = "admin"
    admin_password = "12345"

    if username == admin_username or username == admin_username.upper() and password == admin_password:
        print("Access granted")
    else:
        print("Access denied")

def hows_the_weather(temperature):
    if temperature < 40:
        response = "brisk"
    elif 40 <= temperature <= 65:
        response = "a little chilly"
    elif temperature > 85:
        response = "too dang hot"
    else:
        response = "perfect"

    result = f"It's {response} out there!"
    print(result)

    

def fizzbuzz(num):
    def fizzbuzz(num):
      if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
      elif num % 3 == 0:
        return "Fizz"
      elif num % 5 == 0:
        return "Buzz"
      else:
        return num


def calculator(operation, num1, num2):
    def calculate(operation, num1, num2):
      operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
      }

      result = operations.get(operation, lambda x, y: None)(num1, num2)

      if result is not None:
        return result
      else:
        print("Invalid operation!")



