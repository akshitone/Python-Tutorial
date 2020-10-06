# HELLO WORLD
print("Hello world")

# LIST
nums = [25, 34, 92, 8, 82, 56]
print(nums[-1])
print(nums[2:4][-1])

chars = ['akshit', 5, 3.4, '''I'm web developer
I love python
I'm from Surat and lived in Pune''']
print(chars)
print(chars[0][-1])

mix = [nums, chars]
print(mix)
print(mix[1][0][-1])
mix.clear()
print(mix)
print(min(nums))
print(max(nums))
print(sorted(nums))

# TUPLE - faster than list, not mutable
tup = (25, 76, 5, 31)
print(tup)

# SET - unique values only
s = {5, 15, 95, 25, 15, 40}
print(s)
