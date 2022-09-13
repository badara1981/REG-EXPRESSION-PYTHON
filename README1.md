# You need to - (import re)
# ^		    - Matches the beginning of the line
# $		    - Matches the end of the line
# .		    - Matches any character
# \s	    - Matches whitespace
# \S	    - Matches any non-whitespace character
# *		    - Repeat a character zero or more times
# *?	    - Repeat a character zero or more times (non-greedy)
# +		    - Repeat a character one or more times
# +?	    - Repeat a character one or more times (non-greedy)
# [aeiou]	- Matches a single character in the listed set
# [^XYZ]	- Matches a single character not in the listed set
# [a-z0-9]	- The set of characters can include a range
# (			- Indicates where string extraction is to start
# )			- Indicates where string extraction is to end 
