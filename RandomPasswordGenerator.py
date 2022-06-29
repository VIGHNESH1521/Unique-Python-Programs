import string
import random
from pywebio.input import input
from pywebio.output import put_text

length = int(input('Enter the length of password: '))
all = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
temp = random.sample(all, length)

# create the password
password = "".join(temp)
put_text(f'Password is : {password}')