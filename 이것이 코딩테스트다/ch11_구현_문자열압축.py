s = input()

pivot = len(s) // 2 + 1

compressed_length = len(s)

for step in range(1,pivot):
    compressed_str = ""
    compare_str = s[:step]
    cnt = 1

    for j in range(step,len(s),step):
        temp_str = s[j:j+step]

        if compare_str == temp_str:
            cnt += 1
        else:
            if cnt >= 2:
                compressed_str += (str(cnt) + compare_str)
            else:
                compressed_str += compare_str
            compare_str = temp_str
            cnt = 1
        
    compressed_str += str(cnt) + compare_str if cnt >= 2 else compare_str
    print(compressed_str)
    compressed_length = min(compressed_length,len(compressed_str))

print(compressed_length)

# 2a2ba3c