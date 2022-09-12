import re

############ match() ############
# s = input("Enter pattern to search: ")
# matcher = re.match(s, "Aswad Ali Present")
#
# if matcher is not None:
#     print("Match is available at the beginning of the String")
#     print(matcher.start(), "...", matcher.end(), "...", matcher.group())
# else:
#     print("Search pattern not exist!")

############ fullmatch() ############
# s = input("Enter pattern to search: ")
# matcher = re.fullmatch(s, "aswadali")
#
# if matcher is not None:
#     print("Full String Matched ")
# else:
#     print("Full String not Matched")

############ search() ############
# s = input("Enter pattern to search: ")
# matcher = re.search(s, "Aswad Ali Aswad Present")
#
# if matcher is not None:
#     print("Match is available")
#     print(matcher.start(), "...", matcher.end(), "...", matcher.group())
# else:
#     print("Match is not available!")

############ findall() ############
# matcher = re.findall("[A-Z]", "Aswad Ali Aswad Present")
# print(matcher) # returns the list[]

############ finditer() ############
# matcher = re.finditer("[a-z]", "Aswad Ali Aswad Present")
#
# for match in matcher:
#     print(match.start(), "...", match.group())

############ sub() ############
# matcher = re.sub("[a-z]", "#", "a7b9c5k8z")
# print(matcher)

############ subn() ############
# matcher = re.subn("[a-z]", "#", "a7b9c5k8z")
# print(matcher) # returns tuple

############ split() ############
# matcher = re.split(",", "Naruto, Sakura, Sasukae")
# print(matcher) # prints list[]

############ search() ^ ############
# s = "Hello There"
# matcher = re.search("^Hel", s)
#
# if matcher is not None:
#     print("Target String starts with Hello")
# else:
#     print("Not starts with Hel")

############ search() $ ############
# s = "Hello There Aswad"
# matcher = re.search("Aswad$", s)
#
# if matcher is not None:
#     print("Target String ends with Aswad")
# else:
#     print("Target string Not ends with Aswad")

############ search() $ IGNORECASE ############
# s = "Hello There Aswad"
# matcher = re.search("aswad$", s, re.IGNORECASE)
#
# if matcher is not None:
#     print("Target String ends with Aswad")
# else:
#     print("Target string Not ends with Aswad")