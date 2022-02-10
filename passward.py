import random
import string

def make_password(length):
    pswd = ""
    for _ in range(length):
        random_char = random.choice(string.ascii_letters+string.digits+string.punctuation)
        pswd = pswd + random_char
    return pswd

for _ in range(10):
    print(make_password(13))

