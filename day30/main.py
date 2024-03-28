# #file not found
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key" : "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is the error tha i have created on my own")

height = float(input("Height : "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be more than 3 metres")

bmi =  weight/ height**2
print(bmi)

