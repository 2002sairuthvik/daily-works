# fruits = ["apple", "banana", "cherry"]
# for i in range(len(fruits)):
#   print(fruits[i])
#   print(fruits[i] + "Pie")

# #exercise below
# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# # Write your code below this row 👇
# max = 0
# for i in range(len(student_scores)):
#   if student_scores[i] > max :
#     max = student_scores[i]
#   else:
#     max
# print(f'The highest score in the class is: {max}')

# #exercise below
# # Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆

# # Write your code below this row 👇
# th = 0
# ns =0
# avg =0 
# for x in student_heights:
#   ns+=1
#   th+=x
# avg = round(th/ns)
# print(f'total height = {th}')
# print(f'number of students = {ns}')
# print(f'average height = {avg}')

# # exercise
# target = int(input()) # Enter a number between 0 and 1000
# # 🚨 Do not change the code above ☝️

# # Write your code here 👇
# total = 0
# for i in range(2,target+1,2):
#   total+=i
# print(total)

# #exercise
# # Write your code here 👇
# target = 100
# for i in range(1,target+1):

#   if i%3 == 0 and i%5 == 0 :
#     print("FizzBuzz")
#   elif i%3 == 0:
#     print("Fizz")
#   elif i%5 == 0:
#     print("Buzz")
#   else:
#     print(i)
# import random
# lst=['a','b','c']
# sap = ''
# for char in lst:
#   sap+=random.choice(lst)
# print(sap)

# # Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# # Eazy Level - Order not randomised:
# # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# for letter in range(0,nr_letters):
#   password+= random.choice(letters)
# for symbol in range(0,nr_symbols):
#   password += random.choice(symbols)
# for num in range(0,nr_numbers):
#   password += random.choice(numbers)

# print(password)



# # Hard Level - Order of characters randomised:
# # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password = []
# for letter in range(0,nr_letters):
#   password+= random.choice(letters)
# for symbol in range(0,nr_symbols):
#   password += random.choice(symbols)
# for num in range(0,nr_numbers):
#   password += random.choice(numbers)

# random.shuffle(password)
# passwd = ""
# for char in password:
#   passwd += char
# print(passwd)
# for ch in password:
#   passwd+= random.choice(password)
# print(password)