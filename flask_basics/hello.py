# from flask import Flask
# app = Flask(__name__)

# def make_bold(func):
#     def in_bold():
#         return "<b>" + func() + "</b>"
#     return in_bold

# def make_emphasis(func):
#     def in_em():
#         return "<em>" + func() + "</em>"
#     return in_em

# def make_underlined(func):
#     def in_ul():
#         return "<u>" + func() + "</u>"
#     return in_ul



# @app.route('/')
# def hello_world():
#     return '<h1 style="text-align : center">Hello World!</h1>'\
#             '<p>This is a paragraph</p>'\
#             '<img src="https://media.giphy.com/media/YRVP7mapl24G6RNkwJ/giphy.gif?cid=790b7611xuvosx24tiqatdh5khvpkqv3pushhv4c1dz1mffh&ep=v1_gifs_search&rid=giphy.gif&ct=g" width=200>'

# #different routes using app.route decorator
# @app.route('/bye')
# @make_bold
# @make_emphasis
# @make_underlined
# def bye():
#     return 'Bye!!!!!!'

# #creating variable paths and converting the path to a specified data type
# @app.route('/username/<name>/<int:number>')
# def greet(name, number):
#     return f"Hello there {name}, you are {number} years old."


# if __name__ == "__main__":
#     #run the app in debug mode to auto reload the server
#     app.run(debug=True)