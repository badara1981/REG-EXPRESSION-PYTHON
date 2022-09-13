import re

text = "test1, test2, test3"
regex = re.compile(r"test1")

# Returns range of first match
print(regex.match(text).span())

# Returns text with all matches replaces with other text
print(regex.sub("replace", text))

# Returns every match
print(regex.findall(text))

# OUT:
#
# (0, 5)
# replace, replace, replace
# ['test1', 'test2', 'test3']