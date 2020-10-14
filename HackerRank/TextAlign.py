# w = 20
# print('Akshit'.center(w, '-'))
n = 11
m = 33
n = (int(input()))
m = (int(input()))
for i in range(1, n, 2):
    st = '.|.'*i 
    print(st.center(m, '-'))

print('WELCOME'.center(m, '-'))

for i in range(n-2, 0, -2):
    st = '.|.'*i
    print(st.center(m, '-'))
