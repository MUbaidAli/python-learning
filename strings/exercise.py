username = "  MUHAMMAD UBAID  "
email = "  UBAID@GMAIL.COM "


# Remove extra whitespace.
# Convert username to title case.
# Convert email to lowercase.
# Check whether the email ends with @gmail.com.
# Check whether username contains only letters and spaces.

username = username.strip().title()
email = email.strip().lower()

# print(username)
# print(email)
# print(email.endswith("@gmail.com"))
# print(username.istitle())





string = "Python is easy and Python is powerful"


print(string.count(""))
print(len(string.split(" ")))
print(string.count("Python"))