import re

pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,4}+$"
email = "test@example.commmmmmm"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
