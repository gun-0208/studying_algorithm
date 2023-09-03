input_data = input()

summation = 0

if '+' not in input_data and '-' not in input_data:
    summation += int(input_data)

else:
    if '-' in input_data:
        minus_split = input_data.split("-")
        
        if '+' in minus_split[0]:
            for plus in minus_split[0].split("+"):
                summation += int(plus)
        else:
            summation += int(minus_split[0])

        for data in minus_split[1:]:
            temp_sum = 0
            if '+' in data:
                for plus in data.split("+"):
                    temp_sum += int(plus)
            else:
                temp_sum += int(data)
        
            summation -= temp_sum
    
    else:
        for plus in input_data.split("+"):
            summation += int(plus)

print(summation)