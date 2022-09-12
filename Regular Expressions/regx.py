import re

# pattern = re.compile("ab")
# matches = re.finditer("ab", "abaabaaaab")
# matches = re.finditer("[abc]", "a7b@k9z")
# matches = re.finditer("[^abc]", "a7b@k9z")
# matches = re.finditer("[a-z]", "a7b@k9z")
# matches = re.finditer("[0-9]", "a7b@k9z")
# matches = re.finditer("[a-zA-Z0-9]", "a7b@k9z")

############ Predefined Character classes ############
# matches = re.finditer("\s", "a7b @k9z")
# matches = re.finditer("\S", "a7b @k9z")
# matches = re.finditer("\d", "a7b @k9z")
# matches = re.finditer("\D", "a7b @k9z")
# matches = re.finditer("\w", "a7b @k9z")
# matches = re.finditer("\W", "a7b @k9z")
# matches = re.finditer(".", "a7b @k9z")

############ Quantifiers ############
# matches = re.finditer("a", "abaabaaab")  # exactly one a
# matches = re.finditer("a+", "abaabaaab")  # at least one a
# matches = re.finditer("a*", "abaabaaab")  # any number of a including 0 number
# matches = re.finditer("a?", "abaabaaab")  # at most one a either 0 number or 1 number
matches = re.finditer("a{3}", "abaabaaab")  # exactly m number of a
# matches = re.finditer("a{m}{n}", "abaabaaab")  # min {m} number of 'a' and max {n} number of 'a'

count = 0
for match in matches:
    count += 1
    # print(match.start(), "...", match.end(), "...", match.group())
    print(match.start(), "...", match.group())
    # print("The No. of occurrences:", count)
