from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bids = {}
bidding_finished = False
def find_highest_bidder(bidding_record):
  highest_bid=0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder

  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name? :  ")
  price = int(input("What is your bid? : $"))
  bids[name]=price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()

def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  f_name = f_name.title()
  l_name = l_name.title()
  return f"{f_name} {l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
def outer_function(a, b):
  def inner_function(c, d):
      return c + d
  return inner_function(a, b)

result = outer_function(5, 10)
print(result)


programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again." , 
  # "loop":"The action of doing something over and over again"
}
# #Retrieving items from dicti
# for keys in programming_dictionary:
#   values = programming_dictionary[keys]
#   print(keys ,':', values)

#adding new values
programming_dictionary['loop']="The action of doing something over and over again"

print(programming_dictionary)




#Calculator
from replit import clear
from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
def calci():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
      print(symbol)
  
  should_continue = False
  #Here we select "+"
  while not should_continue:
      operation_symbol = input("Pick an operation: ")
      num2 = float(input("What's the next number?: "))
      calculation_function = operations[operation_symbol]
      first_answer = calculation_function(num1, num2)
  
      print(f"{num1} {operation_symbol} {num2} = {first_answer}")
      if input(
              "Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation:"
      ) == "y":
          num1 = first_answer
      else:
          should_continue = True
          clear()
          calci()

calci()
