import logging

# logging.debug("This is a debug message")

# logging.info("This is an info message")

# logging.warning("This is a warning message")
# # WARNING:root:This is a warning message

# logging.error("This is an error message")

# logging.critical("This is a critical message")

# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This will get logged.")

# import logging
# logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s")
# logging.warning("Hello, Warning!")
# logging.basicConfig(
#      format="{asctime} - {levelname} - {message}",
#      style="{",
#      datefmt="%Y-%m-%d %H:%M",
#  )
# logging.error("Something went wrong!")

# logging.basicConfig(
#      filename="app.log",
#      encoding="utf-8",
#      filemode="a",
#      format="{asctime} - {levelname} - {message}",
#      style="{",
#      datefmt="%Y-%m-%d %H:%M",
#  )

# logging.warning("Save me!")
# logging.basicConfig(
#      format="{asctime} - {levelname} - {message}",
#      style="{",
#      datefmt="%Y-%m-%d %H:%M",
#      level=logging.DEBUG,
#     filename="app.log",
#      encoding="utf-8",
#      filemode="a",
#  )

# name = "Samara"
# logging.debug(f"{name=}")

logging.basicConfig(
     filename="app.log",
     encoding="utf-8",
     filemode="a",
     format="{asctime} - {levelname} - {message}",
     style="{",
     datefmt="%Y-%m-%d %H:%M",
 )

donuts = 5
guests = 0
# try:
#      donuts_per_guest = donuts / guests
# except ZeroDivisionError:
#      logging.error("DonutCalculationError", exc_info=True)
try:
     donuts_per_guest = donuts / guests
except ZeroDivisionError:
     logging.exception("DonutCalculationError")