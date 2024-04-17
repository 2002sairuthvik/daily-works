# from flask import Flask
# import random

# random_number = random.randint(0, 9)
# print(random_number)

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return "<h1>Guess a number between 0 and 9</h1>" \
#            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


# @app.route("/<int:guess>")
# def guess_number(guess):
#     if guess > random_number:
#         return "<h1 style='color: purple'>Too high, try again!</h1>" \
#                "<img src='https://media.giphy.com/media/fLyfhjZr9g47fTJMuk/giphy.gif?cid=790b7611kwp72y9rbriflkptkqmz5nq8r8jdwp1jp5jjfaag&ep=v1_gifs_search&rid=giphy.gif&ct=g'/>"

#     elif guess < random_number:
#         return "<h1 style='color: red'>Too low, try again!</h1>"\
#                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHZ4NDhqNTVvOWRmMjdwM3I4NmxqajFiZzY3enlwZzl1ejRrZGo5NiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Jt4sQOFEh29Ob8KAxg/giphy.gif'/>"
#     else:
#         return "<h1 style='color: green'>You found me!</h1>" \
#                "<img src='https://media.giphy.com/media/RpizrZcLTdlVFjZFFP/giphy.gif?cid=790b7611etliyu1d90fcyg7wj0n5aw6fzrq1o7ym6tjp3t2w&ep=v1_gifs_search&rid=giphy.gif&ct=g'/>"


# if __name__ == "__main__":
#     app.run(debug=True)