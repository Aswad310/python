class TooYoungException(Exception):
   def __init__(self, arg):
       self.msg=arg
class TooOldException(Exception):
   def __init__(self, arg):
       self.msg=arg

age=int(input("Enter Age:"))
if age>60:
   raise TooOldException("Your age already crossed marriage age...no chance of getting marriage")
elif age<18:
   raise TooYoungException("Plz wait some more time you will get best match soon!!!")
else:
   print("You will get match details soon by email!!!")