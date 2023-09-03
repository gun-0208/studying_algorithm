s = input()

num_sum = 0
temp_s = []

for i in range(len(s)):
    if ord(s[i]) < ord('A'):
        num_sum += int(s[i])
    
    else:
        temp_s.append(ord(s[i]))

temp_s.sort()

new_s = ""

for i in range(len(temp_s)):
    new_s += chr(temp_s[i])

new_s += str(num_sum)

print(new_s)