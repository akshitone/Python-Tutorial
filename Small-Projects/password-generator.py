import string
import random


def pass_gen():
    str_upper = string.ascii_uppercase
    str_lower = string.ascii_lowercase
    str_digits = string.digits
    str_special = string.punctuation

    st = []
    st.extend(list(str_upper))
    st.extend(list(str_lower))
    st.extend(list(str_digits))
    st.extend(list(str_special))
    # here st contain all letters upper, lower, digit, special in a list
    random.shuffle(st)
    pass_len = int(input("Enter password length: "))
    password_generate = "".join(st[0:pass_len])
    print(password_generate)


pass_gen()
