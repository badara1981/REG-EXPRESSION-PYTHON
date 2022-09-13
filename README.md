# REG_EXPRESSION

a27 on Jan 7 2021 ThankComment
1. A fixed string -> abc123
2. Arbitrary repetition -> a*b ( "*" means that you can have an arbitrary
								number (possibly 0) of the previous char
3. Repeat character at least once -> a+b # ab, aaaab
4. Repeat character at most once -> a?b # b, ab
5. Repeat a character a fixed number of timers -> a{5} # aaaaa
6. Repeat a pattern a fixed number of times -> (a*b){3} # baabab, ababaaaab
7. Repeat a character or pattern a variable number of times -> a{2,4} # aa, aaa, aaaa
8. Choice of several characters -> [ab]c # ac, bc
9. Arbitrary mixture of several characters -> [ab]*c # c, aac, abbac
10. Ranges of characters -> [A-H][a-z]* # Aasdfalsd, Hb, G 