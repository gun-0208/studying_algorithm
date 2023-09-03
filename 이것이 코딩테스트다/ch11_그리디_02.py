# 곱하기 혹은 더하기
# 각 자리 숫자가 (0부터9)로만 이루어진 문자열 s. 왼쪽 부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 x 혹은 + 연산자를 넣어
# 결과적으로 만들어질 수 있는 수중 가장 큰수
# 02984 => ((((0+2)x9)x8)x4) = 57
# 가장큰수는 항상 20억 이하의 정수가 되도록 입력이 주어짐.
# 1 <= len(s) <= 20

# 0이 있는 자리 뒤나 앞에는 항상 +를 사용한다.
# 1이 있는 자리는 곱하기보다 더하기가 1이 더 커지므로, 주변에 항상 +를 한다.
# 0과 1을 제외한 숫자들이 있는 경우에는 항상 x가 더큼.

s = input()

numbers = [int(i) for i in s]

for i in range(len(numbers)-1):
    if numbers[i] in [0,1] or numbers[i+1] in [0,1]:
        numbers[i+1] = numbers[i] + numbers[i+1]

    else:
        numbers[i+1] = numbers[i] * numbers[i+1]

result = numbers[-1]

print(result)