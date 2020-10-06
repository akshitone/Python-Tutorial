# DICTIONARY - key and value
data = {
    'rollno': 'MCA-235',
    'fname': 'Akshit',
    'lname': 'Mithaiwala'
}
print(data)
print(data['lname'])

key = ['rollno', 'firstname', 'lastname']
value = ['MCA-235', 'Akshit', 'Mithaiwala']
data = dict(zip(key, value))
# print(list(data))
# print(tuple(data))
# print(set(data))
print(data)
print(data['firstname'])

# VARIABLE
a = 10
b = a
print(id(a))
print(id(b))
print(b)
a = 15
print(b)
