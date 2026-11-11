text  = "Hello Python"

print(text.upper())
# hello python
print(text.lower())
# HELLO PYTHON
print(text.capitalize())
# Hello python
print(text.title())
# Hello Python
print(text.swapcase())
# hELLO pYTHON


name1 = "PYTHON"
name2 = "python"

print(name1.casefold() == name2.casefold())
# True



name = "  Ubaid  "

print(name.strip())
# Ubaid

print(name.lstrip())
# Ubaid  

print(name.rstrip())
#   Ubaid