import re

# Regex Cheat sheet : https://www.dataquest.io/blog/regex-cheatsheet/
# Regex python tester : https://pythex.org/
# re doc : https://docs.python.org/3/library/re.html

text = "i like train" 
reg = r"[a-c]" #the group of char a to c

if re.match(reg, text): #Check if regex is correct
	print(text)
else:
  print("Not any match")