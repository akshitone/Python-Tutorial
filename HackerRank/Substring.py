string = 'ABCDCDC'
sub_string = 'CDC'
ln = len(sub_string)
cnt = 0
for i in range(len(string)):
    if sub_string == string[i:(i+ln)]:
        cnt = cnt + 1
print(cnt)

s = 'qA2'
print(any([i.isalnum() for i in s]))
print(any([i.isalpha() for i in s]))
print(any([i.isdigit() for i in s]))
print(any([i.islower() for i in s]))
print(any([i.isupper() for i in s]))
