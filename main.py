# from modules.basic_calculator import add_two_numbers, subtract_two_numbers, greet

# import modules.basic_calculator as basic_calculator

# print(basic_calculator.greet)
# print (basic_calculator.add_two_numbers(50, 24))
# print (basic_calculator.subtract_two_numbers(24, 4))

# print (greet)
# print (add_two_numbers(50, 24))
# print (subtract_two_numbers(24, 4))



# How to use the dotenv module to load environment variables from a .env file (first install the module using pip install python-dotenv)
import os
from dotenv import load_dotenv

load_dotenv()

print(os.environ.get("SECRET_KEY"))