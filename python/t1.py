import re

s = "ApPLe-darwin"
print(s.replace("-", " "))
re.sub(r"([A-Z]+)", r" \1", s.replace("-", " "))
print(s)
