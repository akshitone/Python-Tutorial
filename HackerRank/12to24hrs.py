s = '12:05:45PM'
if s[-2:] == 'PM' and s[:2] != '12':
    s = str(12 + int(s[:2])) + s[2:-2]
if s[-2:] == 'AM' and s[:2] == '12':
    s = '00' + s[2:-2]

print(s)
