# # import logging

# # # logging.debug("This is a debug message")

# # # logging.info("This is an info message")

# # # logging.warning("This is a warning message")
# # # # WARNING:root:This is a warning message

# # # logging.error("This is an error message")

# # # logging.critical("This is a critical message")

# # # logging.basicConfig(level=logging.DEBUG)
# # # logging.debug("This will get logged.")

# # # import logging
# # # logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s")
# # # logging.warning("Hello, Warning!")
# # # logging.basicConfig(
# # #      format="{asctime} - {levelname} - {message}",
# # #      style="{",
# # #      datefmt="%Y-%m-%d %H:%M",
# # #  )
# # # logging.error("Something went wrong!")

# # # logging.basicConfig(
# # #      filename="app.log",
# # #      encoding="utf-8",
# # #      filemode="a",
# # #      format="{asctime} - {levelname} - {message}",
# # #      style="{",
# # #      datefmt="%Y-%m-%d %H:%M",
# # #  )

# # # logging.warning("Save me!")
# # # logging.basicConfig(
# # #      format="{asctime} - {levelname} - {message}",
# # #      style="{",
# # #      datefmt="%Y-%m-%d %H:%M",
# # #      level=logging.DEBUG,
# # #     filename="app.log",
# # #      encoding="utf-8",
# # #      filemode="a",
# # #  )

# # # name = "Samara"
# # # logging.debug(f"{name=}")

# # # logging.basicConfig(
# # #      filename="app.log",
# # #      encoding="utf-8",
# # #      filemode="a",
# # #      format="{asctime} - {levelname} - {message}",
# # #      style="{",
# # #      datefmt="%Y-%m-%d %H:%M",
# # #  )

# # # donuts = 5
# # # guests = 0
# # # # try:
# # # #      donuts_per_guest = donuts / guests
# # # # except ZeroDivisionError:
# # # #      logging.error("DonutCalculationError", exc_info=True)
# # # try:
# # #      donuts_per_guest = donuts / guests
# # # except ZeroDivisionError:
# # #      logging.exception("DonutCalculationError")

# # # A simple decorator function
# # def decorator(func):
  
# #     def wrapper():
# #         print("Before calling the function.")
# #         func()
# #         print("After calling the function.")
# #     return wrapper

# # # Applying the decorator to a function
# # @decorator
# # def greet():
# #     print("Hello, World!")

# # greet()

# # from dataclasses import dataclass
 
# # @dataclass
# # class GfgArticle():
# #     """A class for holding an article content"""
 
# #     # Attributes Declaration
# #     # using Type Hints
 
# #     title: str
# #     author: str
# #     language: str
# #     upvotes: int
 
# # # A DataClass object
# # article = GfgArticle("DataClasses",
# #                      "vibhu4agarwal",
# #                      "Python", 0)
# # print(article)

# # class Fruit:
# #      def __init__(self, name, color, taste):
# #           self.name = name
# #           self.color = color
# #           self.taste = taste

# # banana = Fruit("Banana", "Yellow", "Sweet")
# # apple1 = Fruit("Apple", "Red", "Tart")
# # apple2 = Fruit("Apple", "Red", "Tart")

# # print(apple1 is apple2)

# from dataclasses import dataclass
# # @dataclass(slots=True)
# # @dataclass(kw_only=True)
# # class Fruit:
# #      # __slots__ = ['name', 'color', 'taste']
# #      name: str 
# #      color: str
# #      taste: str
# #      def __str__(self):
# #           return f'{self.name} {self.color} {self.taste}'

# # # banana = Fruit("Banana", "Yellow", "Sweet")
# # banana = Fruit(name = "Banana",color= "Yellow", taste="Sweet")
# # # banana2 = Fruit("Banana", "Yellow", "Sweet")
# # # apple = Fruit("Apple", "Red", "Tart")

# # print(banana)

# @dataclass( slots=True)
# class Person:
#      name: str
#      age: int
#      job: str = None
#      friends: list[str] = None

#      def __str__(self):
#           return f'{self.name} is  {self.age} years old and works as a {self.job}. His friends are {self.friends}'

# json: dict ={
#      'name': 'John Doe',
#      'age': 30,
#      'job': 'Engineer',
#      'friends': ['Jane Doe', 'Alice Johnson']  # list of strings
# }
# # bob = Person(**json)
# bob = Person(json['name'], json['age'], json['job'], json['friends'])
# print(bob.friends)


# # person1 = Person(name="John Doe", age=30, job="Engineer", friends=["Jane Doe", "Alice Johnson"])

# import os
# print(os.getcwd())
# from datetime import datetime



# os.chdir(r'C:\Users\hayze\Documents')
# print(os.getcwd())


# # print(os.makedirs('OS-Demo2/Subdir2'))
# # print(os.mkdirs('OS-Demo'))
# # print(os.removedirs('OS-Demo2/Subdir2'))
# # os.rename('publishers_table.csv','publish_table.csv')
# # mod_time = os.stat('publish_table.csv').st_mtime
# # print(os.listdir())
# # print(os.stat('publish_table.csv').st_size)
# # print(datetime.fromtimestamp(mod_time))
# # for dirpath, dirnames, filenames in os.walk(r'C:\Users\hayze\Documents'                     ):
# #     print('Current Path:', dirpath)
# #     print('Directories:', dirnames)
# #     print('Files:', filenames)
# #     print()

# print(os.environ.get('HOME') )




